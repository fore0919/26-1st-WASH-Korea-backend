import json, bcrypt, jwt 

from django.http    import JsonResponse
from django.views   import View

from django.conf    import settings

from .models        import User
from .utils         import validate_email, validate_password

class SignupView(View):
    def post(self, request):
        try :
            data = json.loads(request.body)
            user_name = data['user_name']
            password  = data['password']
            name      = data['name']
            nickname  = data['nickname']
            email     = data['email']
            contact   = data['contact']
            address   = data['address']

            if not validate_email(email) :
                return JsonResponse({'message':'EMAIL_VALIDATION_ERROR'}, status=400)
            if not validate_password(password):
                return JsonResponse({'message':'PW_VALIDATION_ERROR'}, status=400)
            if User.objects.filter(email=email).exists():
                return JsonResponse({'message':'ALREADY_EXISTS_EMAIL'}, status=409)
            if User.objects.filter(user_name=user_name).exists():
                return JsonResponse({'message':'ALREADY_EXISTS_USERNAME'}, status=409)

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            User.objects.create(
                user_name = user_name,
                password  = hashed_password,
                name      = name,
                nickname  = nickname,
                email     = email,
                contact   = contact,
                address   = address,
            )
            return JsonResponse({'message':'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)

class LoginView(View):
    def post(self, request):        
        try : 
            data = json.loads(request.body)
            user_name = data['user_name']
            password  = data['password']
            user      = User.objects.get(user_name=user_name)

            if not bcrypt.checkpw(password.encode("utf-8"), user.password.encode('utf-8')):
                return JsonResponse({'message':'INVALID_USER'}, status=401)

            access_token = jwt.encode({'id':user.id},settings.SECRET_KEY, algorithm = settings.ALGORITHM)

            return JsonResponse({'message':'SUCCESS', 'ACCESS_TOKEN': access_token}, status=200)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)

        except User.DoesNotExist:
            return JsonResponse({'message':'USER_DOES_NOT_EXISTS'}, status=401)

        except json.decoder.JSONDecodeError:
            return JsonResponse({'message': 'JSON_DECODE_ERROR'}, status=400)