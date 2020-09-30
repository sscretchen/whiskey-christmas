from django.contrib import admin
from .models import Post, Category, Tag, Comment


class AdminPost(admin.ModelAdmin):
    # Add any field from the 'Post' model to list_filter to be displayed on the admin page
    list_filter = ['timestamp',]
    list_display = ['title', 'timestamp', ]
    search_fields = ['title', 'content', ]

    class Meta:
        model = Post

class AdminComment(admin.ModelAdmin):
    list_filter = ('publishing_date', )
    search_fields = ('name', 'content', 'post__title')

    class Meta:
        model = Comment

admin.site.register(Post, AdminPost)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment,  AdminComment)
