from rest_framework.authentication import (
    BaseAuthentication,
    BasicAuthentication,
    SessionAuthentication,
)
from rest_framework.generics import ListAPIView
from rest_framework.permissions import (
    BasePermission,
    IsAuthenticated,
)
from rest_framework.serializers import Serializer

from news.models.article import Article
from news.models.country import Country
from news.models.source import Source
from users.models.subscription import Subscription
from api_newsfeed.serializers import ArticleSerializer

class NewsfeedList(ListAPIView):
    authentication_classes: list[BaseAuthentication] = [SessionAuthentication, BasicAuthentication]
    permission_classes:     list[BasePermission]     = [IsAuthenticated]
    serializer_class:       Serializer               = ArticleSerializer
    paginate_by:            int                      = 5


    def get_queryset(self):
        try:
            sources: list[Source] = (
                Subscription.objects.get(user=self.request.user).sources.all()
            )

            countries: list[Country] = (
                Subscription.objects.get(user=self.request.user).countries.all()
            )

            return (
                Article.objects.filter(source__in=sources).all() |
                Article.objects.filter(source__country__in=countries).all()
            )
        except Subscription.DoesNotExist:
            return Article.objects.none()
