# translate_text.py
import subprocess

def translate_text_with_node(input_text, target_language):
    """
    Translates text to a target language by calling a Node.js script.
    """
    try:
        result = subprocess.run(
            ['node', 'C:\\Users\\BunnyPreethi\\p\\translate.mjs', input_text, target_language],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode == 0:
            return result.stdout.strip()  # Translated text from Node.js script
        else:
            print("Error in translation:", result.stderr)
            return None
    except Exception as e:
        print(f"An error occurred while calling Node.js script: {e}")
        return None
