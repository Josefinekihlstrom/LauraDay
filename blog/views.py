from django.views import generic
from .models import Post
from .forms import BlogForm
from django.urls import reverse_lazy


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
