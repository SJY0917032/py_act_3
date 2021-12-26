from django.shortcuts import render
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