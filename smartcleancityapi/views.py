from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import User, Complaint, Bin
from .serializer import UserSerializer, BinSerializer, ComplaintSerializer

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status




class ViewComplaintAdmin(APIView):

    def get(self, request):
        complaint = Complaint.objects.all()
        serializer = ComplaintSerializer(complaint, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class ViewUsers(APIView):

    def get(self, request):
        complaint = User.objects.all()
        serializer = UserSerializer(complaint, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class ViewComplaintUser(APIView):

    def post(self, request):
        uid = request.data['uid']
        complaint1 = Complaint.objects.filter(uid=uid)
        serializer = ComplaintSerializer(complaint1, many=True)
        return Response(serializer.data)


class ViewAssignedWorkAdmin(APIView):

    def post(self, request):
        driver_id = request.data['did']
        c_status = request.data['status']
        work = Complaint.objects.filter(did=driver_id, status=c_status)
        serializer = ComplaintSerializer(work, many=True)
        return Response(serializer.data)



class ViewWorkDriver(APIView):

    def post(self, request):
        driver_id = request.data['did']
        work = Complaint.objects.filter(did=driver_id)
        serializer = ComplaintSerializer(work, many=True)
        return Response(serializer.data)



class GetDriverListAdmin(APIView):

    def post(self, request):
        driver = request.data['role']
        list = User.objects.filter(role=driver)
        serializer = UserSerializer(list, many=True)
        return Response(serializer.data)



class GetBinListAdmin(APIView):

    def get(self, request):
        bin = Bin.objects.all()
        serializer = BinSerializer(bin, many=True)
        return Response(serializer.data)





@api_view(['POST', ])
def createComplaint(request):

    try:
        print("got req client reg " + str(request.data))
        c_uid = request.data['usrid']
        c_description = request.data['cmplntdescription']
        c_photo = request.data['cmplntphoto']
        c_clat = request.data['cmplntlat']
        c_clon = request.data['cmplntlon']


        user = User.objects.filter(uid=c_uid)


        complaint = Complaint.objects.create(uid=user.first(), did="", description=c_description, photo=c_photo, clat=float(c_clat), clong=float(c_clon), status= "not assigned")


        data = {}
        data["status"] = "success"
        data["message"] = 'Complaint Raised Successfully !'
        return Response(data=data)

    except:
        return Response({'status': 'failed', 'message': 'something went wrong!'})



@api_view(['POST', ])
def createBin(request):

    try:
        print("got req client reg " + str(request.data))
        c_blat = request.data['blat']
        c_blong = request.data['blong']
        c_baddr = request.data['baddr']


        #user = User.objects.filter(uid=c_uid)


        bin = Bin.objects.create(alat=float(c_blat), along=float(c_blong), address=c_baddr)


        data = {}
        data["status"] = "success"
        data["message"] = 'Bin Created Successfully !'
        return Response(data=data)

    except:
        return Response({'status': 'failed', 'message': 'something went wrong!'})




@api_view(['POST', ])
def assignWorkAdmin(request):

    try:
        print("got req client reg " + str(request.data))
        a_did = request.data['did']
        a_status = request.data['status']

        to_update = Complaint.objects.filter(did=a_did).update(name=a_status)


#        bin = Bin.objects.create(alat=float(c_blat), along=float(c_blong), address=c_baddr)


        data = {}
        data["status"] = "success"
        data["message"] = 'Work Assigned Successfully !'
        return Response(data=data)

    except:
        return Response({'status': 'failed', 'message': 'something went wrong!'})




