from rest_framework.exceptions import PermissionDenied,NotAuthenticated
class CustomPermissionMixin:
    def check_perms(self,request):
        method =request.method.upper()
        user = request.user
        obj = None
        is_owner=False
        try:
            obj =self.get_object()
        except Exception as e:
            print(e,'метод get_obj не определен у класса')
        if obj.onwer == request.user:
            is_owner = True
        if not user.is_authenticated:
            raise NotAuthenticated('Пожалуйста, войдите в систему')
        if method == 'GET':
            if user.role.can_view_all:
                return True
            elif user.role.can_view and is_owner:
                return True
        elif method in ('PUT', 'PATCH', 'POST'):
            if user.role.can_edit_all:
                return True
            elif user.role.can_edit and is_owner:
                return True
        if method =="DELETE":
            if user.role.can_delete_all:
                return True
            elif user.role.can_delete and is_owner:
                return True

        raise PermissionDenied('не достаточно прав')
