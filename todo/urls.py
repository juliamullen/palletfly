from rest_framework.routers import DefaultRouter
from todo.views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = router.urls
