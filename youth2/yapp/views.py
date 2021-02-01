# from django.shortcuts import render
#
# # Create your views here.
# from django.contrib.auth.models import User
# import mysql.connector as mq
#
# def userdata(req):
#     user=User.objects.all()
#
#     user=user[0]
#     con = mq.connect(host="localhost", port="3306", username="root", password="root", database="youthdb")
#     cur=con.cursor()
#     q="insert into "
#     args={'user':user}
#
#     print(User.email)
#     s=User.last_name
#     print(s)
#     return render(req,"yapp/userdata.html",args)
from django.contrib.auth.models import User
from rest_framework import generics
from . import serializer,models
class Create(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializer.UserSerializer
