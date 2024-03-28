from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.models import User
from ..serializers import UserSerializer

@api_view(['GET'])
def get_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)