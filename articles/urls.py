from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import ArticleViewSet, vote

router = SimpleRouter()
router.register("articles", ArticleViewSet)

urlpatterns = [
	path('articles/<int:article_id>/votes/', vote),
]

urlpatterns += router.urls