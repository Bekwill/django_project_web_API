from rest_framework.views import APIView
from .serializers import NoteSerializer
from rest_framework import response,status
from rest_framework.permissions import IsAuthenticated
from .models import Note
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
class NoteCollectionView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NoteSerializer
    def get(self, request):
        """list"""

        notes = request.user.notes.all()
        serializer = self.serializer_class(instance=notes, many=True)
        return response(data=serializer.data)

    def post(self, request):
        """Create"""

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(user=request.user)
        return response(data = serializer.data)

class NoteSingletoView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NoteSerializer
    def get(self,request, pk):
        """Detail"""
        note = get_object_or_404(Note, pk=pk)
        serializer = self.serializer_class(instance=note)
        return response(data=serializer.data)

    def patch(self, request, pk):
        """update"""
        note = get_object_or_404(Note, pk=pk)
        serializer = self.serializer_class(data=request.data, instance=note, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response(data=serializer.data)
    def delete(self, request, pk):
        """delete"""
        note = get_object_or_404(Note, pk=pk)
        note.delete()
        return response(status=status.HTTP_204_NO_CONTENT)



class NoteListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NoteSerializer
    def get_queryset(self):
        notes = self.request.user.notes.all()
        return notes
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class NoteRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NoteSerializer
    def get_queryset(self):
        notes = self.request.user.notes.all()
        return notes


class NoteViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = NoteSerializer
    def get_queryset(self):
        notes = self.request.user.notes.all()
        return notes
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
