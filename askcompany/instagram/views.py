from django.shortcuts import render
from django.template.response import TemplateResponse
from rest_framework import generics, serializers
from rest_framework.generics import RetrieveAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view,action, authentication_classes, renderer_classes
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post

# def post_list(requeset):
#     pass
    
# def post_detail(request, pk):
#     # request.method # = > 3개분기
#     pass

# 이 모델 뷰셋이
# 저 위의 함수 view와 같은것을 지원한다.
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # authentication_classes = [] login_required
    
    def perform_create(self, serializer):
        # FIXME 로그인이돼있다는 가정하
        author = self.request.user # User or AnonymousUser(인증받지 못한 유저)
        ip=self.request.META['REMOTE_ADDR']
        serializer.save(ip=ip, author=author)
    
    @action(detail = False, methods=['GET'])
    def public(self, request):
        qs = self.get_queryset().filter(is_public=True)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)
    
    @action(detail = True, methods=['PATCH'])
    def set_public(self, request, pk):
        instance = self.get_object()
        instance.is_public = True
        # is_public만 업데이트가 된다.
        instance.save(update_fields=['is_public'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    # def dispatch(self, request, *args, **kwargs):
    #     print("request body : ", request.body) # 실제 Product라면 Logger를 사용한다. dont use print
    #     print("request POST : ", request.POST)
    #     return super().dispatch(request, *args, **kwargs)
    
# 공개여부에대해서 직렬화가 다르다면 적용시킬수있다.
# class PublicPostListAPIView(generics.ListAPIView):
#     queryset = Post.objects.filter(is_public=True)
#     serializer_class = PostSerializer

# class PublicPostListAPIView(APIView):
#     def get(self, request, format=None):
#         qs = Post.objects.filter(is_public=True)
#         serializer = PostSerializer(qs, many=True)
#         return Response(serializer.data)
    
# public_post_list = PublicPostListAPIView.as_view()

# # 함수기반뷰
# @api_view(['GET'])
# def public_post_list(request):
#     qs = Post.objects.filter(is_public=True)
#     serializer = PostSerializer(qs, many=True)
#     return Response(serializer.data)

class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'instagram/post_detail.html'
    def get(self, request, *args, **kwargs):
        post = self.get_object()
        
        return Response({
            'post' : post,
        })
    
    