from django.contrib import admin
from .models import Post



class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','auther','publish','status')
    list_filter = ('status','created','auther','publish')
    search_fields = ('title','body')
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ('auther',)
    date_hierarchy = 'publish'
    ordering = ['status','publish']
admin.site.register(Post,PostAdmin)
# Register your models here.
