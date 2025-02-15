from django.contrib import admin

# Register your models here.
from blog.models import Posts, Authors
admin.site.register(Posts)
admin.site.register(Authors)