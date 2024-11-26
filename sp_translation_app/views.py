from django.shortcuts import render
from .serializers import TranslationRequestS, TranslationResponseS
from rest_framework.views import APIView
from .sp_sp_translation import SpeechTranslationApp
from rest_framework.response import Response
from rest_framework import status
import wave
from io import BytesIO
from pydub import AudioSegment
import speech_recognition as sr

# Create your views here.
class sp_translation(APIView):
    def post(self, request):
        serializer = TranslationRequestS(data=request.data)
        if serializer.is_valid():
            # Getting inputs from HTML
            audio_file = serializer.validated_data['audio']
            language = serializer.validated_data['language']

            #Processing the audio for input
            audio_file = audio_file.read() 
            audio = AudioSegment.from_file(BytesIO(audio_file))  # Automatically detects file type
            # Export as WAV to a new BytesIO object
            wav_bytes = BytesIO()
            audio.export(wav_bytes, format="wav")
            wav_bytes.seek(0) 
            audio_data = sr.AudioData(wav_bytes.read(), 48000, 2)
            
            # Passing the data into the model
            model = SpeechTranslationApp(audio = audio_data, language = language)

            # Fetching translated text
            translated_text = model.translate()
        # Passing translated text to response serializer 
        response_serializer = TranslationResponseS({'translated_text': translated_text})
        return Response(response_serializer.data, status = status.HTTP_200_OK)

# Create your views here.
def home(request):
    return render(request, 'sp_translation_app/index.html')