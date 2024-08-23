from django.contrib import admin
from goods.models import CategoryRental, CategorySpare, CategoryRental, ProductCarRental, ProductSpare

@admin.register(CategoryRental)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name",]


@admin.register(CategorySpare)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name",]


@admin.register(ProductCarRental)
class ProductCarRentalAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "quantity", "price", "in_stock"]
    list_editable = ["in_stock"]
    search_fields = ["name", "description"]
    list_filter = ["quantity", "category", "in_stock"]
    fields = [
        "name",
        "category",
        "slug",
        "description",
        "image",
        "price",
        "quantity",
        "in_stock",
    ]

@admin.register(ProductSpare)
class ProductSpareAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "quantity", "price"]
    search_fields = ["name", "description"]
    list_filter = ["quantity", "category"]
    fields = [
        "name",
        "category",
        "slug",
        "description",
        "image",
        "price",
        "quantity",
    ]
