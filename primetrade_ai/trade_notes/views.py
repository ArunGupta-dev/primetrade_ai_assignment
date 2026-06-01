from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import status
from CoreUtils.Logger import Logger

from trade_notes.utils.Trade_notes_handler import Trading_notes_handler

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from trade_notes.models import trade_notes
from trade_notes.utils.serializer import trade_notes_serializer
from rest_framework import viewsets, permissions


createLog = Logger()



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_note(request):

    data = request.data
    try:

        handler = Trading_notes_handler(request.user)
        is_created = handler.create_note(data)

        if is_created == 'created':
            return Response(
                    {'code': 'created'}, 
                    status=status.HTTP_201_CREATED
                    )
        if is_created == 'not-created':
            return Response(
                    {'code': 'not-created'},
                    status=status.HTTP_400_BAD_REQUEST
                    )
        else:
            return Response(
                    {'code': 'db-error'},
                    status=status.HTTP_404_NOT_FOUND
                    )

    except Exception as e:
        createLog.Log_Error('trade_notes_views_create_note_Exception', e)
        return Response(
                {'code': 'Something went wrong'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )



@api_view(['PATCH'])
def update_note(request):

    data = request.data

    try:
        handler = Trading_notes_handler(request.user)

        is_updated = handler.update_note(data)

        if is_updated == 'updated':
            return Response(
                    {'code': 'updated'}, 
                    status= status.HTTP_200_OK
                    )

        elif is_updated == 'no-permission':
            return Response(
                    {'code': 'not-authorized'},
                    status=status.HTTP_403_FORBIDDEN
                    )

        elif is_updated == 'not-updated':
            return Response(
                    {'code': 'not-updated'},
                    status=status.HTTP_400_BAD_REQUEST
                    )
        else:
            return Response(
                    {'code': 'db-error'},
                    status=status.HTTP_400_BAD_REQUEST
                    )

    except Exception as e:
        return Response(
                {'code': 'Something went worng'},
                status= status.HTTP_500_INTERNAL_SERVER_ERROR
                )




@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_note(request):

    data = request.data

    try:
        handler = Trading_notes_handler(request.user)

        is_deleted = handler.delete_note(data)

        if is_deleted == 'deleted':
            return Response(
                    {'code': 'deleted'},
                    status=status.HTTP_204_NO_CONTENT
                    )
        elif is_deleted == 'no-permission':
            return Response(
                    {'code': 'not-authorized'},
                    status=status.HTTP_403_FORBIDDEN
                    )
        else:
            return Response(
                    {'code': 'db-error'},
                    status=status.HTTP_400_BAD_REQUEST
                    )
    except Exception as e:
        createLog.Log_Error('Trade_Note_Views_delete_note_Exception', e)
        return Response(
                {'code': 'Something went wrong'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )






class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.author== request.user


class TradeNoteViewSet(viewsets.ModelViewSet):
    serializer_class = trade_notes_serializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def get_queryset(self):
        if self.request.user.is_staff:
            return trade_notes.objects.all()
        return trade_notes.objects.filter(author=self.request.user)

