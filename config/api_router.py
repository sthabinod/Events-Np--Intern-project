
from rest_framework import routers

from blogs.views import BlogViewSet
from core.views import ContactViewSet
from events.api.api_views import EventViewSet,FileViewSet,SpeakerViewSet,ScheduleViewSet,OrganiserViewSet,CategoryViewSet,PersonViewSet,ProgramViewSet
from blogs.api.api_views import UserViewSet

router = routers.DefaultRouter()

router.register('users', UserViewSet)
router.register('event', EventViewSet)
router.register('blog', BlogViewSet)
router.register('contact',ContactViewSet)
router.register('file',FileViewSet)
router.register('speaker',SpeakerViewSet)
router.register('schedule',ScheduleViewSet)
router.register('category',CategoryViewSet)
router.register('program',PersonViewSet)
router.register('organiser',OrganiserViewSet)