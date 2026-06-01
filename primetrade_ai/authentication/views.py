
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import status
from CoreUtils.Logger import Logger

from authentication.utils.Authentication_handler import Authentication_handler


createLog = Logger()



@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):

    user_data = request.data

    try:
        signup_handler = Authentication_handler(user_data)
        is_created_response = signup_handler.create_account();

        is_created = is_created_response.keys()


        if "created" in is_created:
            return Response(
                    {'code':'created'},
                    status=status.HTTP_201_CREATED
                    )

        if "user_exist" in is_created:
            return Response(
                    {'code': f'{is_created_response["user_exist"]}'},
                    status=status.HTTP_409_CONFLICT
                    )
        if "error" in is_created:
            return Response(
                    {'code': 'soemthing went wrong'}, 
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                    )

    except Exception as e:
        createLog.Log_Error('Authentication_View_Signup_Exception', e)
        return Response(
                {'code': f'{e}'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def auto_auth(request):
    return Response(
            {'code': 'authenticated'},
            status=status.HTTP_200_OK
            )





@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    return Response({
        'username': request.user.username,
        'is_staff': request.user.is_staff
    })



