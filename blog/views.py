from django.shortcuts import render

# Create your views here.
from blog.models import Posts, Authors
def show_posts(request):
    result = Posts.objects.all()
    context = {"posts_list": result}
    return render(request, template_name = "blog/post_list.html", context=context)
def show_posts_by_author(request, author_id):
    result = Posts.objects.filter(author=author_id)
    context = {"posts_by_author_list": result}
    return render(request, template_name = "blog/post_by_author_list.html", context=context)