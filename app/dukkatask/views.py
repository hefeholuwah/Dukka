# yourapp/views.py
from rest_framework import generics
from .models import UserProfile
from .serializers import UserProfileSerializer
import speech_recognition as sr
from gtts import gTTS
import os

class UserProfileCreateView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def perform_create(self, serializer):
        audio_file = self.request.FILES.get('audio_file')
        
        # Use SpeechRecognition to convert audio to text
        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_file) as source:
            audio_text = recognizer.recognize_google(source)

        # Save the text to the serializer
        serializer.validated_data['speech_text'] = audio_text

        # Continue with normal serialization and save
        serializer.save()

                # Generate welcome message
        welcome_message = "Welcome to our platform. Your account has been created successfully."
        tts = gTTS(welcome_message)
        tts.save("welcome_message.mp3")

        # Save the welcome message file path to the serializer
        serializer.validated_data['welcome_message'] = "welcome_message.mp3"

        serializer.save()
