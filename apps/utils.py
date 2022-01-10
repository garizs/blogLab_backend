from apps.users.serializers import UsersSerializers


def my_jwt_response_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UsersSerializers(user, context={'request': request}).data
    }