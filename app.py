import streamlit as st
import os
from extract_audio import extract_audio
from transcribe_audio import transcribe_audio
from translate_text import translate_text_with_node
from create_srt import create_srt

# Ensure the temp directory exists
TEMP_DIR = "temp"
os.makedirs(TEMP_DIR, exist_ok=True)

def main():
    st.title("Video to Subtitle Generator")
    st.markdown("""
        **Upload a video file**, select a target language, and generate subtitles.
        - Supported formats: MP4, MPEG4
        - Max file size: 200MB
    """)

    # Step 1: File Upload
    uploaded_file = st.file_uploader("Upload a Video File", type=["mp4", "mpeg4"])
    
    # Step 2: Language Selection
    target_language = st.selectbox("Select Target Language", ["hi", "es", "fr", "de"])  # Add more languages as needed

    if st.button("Process"):
        if uploaded_file is not None:
            # Save the uploaded file temporarily in the temp directory
            video_file_path = os.path.join(TEMP_DIR, uploaded_file.name)
            with open(video_file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.success(f"File uploaded successfully: {uploaded_file.name}")

            try:
                # Step 3: Extract Audio
                st.info("Extracting audio from video...")
                audio_file = extract_audio(video_file_path)
                st.success("Audio extracted successfully!")

                # Step 4: Transcribe Audio
                st.info("Transcribing audio...")
                transcription = transcribe_audio(audio_file)
                
                if transcription:
                    st.success("Transcription successful!")
                    st.text_area("Transcription Output", transcription, height=200)

                    # Step 5: Translate Text using Node.js script
                    st.info("Translating text...")
                    translated_text = translate_text_with_node(transcription, target_language)
                    
                    if translated_text:
                        st.success("Translation successful!")
                        st.text_area("Translated Output", translated_text, height=200)

                        # Step 6: Create Subtitle File
                        srt_filename = os.path.join(TEMP_DIR, "output_subtitles.srt")
                        create_srt(translated_text, srt_filename)
                        
                        with open(srt_filename, "rb") as f:
                            st.download_button(
                                label="Download Subtitles",
                                data=f,
                                file_name="output_subtitles.srt",
                                mime="text/srt"
                            )
                        st.success("Subtitle file created successfully!")
                    else:
                        st.error("Translation failed.")
                else:
                    st.error("Transcription failed.")
            except Exception as e:
                st.error(f"An error occurred during processing: {e}")
        else:
            st.error("Please upload a video file.")

if __name__ == "__main__":
    main()
