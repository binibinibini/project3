import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import tempfile, os, base64

try:
    from inference_sdk import InferenceHTTPClient
except Exception:
    InferenceHTTPClient = None

def run_monitor_detection():
    st.subheader("📸 이미지 분석")

    # 촬영 가이드라인 섹션
    st.markdown(" ")
    st.markdown(" ")
    st.markdown("#### 💡 올바른 사진 촬영 가이드")
    st.info("정확한 분석을 위해, 아래 가이드를 참고하여 책상 사진을 찍어주세요.")


    col1, col2 = st.columns([1.0, 1.0])  # 텍스트와 이미지 영역 비율

    with col1:
        st.markdown(
            """
            **이렇게 찍어주세요:**
            * **1. 정면에서 촬영:** 평소에 의자에 앉은 시선으로 책상 정면을 찍어주세요.
            * **2. 전체가 나오게:** 책상 위에 있는 모니터, 노트북, 키보드, 마우스가 모두 보여야 합니다.
            * **3. 주변 환경 포함:** 책상 위 조명이나 주변 창문이 있다면 함께 나오는 것이 좋습니다.
            * **4. 선명하게:** 너무 어둡거나, 흔들리거나, 물체가 가려지지 않게 찍어주세요.
            """
        )

    with col2:
        st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True)


        image_path = "C:/workspace/website_frame/project/가이드라인 사진.jpg"

        try:
            st.image(image_path, caption="예시 사진", use_container_width=True)
        except FileNotFoundError:
            st.warning("가이드라인 이미지를 찾을 수 없습니다.")
            st.markdown(f"경로 확인 필요: `{image_path}`")
            
            # 이미지를 못찾을 경우를 대비한 Placeholder
            with st.container(border=True, height=200):
                st.markdown(
                    """
                    <div style='display: flex; align-items: center; justify-content: center; height: 100%; text-align: center; color: gray;'>
                        ( 🖼️ 예시 사진 )<br>
                        (이미지 로드 실패)
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        except Exception as e:
            st.error(f"이미지 로드 중 오류 발생: {e}")

    st.markdown("---")


    uploaded_file = st.file_uploader("분석할 이미지를 업로드하세요", type=["jpg", "jpeg", "png"])
    if not uploaded_file:
        st.info("이미지를 업로드하면 자동으로 감지 및 시각화 결과가 표시됩니다.")
        return

    image = Image.open(uploaded_file).convert("RGB")

    if InferenceHTTPClient is None:
        st.error("Roboflow 클라이언트 모듈(inference_sdk)을 찾을 수 없습니다.")
        return

    client = InferenceHTTPClient(
        api_url="https://serverless.roboflow.com",
        api_key=st.secrets.get("ROBOFLOW_API_KEY", "")
    )
    if not st.secrets.get("ROBOFLOW_API_KEY"):
        st.warning("Roboflow API 키가 설정되어 있지 않습니다. st.secrets에 ROBOFLOW_API_KEY를 등록하세요.")

    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as temp_file:
        temp_file.write(uploaded_file.getvalue())
        temp_path = temp_file.name

    status_text = st.empty()
    status_text.info("✨ 객체를 감지하는 중입니다...")

    try:
        result = client.run_workflow(
            workspace_name="yujin-qkjrt",
            workflow_id="detect-count-and-visualize-14",
            images={"image": temp_path},
            use_cache=True
        )
        status_text.empty()
        data = result[0]
        detections = data.get("predictions", {}).get("predictions", [])
        output_b64 = data.get("output_image")
        screens = [obj for obj in detections if obj.get("class") in ["screen", "monitor", "laptop"]]

        if output_b64:
            st.image(base64.b64decode(output_b64), caption="📊 객체 탐지 결과", use_container_width=True)

        if len(screens) > 0:
            draw_img = image.copy()
            draw = ImageDraw.Draw(draw_img, "RGBA")
            try:
                font = ImageFont.truetype("arial.ttf", 36)
            except Exception:
                font = ImageFont.load_default()

            for idx, obj in enumerate(screens):
                # Roboflow 예측 포맷에 맞춘 좌표 처리: x,y,width,height 중심좌표 가정
                x, y, w, h = obj.get("x"), obj.get("y"), obj.get("width"), obj.get("height")
                left, top = x - w / 2, y - h / 2
                right, bottom = x + w / 2, y + h / 2
                draw.rectangle([left, top, right, bottom], outline="red", width=4)
                num = str(idx + 1)
                try:
                    bbox = draw.textbbox((0, 0), num, font=font)
                    text_w, text_h = bbox[2] - bbox[0], bbox[3] - bbox[1]
                except AttributeError:
                    text_w, text_h = font.getsize(num)
                cx, cy = (left + right) / 2, (top + bottom) / 2
                draw.rectangle(
                    [cx - text_w/2 - 8, cy - text_h/2 - 8,
                     cx + text_w/2 + 8, cy + text_h/2 + 8],
                    fill=(255, 0, 0, 160)
                )
                draw.text((cx - text_w/2, cy - text_h/2), num, font=font, fill="white")

            st.image(draw_img, caption="감지된 스크린 번호 표시", use_container_width=True)

            if len(screens) > 1:
                st.warning(f"🖥️ 스크린이 {len(screens)}개 감지되었습니다. 메인 스크린을 선택해주세요.")
                selected_idx = st.radio("메인 스크린 번호 선택:", options=[i + 1 for i in range(len(screens))], horizontal=True)
                main_screen = screens[selected_idx - 1]
            else:
                main_screen = screens[0]
                st.info("✅ 스크린이 1개 감지되어 자동 선택되었습니다.")

            monitor_inch = st.number_input("메인 스크린 인치 입력 (예: 27)", min_value=5.0, max_value=60.0, value=27.0, step=0.5)

            # session_state에 저장 (app.py가 흐름 제어)
            st.session_state["workflow_result"] = result
            st.session_state["main_screen"] = main_screen
            st.session_state["monitor_inch"] = monitor_inch
        else:
            st.error("❌ 스크린 또는 랩탑 객체가 감지되지 않았습니다.")
    except Exception as e:
        status_text.empty()
        st.error(f"🚨 오류 발생: {e}")
    finally:
        try:
            os.remove(temp_path)
        except Exception:
            pass
