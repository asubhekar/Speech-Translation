
import torch
import speech_recognition as sr
from transformers import pipeline, AutoProcessor
from langdetect import detect
from gtts import gTTS

import io


class SpeechTranslationApp:
    def __init__(self, audio, language: str = 'en'):
        
        self.audio = audio
        self.lang2 = language

        self.text, self.lang1 = self.speech_to_text(audio = self.audio)

        self.translated_text = self.text_to_text(self.text, self.lang1, self.lang2)


    def speech_to_text(self, audio):
        recognizer = sr.Recognizer()
        # Recognizing text and language
        text = recognizer.recognize_google(audio)
        lang1 = detect(text)
        return text, lang1
    
    def text_to_text(self, text, lang1, lang2):
        # Initializing the model
        translation_model = f'Helsinki-NLP/opus-mt-{lang1}-{lang2}'

        translation_pipeline = pipeline("translation", model = translation_model, clean_up_tokenization_spaces = True, device=0 if torch.cuda.is_available() else -1)

        return translation_pipeline(text)[0]["translation_text"]
    
    def translate(self):
        return self.translated_text



