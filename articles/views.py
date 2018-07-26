from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.viewsets import ViewSetMixin
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Article
from .serializers import ArticleSerializer


class ArticleViewSet(ListModelMixin, CreateModelMixin, ViewSetMixin, GenericAPIView):
	queryset = Article.objects.all().order_by("-votes")
	serializer_class = ArticleSerializer


@api_view(['POST'])
def vote(request, article_id):
	article = get_object_or_404(Article.objects.all(), id=article_id)
	article.votes += 1
	article.save()
	return Response(article.votes, status=status.HTTP_201_CREATED)
