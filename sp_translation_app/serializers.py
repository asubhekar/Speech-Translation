from rest_framework import serializers

class TranslationRequestS(serializers.Serializer):
    audio = serializers.FileField(required=True)  # To handle audio file
    language = serializers.CharField(max_length=10)

class TranslationResponseS(serializers.Serializer):
    translated_text = serializers.CharField(max_length = 500)