from django.apps import AppConfig
from django.contrib.auth.models import Group, Permission
from django.db.utils import OperationalError


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MyApp'

    def ready(self):
        try:
            self.create_user_management_group()
        except OperationalError:
            pass

    def create_user_management_group(self):
        group_name = "UserManagement"
        group, created = Group.objects.get_or_create(name=group_name)

        if created:
            user_permissions = Permission.objects.filter(content_type__model='user')
            group.permissions.set(user_permissions)
            print(f"Группа '{group_name}' успешно создана.")
        else:
            print(f"Группа '{group_name}' уже существует.")
