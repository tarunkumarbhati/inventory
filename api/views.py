from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.http import Http404

from .models import Box
from .helpers import get_box_queryset
from .serializers import BoxSerializer

class BoxView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk=None):
        boxes = get_box_queryset(request.GET)
        serializer = BoxSerializer(boxes, many=True, context={'request': request})
        return Response({"boxes": serializer.data})

    def post(self, request, pk=None):
        if not request.user.is_staff:
            raise PermissionDenied("User is not staff user!")
        box = request.data
        serializer = BoxSerializer(data=box, context={'request': request})
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            box_saved = serializer.save()
        return Response({"success": "Box created successfully", "id":box_saved.id})

    def put(self, request, pk=None):
        if not pk:
            raise Http404("Please provide ID of box!")
        saved_box = get_object_or_404(Box.objects.all(), pk=pk)
        data = request.data.get('box')
        serializer = BoxSerializer(instance=saved_box, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Box with id '{}' updated successfully".format(saved_box.id)})

    def delete(self, request, pk=None):
        if not pk:
            raise Http404("Please provide ID of box!")
        box = get_object_or_404(Box.objects.all(), pk=pk)
        if box.creator != request.user:
            raise PermissionDenied("Only creator of the box can delete it!")
        box.delete()
        return Response({"message": "Box with id `{}` has been deleted.".format(pk)}, status=204)

class MyBoxView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk=None):
        if not request.user.is_staff:
            raise PermissionDenied("User is not staff user!")
        boxes = get_box_queryset(request.GET, creator=request.user)
        serializer = BoxSerializer(boxes, many=True, context={'request': request})
        return Response({"boxes": serializer.data})