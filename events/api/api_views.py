from .serializers import ScheduleSerializer,CategorySerializer,PersonSerializer,OrganiserSerializer,SpeakerSerializer,ProgramSerailizer,EventSerializer,FileSerialzer
from rest_framework import viewsets
from events.models import Category,Person,Organiser,Speaker,Schedule,Program,Event,File
from rest_framework import permissions


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAuthenticated]

class OrganiserViewSet(viewsets.ModelViewSet):
    queryset = Organiser.objects.all()
    serializer_class = OrganiserSerializer
    permission_classes = [permissions.IsAuthenticated]

class SpeakerViewSet(viewsets.ModelViewSet):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer
    permission_classes = [permissions.IsAuthenticated]

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerailizer
    permission_classes = [permissions.IsAuthenticated]

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerialzer
    permission_classes = [permissions.IsAuthenticated]