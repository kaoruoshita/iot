from django.contrib.auth.models import User
from django.http import Http404

from restapp.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from send_mail_script import sendMail
from manage_device_power import power_on_device, power_off_device
from device_photo import get_latest_photo
from device_state import get_device_state
from get_gmail import get_emails

from django.shortcuts import render
from PIL import Image
from django.http import HttpResponse

class GetAlarms(APIView):
    def get(self, request, format=None):
        msg = get_emails()
        return  Response(msg)

def index(request):
    image_data = open("/home/kaoru.oshita/rest_example/restapp/real_rack.jpg", "rb").read()
    return HttpResponse(image_data, content_type="image/png")

class GetDeviceState(APIView):
    def get(self, request, pk, format=None):
        state = get_device_state(pk)
        return  Response(state)

class GetDevicePhoto(APIView):
    def get(self, request, format=None):
        jpg = get_latest_photo()
        return  Response(jpg)

class DevicePower(APIView):
    def post(self, request, format=None):
    	data = request.data
        device_id = data['device_id']
        state = data['state']
        if state == "on":
            power_on_device(device_id)
        elif state == "off":
            power_off_device(device_id)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response("state: %s" % state, status=status.HTTP_201_CREATED)


class SendEmails(APIView):
    def post(self, request, format=None):
        #serializer = UserSerializer(data=request.data)

        #serializer.is_valid()
      
        data = request.data
        address_to = data['address_to']
        address_from = data['address_from']
        title = data['title']
        body = data['body']

#        sendMail(['Kaoru Oshita <kaoru.oshita@gmail.com>'],'test2 <test2@gmail.com>','Hello Python!','Heya buddy! Say hello to Python! :)',[])
        sendMail([address_to], address_from, title, body,[])
        return Response("Email Sent to: %s" % address_to  , status=status.HTTP_201_CREATED)


class UserList(APIView):
    """
    List all users, or create a new user.
    """
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        user = UserSerializer(user)
        return Response(user.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
