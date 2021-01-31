# from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView  # импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД
from .models import Post
from datetime import datetime
from .filters import PostFilter
from .forms import PostForm # импортируем нашу форму
from django.core.paginator import Paginator


class PostList(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'news.html'  # указываем имя шаблона, в котором будет лежать html,
    # в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'news'  # это имя списка, в котором будут лежать все объекты,
    # его надо указать, чтобы обратиться к самому списку объектов через html-шаблон
    queryset = Post.objects.order_by('-id')
    form_class = PostForm  # добавляем форм класс, чтобы получать доступ к форме через метод POST
    #paginate_by = 1


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        context['value1'] = None  # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу
        # другого фильтра
        return context

# создаём представление в котором будет детали конкретного отдельного товара
class PostDetail(DetailView):
    model = Post # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'post.html' # название шаблона будет post.html
    context_object_name = 'post' # название объекта. в нём будет

class Search(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'search'
    ordering = ['-time_in']
    paginate_by = 1  # поставим постраничный вывод в один элемент

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод
        # get_context_data у наследуемого класса (привет полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр
        # в контекст
        return context

class PostCreateView(CreateView):
    template_name = 'add.html'
    form_class = PostForm

# дженерик для редактирования объекта
class PostEditView(UpdateView):
    template_name = 'edit.html'
    form_class = PostForm

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте
    # который мы собираемся редактировать
    def get_object(self, **kwargs):
        id_1 = self.kwargs.get('pk')
        return Post.objects.get(id=id_1)


# дженерик для удаления товара
class PostDeleteView(DeleteView):
    template_name = 'delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'