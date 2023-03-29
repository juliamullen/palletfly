from rest_framework   import viewsets
from todo.models      import Task
from todo.serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset         = Task.objects.all()
