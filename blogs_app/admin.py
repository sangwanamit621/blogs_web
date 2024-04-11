from django.contrib import admin
from .models import Post,Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ["post_id","title","author"]
    search_fields = ["title","author"]
    autocomplete_fields = ["author"]
    list_filter = ["author","title"]


class CommentAdmin(admin.ModelAdmin):
    list_display = ["comment_id","post_id","user_id"]
    search_fields = ["comment","user_id","post_id"]
    autocomplete_fields = ["user_id"]


admin.site.register(Post,admin_class=PostAdmin)
admin.site.register(Comment,admin_class=CommentAdmin)


