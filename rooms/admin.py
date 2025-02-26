from django.contrib import admin
from .models import Room, Amenity


@admin.action(description="Set All Prices to Zero")
def reset_prices(model_admin, request, rooms):
    for room in rooms:
        room.price = 0
        room.save()


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    actions = (reset_prices,)

    list_display = (
        "name",
        "price",
        "kind",
        "total_amenities",
        "rating",
        "owner",
        "category",
    )
    list_filter = (
        "country",
        "city",
        "price",
        "pet_friendly",
        "kind",
        "amenities",
    )

    search_fields = ("owner__username",)

    def total_amenities(self, room):
        return room.amenities.count()

    def rating(self, room):
        count = room.reviews.count()
        if count == 0:
            return f"No Reviews"
        else:
            total = 0
            for review in room.reviews.all().values("rating"):
                total += review["rating"]

            rating_avg = total / count

            return round(rating_avg, 1)


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_at",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
