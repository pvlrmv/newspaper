from django_filters import FilterSet
from .models import Post


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'time_in': ['gt'],
            # мы хотим чтобы нам выводило имя хотя бы отдалённо похожее на то что запросил пользователь
            'post_name': ['gt'],  # количество товаров должно быть больше или равно тому, что указал пользователь
            'author': ['lt'],  # цена должна быть меньше или равна тому, что указал пользователь
        }

