from rest_framework import permissions


'''Класс доступов для отображение записи всем желающим, 
а функция удаление только для авторизированных пользователей/администратора.'''


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)


'''Класс доступов для отображение записи всем желающим, 
а функция редактирования только для пользователя !АВТОРА.'''


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
        # Если пользователь с базы данных (obj.user) == (request.user) пользователю от которого пришел запрос,
        # то дать доступ на редактирование записи


# https://www.youtube.com/watch?v=b4C6UTlSC-o&list=PLA0M1Bcd0w8xZA3Kl1fYmOH_MfLpiYMRs&index=14