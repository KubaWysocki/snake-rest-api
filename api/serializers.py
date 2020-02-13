from rest_framework.serializers import ModelSerializer, CharField

from api.models import User, Record, GameMode


class UserSerializer(ModelSerializer):
    password = CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class GameModeSerializer(ModelSerializer):
    class Meta:
        model = GameMode
        fields = ('board_size', 'speed', 'acceleration', 'border')

class ScoreboardSerializer(ModelSerializer):
    user = CharField()

    class Meta:
        model = Record
        fields = ('user', 'score')

    def create(self, validated_data, user):
        score = validated_data.pop('score')
        game_mode = GameMode.objects.filter(**validated_data)
        if len(game_mode) == 0:
            new_game_mode = GameModeSerializer(data=validated_data)
            if new_game_mode.is_valid():
                game_mode = GameMode.objects.create(**new_game_mode.data)

        record = game_mode.first().record_set.filter(user=user)
        if len(record) == 0:
            record = Record.objects.create(
                score=score,
                game_mode=game_mode.first(),
                user=user
            )
            return 'First personal highscore in this game mode!'
        elif record.first().score < score:
            record.update(
                score=score,
            )
            return 'New personal highscore in this game mode!!!'

        return 'Try again!'
