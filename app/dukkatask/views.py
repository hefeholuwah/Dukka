from rest_framework import generics
from rest_framework.response import Response
from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework.permissions import IsAuthenticated
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


class UserProfileLoginView(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def retrieve(self, request, *args, **kwargs):
        audio_file = self.request.FILES.get('audio_file')

        # Use SpeechRecognition to convert audio to text
        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_file) as source:
            audio_text = recognizer.recognize_google(source)

        # Separate email and password from the recognized speech text
        email, password = map(str.strip, audio_text.split(';'))

        # You might want to perform more sophisticated authentication logic here
        # For demonstration, we're checking if the user with the provided email and password exists
        try:
            user_profile = UserProfile.objects.get(email=email, password=password)
        except UserProfile.DoesNotExist:
            return Response({'error': 'Invalid email or password'}, status=400)

        serializer = self.get_serializer(user_profile)
        return Response(serializer.data)

class UserProfileWelcomeView(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def retrieve(self, request, *args, **kwargs):
        user_profile = self.request.user  # Assuming you are using Django's built-in authentication

        # Generate a welcome message
        welcome_message = f"Welcome back, {user_profile.full_name}! You have successfully logged in."
        return Response({'welcome_message': welcome_message})