from django.views.generic import ListView, DetailView

from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-creation_date']
    paginate_by = 10

    def get_context_data(self, **kwards):
        context = super(PostListView, self).get_context_data(**kwards)
        context['title'] = 'Главная страница блога'
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwards):
        context = super(PostDetailView, self).get_context_data(**kwards)
        context['title'] = Post.objects.filter(pk=self.kwargs['pk']).first()
        return context


class TagSearch(ListView):

    slug_url_kwarg = 'slug'
    template_name = 'blog/index.html'
    ordering = ['-creation_date']
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        slug = self.kwargs.get(self.slug_url_kwarg)
        queryset = Post.objects.filter(tags__name=slug)
        return queryset
