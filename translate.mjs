import { translate } from '@vitalets/google-translate-api';

async function translateText(inputText, targetLanguage) {
    try {
        const { text } = await translate(inputText, { to: targetLanguage });
        console.log(text); // Output the translated text
    } catch (error) {
        console.error('Error during translation:', error.message);
    }
}

// Example usage: Pass arguments from Python via command line
const inputText = process.argv[2]; // Text to be translated
const targetLanguage = process.argv[3]; // Target language (e.g., 'en', 'hi')
translateText(inputText, targetLanguage);
