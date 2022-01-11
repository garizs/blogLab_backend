"""
    API получения постов
"""
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_301_MOVED_PERMANENTLY

from apps.posts.models import Post, FavouritePosts
from apps.posts.serializers import PostBasicSerializer, PostFavouriteSerializer


@extend_schema(tags=['Посты'])
class PostsViewSet(viewsets.ModelViewSet):  # pylint: disable=too-many-ancestors
    """
        Работа с постами
    """
    serializer_class = PostBasicSerializer
    queryset = Post.objects.all()
    http_method_names = ['get', 'post']

    def create(self, request, *args, **kwargs):
        return Response(data={'status': 'API недоступно'}, status=HTTP_301_MOVED_PERMANENTLY)

    def list(self, request, *args, **kwargs):
        return Response(data={'status': 'API недоступно'}, status=HTTP_301_MOVED_PERMANENTLY)

    def retrieve(self, request, *args, **kwargs):
        return Response(data={'status': 'API недоступно'}, status=HTTP_301_MOVED_PERMANENTLY)

    @action(detail=False, methods=['get'])
    def get_main_posts(self, request):
        """
            Получние постов с главной страницы
        """
        main_posts = Post.objects.filter(post_type='MAIN')

        serializer = self.get_serializer(main_posts, many=True)
        return Response(serializer.data)

    @extend_schema(
        parameters=[
            OpenApiParameter(name='type', location='query', description='Тип документа', required=True, type=str),
        ],
    )
    @action(detail=False, methods=['get'])
    def get_posts_by_type(self, request):
        """
        Получение постов по типу
        """
        post_type = request.query_params.get('type')
        posts = Post.objects.filter(post_type=post_type.upper())
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'], permission_classes=(permissions.IsAuthenticated,),
            serializer_class=PostFavouriteSerializer)
    def add_to_favourite(self, request):
        user = request.user.userprofile
        post_id = request.data.get('id')

        FavouritePosts.objects.update_or_create(user=user, post_id=post_id)

        favourite_post = FavouritePosts.objects.filter(user=user, post_id=post_id).values('post_id')
        data = Post.objects.filter(id__in=favourite_post).first()

        serializer = self.get_serializer(data, many=False)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], permission_classes=(permissions.IsAuthenticated,))
    def get_favourites_posts(self, request):
        """
            Получение избранных постов
        """
        user = request.user.userprofile

        favourites_posts = FavouritePosts.objects.filter(user=user).values('post_id')
        data = Post.objects.filter(id__in=favourites_posts)

        serializer = self.get_serializer(data, many=True)
        return Response(serializer.data)
