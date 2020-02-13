from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import User, GameMode
from api.serializers import UserSerializer, ScoreboardSerializer, GameModeSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    http_method_names = ['post']

class ScoreboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        game_mode = GameModeSerializer(request.query_params)
        scoreboard = GameMode.objects.get(**game_mode.data).record_set.order_by('-score')
        serializer = ScoreboardSerializer(scoreboard, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        response = ScoreboardSerializer().create(request.data, request.user)
        return Response(data=response, status=201)
        