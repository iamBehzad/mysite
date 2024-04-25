from django.contrib import admin
from blog.models import Post, Category, Comments
from django_summernote.admin import SummernoteModelAdmin
from .models import Post
# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    date_hierarchy='created_date'
    empty_value_display = "-empty-"
    #fields=('title', )
    #exclude('created_date')
    list_display=('title', 'author', 'counted_view', 'status', 'published_date', 'created_date')
    list_filter=('status', 'author')
    #prepopulated_fields
    #ordering=['-created_date']
    search_fields=('title','content',)
    summernote_fields = ('content',)
    
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy='created_date'
    empty_value_display = "-empty-"
    list_display=('name','post','approved', 'created_date')
    list_filter=('post', 'approved')
    search_fields=('name','post',)
    
admin.site.register(Comments,CommentAdmin)
admin.site.register(Category)
admin.site.register(Post,PostAdmin)