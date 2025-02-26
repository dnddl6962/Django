from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (
            "Profile",  # 기본 정보
            {
                "fields": (
                    "profile_photo",
                    "username",
                    "password",
                    "name",
                    "email",
                    "is_host",
                    "gender",
                    "language",
                    "currency",
                ),  # 이 그룹에 포함될 필드
                # 'description' : '유저 정보를 입력해주세요.'
                "classes": ("wide",),
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            "Important Dates",
            {
                "fields": (
                    "last_login",
                    "date_joined",
                ),
                "classes": ("collapse",),
            },
        ),
    )
    # fields = ('email', 'password', 'name')
    list_display = (
        "username",
        "email",
        "name",
        "is_host",
    )  # list_display : 사용자 list를 표시할 떄 보이는 column을 설정하는 Tuple
