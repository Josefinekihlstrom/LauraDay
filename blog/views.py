from django.views import generic
from .models import Post
from .forms import BlogForm


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
