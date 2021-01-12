from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):

    rating = models.FloatField(default=0.0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def update_rating(self, rating):
        pass


class Category(models.Model):
    category_name = models.CharField(max_length=255, unique = True)

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    choise = models.BooleanField(default=False)# выбор статья или новость
    time_in = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, through='PostCategory')
    post_name = models.CharField(max_length = 255)
    text = models.CharField(max_length = 255)
    post_rating = models.FloatField(default=0.0)
    def like(self):
        rating = self.post_rating
        rating = rating+1
        return rating

    def dislike(self):
        rating = self.post_rating
        rating = rating - 1
        return rating

    def preview(self):
        return self.text + '...'





class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    text_comment = models.CharField(max_length = 255)
    time_comment = models.DateTimeField(auto_now_add=True)
    rating_comment = models.FloatField(default=0.0)

    def like(self):
        rating = self.rating_comment
        rating = rating+1
        return rating

    def dislike(self):
        rating = self.rating_comment
        rating = rating - 1
        return rating


