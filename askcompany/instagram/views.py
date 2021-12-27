from django.shortcuts import render
from rest_framework import generics, serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
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

    def dispatch(self, request, *args, **kwargs):
        print("request body : ", request.body) # 실제 Product라면 Logger를 사용한다. dont use print
        print("request POST : ", request.POST)
        return super().dispatch(request, *args, **kwargs)
    
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

# 함수기반뷰
@api_view(['GET'])
def public_post_list(request):
    qs = Post.objects.filter(is_public=True)
    serializer = PostSerializer(qs, many=True)
    return Response(serializer.data)