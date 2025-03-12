from django.urls import path
from . import views


urlpatterns = [
    path(
        "",
        views.CategoryViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    ),
    path(
        "<int:pk>",  # ViewSet은 pk를 받기로 약속되어있다.
        views.CategoryViewSet.as_view(
            {
                "get": "retrieve",
                "put": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
]


# urlpatterns = [
#     path(
#         "", views.Categories.as_view()
#     ),  # class를 가져오려면 as_view()를 호출해야함 -> Just Rule!
#     path(
#         "<int:pk>",
#         views.CategoryDetail.as_view(),
#     ),
# ]
