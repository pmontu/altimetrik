from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ViewSetMixin
from rest_framework.mixins import CreateModelMixin
from .models import Article
from .serializers import ArticleSerializer


class ArticleViewSet(CreateModelMixin, ViewSetMixin, GenericAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
