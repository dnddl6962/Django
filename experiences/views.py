from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, PermissionDenied, ParseError
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.status import HTTP_204_NO_CONTENT
from .serializers import (
    ExperienceSerializer,
    ExperienceDetailSerializer,
    PerkSerializer,
)
from .models import Experience, Perk
from categories.models import Category


class Experiences(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        experiences = Experience.objects.all()
        serializer = ExperienceSerializer(
            experiences,
            many=True,
            context={"request": request},
        )
        # print(serializer)
        return Response(serializer.data)

    def post(self, request):
        serializer = ExperienceDetailSerializer(data=request.data)
        if serializer.is_valid():
            new_experience = serializer.save()
            serializer = ExperienceDetailSerializer(new_experience)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class ExperienceDetail(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            experience = Experience.objects.get(pk=pk)
            return experience
        except Experience.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        experience = self.get_object(pk)
        serializer = ExperienceDetailSerializer(
            experience, context={"request": request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        experience = self.get_object(pk)
        if experience.host != request.user:
            raise PermissionDenied

        serializer = ExperienceDetailSerializer(
            experience,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():
            category_id = request.data.get("category")
            if not category_id:
                raise ParseError("Category is required")
            try:
                category = Category.objects.get(pk=category_id)
            except Category.DoesNotExist:
                raise ParseError("Category not found")
            experience.category = category
            experience.save()
            serializer = ExperienceDetailSerializer(
                experience,
                context={"request": request},
            )
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        experience = self.get_object(pk)
        if experience.host != request.user:
            raise PermissionDenied
        experience.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class Perks(APIView):

    def get(self, request):
        perks = Perk.objects.all()
        serializer = PerkSerializer(perks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PerkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class PerkDetail(APIView):

    def get_object(self, pk):
        try:
            return Perk.objects.get(pk=pk)
        except Perk.DoesNotExist:
            raise NotFound()

    def get(self, request, pk):
        perk = self.get_object(pk)
        serializer = PerkSerializer(perk)
        return Response(serializer.data)

    def put(self, request, pk):
        perk = self.get_object(pk)
        serializer = PerkSerializer(
            perk,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        perk = self.get_object(pk)
        perk.delete()
        return Response()
