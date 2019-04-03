from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import Choice,Track,Question

class QuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question_text')

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'question', 'choice_text', 'votes')

class TrackSerializer(serializers.ModelSerializer):
    questions = QuesSerializer(many=True)
    class Meta:
        model = Track
        fields = ('id','name','questions')

    def create(self, validated_data):
        print(validated_data)
        question_data = validated_data.pop('questions')
        track = Track.objects.create(**validated_data)
        for question in question_data:
            Question.objects.create(tracks=track, **question)
        return track


class QuesViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuesSerializer

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer