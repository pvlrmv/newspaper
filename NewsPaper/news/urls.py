from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import PostList, PostDetail, Search, PostEditView, PostDeleteView, PostCreateView # импортируем наше представление
 
 
urlpatterns = [

    # path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно почему
    path('', PostList.as_view()), # т.к. сам по себе это класс, то нам надо представить этот класс в виде view.
    # Для этого вызываем метод as_view
    path('<int:pk>', PostDetail.as_view(), name = 'post_detail'),  # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    path('search', Search.as_view()),
    path('/news/add/', PostCreateView.as_view(), name='post_add'),
    path('<int:pk>/edit/', PostEditView.as_view(), name='post_edit'),
    path('/news/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),


]