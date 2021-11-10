import jwt

from functools        import wraps
from django.http      import JsonResponse
from django.conf      import settings

from users.models     import User

def login_decorator(func):
    @wraps(func)
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token = request.headers.get("Authorization", None)
            payload      = jwt.decode(access_token, settings.SECRET_KEY, settings.ALGORITHM)
            request.user = User.objects.get(id=payload['user_id'])

        except jwt.exceptions.DecodeError:
            return JsonResponse({'message' : 'INVALID_TOKEN' }, status=400)

        except User.DoesNotExist:
            return JsonResponse({'message' : 'INVALID_USER'}, status=400)

        return func(self, request, *args, **kwargs)

    return wrapper