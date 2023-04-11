from django.contrib.auth import authenticate
from django.contrib.auth.models import User as admin_user
from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from .models import User,Notes
from rest_framework.decorators import api_view
import jwt
from .serializers import userSerializer,NoteSerializer
from rest_framework.generics import ListCreateAPIView
# Create your views here.


@api_view(['POST'])
def signUp(request):
    try:
        name = request.data['username']
        email = request.data['email']
        phone = request.data['phone']
        password = request.data['password']
    except:
        return Response({'status': 'Please Provide The Details(name,email,phone,muncipality,district,password)'})

    if len(name) < 3:
        return Response({'status': 'Name should be minimum of 3 letters'})
    if len(password) < 5:
        return Response({'status': 'Password should be minimum of 5'})
    check_user = User.objects.all()

    for i in check_user:
        if i.email == email:
            return Response({'status': 'Email is already Exist'})
        elif i.phone == phone:
            return Response({'status': 'Phone Number is already Exist'})
    user = User.objects.create(
        name=name,
        email=email,
        phone=phone,
        password=password,
    )
    user.save()
    return Response({'status': 'Success'})


@api_view(['POST'])
def user_login(request):
    try:
        email = request.data['email']
        password = request.data['password']
    except:
        return Response({'status': 'Please Provide details(email,password)'})
    user = User.objects.all()
    status = 'None'
    for i in user:
        if i.email == email:
            if i.password == password:
                payload = {
                    'email': email,
                    'password': password,
                    'username': i.name,
                    # 'image':i.image

                }

                jwt_token = jwt.encode(payload, 'secret', algorithm='HS256')
                print(jwt_token, 'token evide undddaa')
                response = Response(
                    {'status': 'Success', 'payload': payload, 'user_jwt': jwt_token})
                return response
            else:
                status = 'Wrong Password'
                break
        else:
            status = 'Email is not found'

    return Response({'status': status})


@api_view(['POST'])
def verify_token(request):
    status = 'None'
    token = request.data['token']
    decoded = jwt.decode(token, 'secret', algorithms='HS256')
    print(decoded, 'athiddaaa..')
    print(decoded.get('email'), 'Yes i am back...')
    user = User.objects.get(email=decoded.get('email'))
    if user:
        return Response({'username': user.name})
    else:
        return Response({'status': 'Token InValid'})


@api_view(['GET'])
def profile(request, id):
    user = User.objects.get(id=id)
    seializer = userSerializer(user, many=False)
    return Response(seializer.data)


@api_view(['GET'])
def user_list(request):
    user = User.objects.all()
    serializer = userSerializer(user, many=True)
    print(serializer.data)
    return Response(serializer.data)



def create_user(request):
    pass


@api_view(['GET'])
def edit_user(request, id):
    user = User.objects.get(id=id)
    serializer = userSerializer(user, many=False)
    print(serializer, 'evide undada')
    return Response(serializer.data)


@api_view(['PUT'])
def update_user(request, id):
    # print(request.data)
    user = User.objects.get(id=id)
    user.name = request.data['userName']
    user.email = request.data['email']
    user.save()
    return Response('User updated')


@api_view(['DELETE'])
def delete_user(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return Response('Deleted')


@api_view(['POST'])
def admin_login(request):
    try:
        email = request.data['email']
        password = str(request.data['password'])
    except:
        return Response({'status': 'Please Provide details(email,password)'})
    user = User.objects.all()

    status = 'None'
    for i in user:
        if i.is_superuser == True:
            if i.email == email:
                if i.password == password:
                    payload = {
                        'email': email,
                        'password': password,
                        # 'username': i.name,

                    }

                    jwt_token = jwt.encode(
                        payload, 'secret', algorithm='HS256') 
                    print(jwt_token, 'token evide undddaa')
                    response = Response(
                        {'status': 'Success', 'payload': payload, 'admin_jwt': jwt_token})
                    return response

                else:
                    status = 'Wrong Password'
                    break
            else:
                status = 'Email is not found'
        else:
            status = 'Not a superuser'
    return Response({'status': status})

 

class Notes(ListCreateAPIView):
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer



@api_view(['GET'])
def userDetails(request, pk):
    user = User.objects.get(id=pk)
    serializer = userSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def userUpdate(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=request.data)
    print(request.data)
    # print(serializer)
    if serializer.is_valid():
        serializer.save()
        print('updated',serializer.data)
    return Response(serializer.data)