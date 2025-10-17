from src.bases.base_viewset import *


class GetMe(APIView):
    def get(self, request):
        user = self.request.user
        data = serializer.UserSerializer(user).data
        return Response(data)
