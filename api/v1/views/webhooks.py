from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes)


@api_view(['POST', 'get'])
@permission_classes([AllowAny])
@authentication_classes([])
def block_io_webhook(request):
    if request.method == 'POST':
        print('data', request.data)
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})
