from django.shortcuts import render

# Create your views here.
from blog.models import Posts
def show_posts(request):
    result = Posts.objects.all()
    context = {"posts_list": result}
    return render(request, template_name = "blog/post_list.html", context=context)