from rest_framework import serializers
from events.models import Category,Person,Organiser,Speaker,Schedule,Program,Event,File


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class OrganiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organiser
        fields = '__all__'

class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    program = serializers.HyperlinkedRelatedField(many=True,view_name='program-detail',read_only=True)
    class Meta:
        model = Schedule
        fields = ['title','date','program']

class ProgramSerailizer(serializers.ModelSerializer):
    speaker = serializers.HyperlinkedRelatedField(many=True,view_name='speaker-detail',read_only=True)
    class Meta:
        model = Program
        fields = ['title','description','time','speaker']

class EventSerializer(serializers.Serializer):
    category = serializers.HyperlinkedRelatedField(many=True,view_name='category-detail',read_only=True)
    organiser = serializers.HyperlinkedRelatedField(many=True,view_name='organiser-detail',read_only=True)
    person = serializers.HyperlinkedRelatedField(many=True,view_name='person-detail',read_only=True)
    class Meta:
        model = Event
        fields = ['title','slug','featured_image','category','start_date','end_date','venue','description','tags','organiser','person','date_added','date_edited','featured','block','schedule']

class FileSerialzer(serializers.Serializer):
    event = serializers.HyperlinkedRelatedField(many=True,view_name='event-detail',read_only=True)
    class Meta:
        model = File
        fields = ['file','event']



