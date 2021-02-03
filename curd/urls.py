
from rest_framework import routers
from .views import *

app_name='curd'

router = routers.SimpleRouter()
router.register(r'students', StudentCurd, basename="students")
urlpatterns = router.urls