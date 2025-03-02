from django.contrib import admin
from django.contrib.auth.hashers import make_password
from .models import Users
from .models import Comment

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ("user_name", "user_email", "user_registration_date")
    readonly_fields = ("user_code",)  # Görünecek ama düzenlenemeyecek

    def save_model(self, request, obj, form, change):
        if obj.user_password:  # Eğer bir şifre girilmişse hashle
            obj.user_password = make_password(obj.user_password)
        super().save_model(request, obj, form, change)


admin.site.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_code', 'comment_text')
    search_fields = ('user_code__user_code', 'comment_text')
    list_filter = ('user_code',)
    
