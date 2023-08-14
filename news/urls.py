from django.urls import path
from .views import PostList, PostDetail, PostSearch, PostCreate, PostDelete, PostUpdate


urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    path('search/', PostSearch.as_view()),
    path('create/', PostCreate.as_view()),
    path('<int:pk>/delete/', PostDelete.as_view()),
    path('<int:pk>/update/', PostUpdate.as_view())
]
