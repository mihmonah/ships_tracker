import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserAccountManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, password, **extra_fields):
        if not password:
            raise ValueError("Password must be provided")

        user = self.model(**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, password=None, **extra_fields):
        return self._create_user(password, **extra_fields)

    def create_superuser(self, password, **extra_fields):
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True

        return self._create_user(password, **extra_fields)


class ShipOwner(AbstractBaseUser, PermissionsMixin):
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'username'

    objects = UserAccountManager()

    token = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(blank=True, null=True, unique=True, max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def get_token(self):
        return self.token


# from django.contrib.auth.models import User
# from django.db import models
# import uuid
#
#
# class ShipOwner(User):
#     user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     is_superuser = False
#
#     class Meta:
#         permissions = (
#             ("can_see_only_ships_api", "Могут смотреть только API судов"),
#         )
