from django.views.generic import ListView, DetailView

from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 10

    def get_context_data(self, **kwards):
        context = super(PostListView, self).get_context_data(**kwards)
        context['title'] = 'Главная страница блога'
        return context
#

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwards):
        context = super(PostDetailView, self).get_context_data(**kwards)
        context['title'] = Post.objects.filter(pk=self.kwargs['pk']).first()
        return context