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

class GameModeViewSet(ModelViewSet):
    queryset = GameMode.objects.all()
    serializer_class = GameModeSerializer

    http_method_names = ['get']

class ScoreboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        game_mode = request.query_params.get('id', False)
        if game_mode:
            scoreboard = GameMode.objects.get(pk=game_mode)
        else:
            game_mode = GameModeSerializer(request.query_params).data
            scoreboard = GameMode.objects.get(**game_mode)
        serializer = ScoreboardSerializer(scoreboard.record_set.order_by('-score'), many=True)
        return Response(data=serializer.data, status=200)

    def post(self, request):
        response = ScoreboardSerializer().create(request.data, request.user)
        return Response(data=response, status=201)
        