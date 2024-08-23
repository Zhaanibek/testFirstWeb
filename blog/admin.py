from django.contrib import admin

from blog.models import CategoryBlog, Post

@admin.register(CategoryBlog)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name",]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ["title", "author", "created_at"]
    search_fields = ["title", "description", "author"]
    list_filter = ["title", "category", "author"]
    fields = [
        "title",
        "category",
        "slug",
        "description",
        "image",
        "author",
    ]

