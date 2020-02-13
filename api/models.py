from django.db.models import Model, CharField, IntegerField, BooleanField, ForeignKey, CASCADE
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserAccountManager


class User(AbstractBaseUser, PermissionsMixin):
    username = CharField(unique=True, max_length=14)
    is_staff = BooleanField(default=False)
    is_superuser = BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'username'

class GameMode(Model):
    board_size = CharField(
        max_length=5,
        choices=[
            ('20x15', 'small'),
            ('30x23', 'medium'),
            ('40x30', 'large')
        ]
    )
    speed = IntegerField(
        choices=[
            (80, 'slow'),
            (160, 'medium'),
            (240, 'fast')
        ]
    )
    acceleration = BooleanField()
    border = BooleanField()

    class Meta:
        unique_together = ('board_size', 'speed', 'acceleration', 'border')

    def __str__(self):
        return self.board_size + "_b" + str(int(self.border)) + "_a" + str(int(self.acceleration)) + "_" + str(self.speed)

class Record(Model):
    user = ForeignKey(User, CASCADE)
    game_mode = ForeignKey(GameMode, CASCADE)
    score = IntegerField()

    class Meta:
        unique_together = ('user', 'game_mode')

    def __str__(self):
        return self.user.username + " " + str(self.score) + " " + self.game_mode.__str__()
