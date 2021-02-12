from django.forms import ModelForm, BooleanField  # Импортируем true-false поле
from .models import Post


class PostForm(ModelForm):
    check_box = BooleanField(label='статья или новость')  # добавляем галочку, или же true-false поле

    class Meta:
        model = Post
        fields = ['author', 'categories', 'post_name', 'text', 'post_rating', 'check_box' ]
        # не забываем включить галочку в поля иначе она не будет показываться на странице!