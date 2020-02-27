from rest_framework import mixins
from rest_framework import viewsets

from .models import Project
from .pagination import CommonPagination
from .serializers import ProjectSerializers


# Create your views here.

class ProjectViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    公司项目列表
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializers
    pagination_class = CommonPagination
