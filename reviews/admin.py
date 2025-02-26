from django.contrib import admin
from .models import Review


class WordFilter(admin.SimpleListFilter):

    title = "Filter by Words"

    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("great", "Great"),
            ("awesome", "Awesome"),
        ]

    def queryset(self, request, reviews):
        word = self.value()
        if word:  # word가 None이 아닌 경우에만 필터 적용
            return reviews.filter(payload__icontains=word)
        return reviews  # word가 None인 경우 원본 QuerySet 반환


class BadorGood(admin.SimpleListFilter):

    title = "BadorGood"

    parameter_name = "rate"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("bad", "Bad"),
        ]

    def queryset(self, request, reviews):
        rate = self.value()
        if rate == "good":
            return reviews.filter(rating__gte=3)
        elif rate == "bad":
            return reviews.filter(rating__lt=3)
        return reviews  # word가 None인 경우 원본 QuerySet 반환


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "rating",
    )

    list_filter = (
        WordFilter,
        BadorGood,
    )
