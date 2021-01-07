from django.contrib import admin

# Register your models here.
from blogging.models import Post, Category


class CategoryInline(admin.TabularInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline,]


class CategoryAdmin(admin.ModelAdmin):
    inlines = [CategoryInline,]
    exclude = ('posts',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
