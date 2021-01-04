from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from memo_app.models import Note
from memo_app.api.serializers import NoteSerializer
from django.contrib.auth.models import User


@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def api_list_note_view(request):
    user = request.user
    try:
        notes = Note.objects.filter(author=user)
    except Note.DoesNoteExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    print('notes', notes)
    if not notes:
        return Response({'response': {}})

    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
def api_detail_note_view(request, slug):

    try:
        note = Note.objects.get(id=slug)
    except Note.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    print(note)
    user = request.user
    if note.author != user:
        return Response({'response': " You don't have the right to view this memo. "})

    if request.method == 'GET':
        serializer = NoteSerializer(note)
        return Response(serializer.data)


@api_view(['PUT', ])
@permission_classes((IsAuthenticated,))
def api_update_note_view(request, slug):

    try:
        note = Note.objects.get(id=slug)
    except Note.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if note.author != user:
        return Response({'response': "You don't have permission to update this memo."})

    if request.method == 'PUT':
        serializer = NoteSerializer(note, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'Update successful'
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', ])
@permission_classes((IsAuthenticated,))
def api_delete_note_view(request, slug):

    try:
        note = Note.objects.get(id=slug)
    except Note.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if note.author != user:
        return Response({'response': "You don't have permission to delete this memo"})

    if request.method == 'DELETE':
        operation = note.delete()
        data = {}
        if operation:
            data['success'] = 'Successfully deleted'
        else:
            data['failure'] = 'Delete failed'
        return Response(data=data)


@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def api_create_note_view(request):

    account = request.user

    note = Note(author=account)

    if request.method == 'POST':
        serializer = NoteSerializer(note, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





    # notes = Note.objects.all()
    # serializered = NoteSerializer(notes, many=True)
    # return Response(serializered.data)

#
# class NoteList(APIView):
#     def get(self, request):
#         notes = Note.objects.all()
#         serializered = NoteSerializer(notes, many=True)
#         return Response(serializered.data)
#
#     def create(self):
#         pass
#
#     def update(self):
#         pass
#
#     def delete(self, request):
#         pass
