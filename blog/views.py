from django.views import generic
from .models import Post, Comment
from .forms import BlogForm, AddCommentForm
from django.urls import reverse_lazy


# Blog application built with help from the following links:
# https://djangocentral.com/building-a-blog-application-with-django/
# https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi&index=1
class PostList(generic.ListView):
    # Only posts with status published will show
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


# Add Blog Post code with help from Codemy.com
# https://www.youtube.com/watch?v=m3efqF9abyg&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi&index=4
class AddPost(generic.CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'


# Add comment code with help from Codemy.com
# https://www.youtube.com/watch?v=OuOB9ADT_bo&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi&index=35
class AddComment(generic.CreateView):
    model = Comment
    form_class = AddCommentForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        slug = self.kwargs['slug']
        form.instance.post = Post.objects.get(slug=slug)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'slug': self.kwargs['slug']})


# Edit Blog Post code with help from Codemy.com
# https://www.youtube.com/watch?v=J7xaESAddDQ&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi&index=6
class EditPost(generic.UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ['title', 'slug', 'content']


# Delete Blog Post with help from Codemy.com
# https://www.youtube.com/watch?v=8NPOwmtupiI&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi&index=7
class DeletePost(generic.DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blog')
