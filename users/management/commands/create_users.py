from django.core.management import BaseCommand


from users.models import Role,User

class Command(BaseCommand):

    def handle(self, *args, **options):
        admin_role = Role.objects.create(
            name="ADMIN",
            can_edit=True,
            can_delete=True,
            can_view=True,
            can_edit_all=True,
            can_view_all=True,
            can_delete_all=True,
        )
        moderator_role = Role.objects.create(
            name="MODERATOR",
            can_edit=True,
            can_delete=True,
            can_view=True,
            can_edit_all=True,
            can_view_all=True,
            can_delete_all=True,
        )

        user_role = Role.objects.create(
            name="USER",
            can_edit=False,
            can_delete=False,
            can_view=True,
            can_edit_all=False,
            can_view_all=False,
            can_delete_all=False,
        )

        admin = User.objects.create(
            first_name ="Admin",
            last_name = 'Adminov',
            middle_name ='Adminovich',
            is_staff =True,
            is_super_user=True,
            role = admin_role
        )
        admin.set_password('qwerty123')
        admin.save()

        moderator = User.objects.create(
            first_name="Moderator",
            last_name="Moderatov",
            middle_name="Moderatorovich",
            is_staff=True,
            is_superuser=False,
            role=moderator_role
        )
        moderator.set_password('parol')
        moderator.save()

        user = User.objects.create(
            first_name="User",
            last_name="Userov",
            middle_name="Userovich",
            is_staff=False,
            is_superuser=False,
            role=user_role
        )
        user.set_password('adminlol')
        user.save()