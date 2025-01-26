# main.py
from extract_audio import extract_audio
from transcribe_audio import transcribe_audio
from translate_text import translate_text_with_node
from create_srt import create_srt

def main(video_file, target_language):
    """
    Orchestrates the entire process of extracting audio, transcribing it,
    translating it, and generating subtitles.
    """
    # Step 1: Extract Audio
    audio_file = extract_audio(video_file)

    # Step 2: Transcribe Audio
    transcription = transcribe_audio(audio_file)
    
    if transcription:
        print("Transcription successful:", transcription)

        # Step 3: Translate Text using Node.js script
        translated_text = translate_text_with_node(transcription, target_language)
        
        if translated_text:
            print("Translation successful:", translated_text)

            # Step 4: Create Subtitle File
            create_srt(translated_text, "output_subtitles.srt")
            print("Subtitle file created successfully.")
        else:
            print("Translation failed.")
    else:
        print("Transcription failed.")

# Example usage
if __name__ == "__main__":
    main("C:\\Users\\BunnyPreethi\\Downloads\\l.mp4", "hi")  # Replace with actual video path and target language code.
