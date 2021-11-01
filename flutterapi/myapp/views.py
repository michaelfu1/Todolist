from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import TodolistSerializer
from .models import Todolist

# GET Data
@api_view(['GET'])
def all_todolist(request):
    alltodolist = Todolist.objects.all() #ดึงข้อมูลจาก model Todolist "SELECT * FROM Todolist"
    serializer = TodolistSerializer(alltodolist,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
        

# POST Data (save data to database)
@api_view(['POST'])
def post_todolist(request):
        if request.method == 'POST':
            serializer = TodolistSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def update_todolist(request,TID):
    # localhost:8000/api/update-todolist/13
    todo = Todolist.objects.get(id=TID)
    if request.method == 'PUT':
        data = {}
        serializer = TodolistSerializer(todo,data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['status'] = 'updated'
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_todolist(request, TID):
    todo = Todolist.objects.get(id=TID)

    if request.method == 'DELETE':
        delete = todo.delete()
        data = {}
        if delete:
            data['status'] = 'deleted'
            statuscode = status.HTTP_200_OK
        else:
            data['status'] = 'failed'
            statuscode = status.HTTP_400_BAD_REQUEST

        return Response(data=data, status=statuscode)








data = [
    {
        "title":"แล็ปท็อปคืออะไร?",
        "subtitle":"คอมพิวเตอร์ คือ อุปกรณ์ที่ใช้สำหรับการคำนวณและทำงานอื่นๆ",
        "image_url":"https://raw.githubusercontent.com/michaelfu1/BasicAPI/main/computer.png",
        "detail":"คอมพิวเตอร์ (อังกฤษ: computer) หรือศัพท์บัญญัติราชบัณฑิตยสภาว่า คณิตกรณ์ เป็นเครื่องจักรแบบสั่งการได้ที่ออกแบบมาเพื่อดำเนินการกับลำดับตัวดำเนินการทางตรรกศาสตร์หรือคณิตศาสตร์\n\nโดยอนุกรมนี้อาจเปลี่ยนแปลงได้เมื่อพร้อม ส่งผลให้คอมพิวเตอร์สามารถแก้ปัญหาได้มากมาย"
   
    },
    {
        "title":"Flutter คือ?",
        "subtitle":"Tools สำหรับออกแบบ UI ของ Google",
        "image_url":"https://raw.githubusercontent.com/michaelfu1/BasicAPI/main/Flutter.jpg",
        "detail":"Flutter คือ Framework ที่ใช้สร้าง UI สำหรับ mobile application ที่สามารถทำงานข้ามแพลตฟอร์มได้ทั้ง iOS และ Android ในเวลาเดียวกัน โดยภาษาที่ใช้ใน Flutter นั้นจะเป็นภาษา dart ซึ่งถูกพัฒนาโดย Google และที่สำคัญคือเป็น open source ที่สามารถใช้งานได้แบบฟรี ๆ อีกด้วย"
    },
    {
        "title":"Python คือ?",
        "subtitle":"ภาษาที่ใช้ในการเขียนโปรแกรม",
        "image_url":"https://raw.githubusercontent.com/michaelfu1/BasicAPI/main/Python.jpg",
        "detail":"ภาษาไพทอน (Python programming language) หรือที่มักเรียกกันว่าไพทอน เป็นภาษาระดับสูงซึ่งสร้างโดยคีโด ฟัน โรสซึม โดยเริ่มในปี พ.ศ.2533 การออกแบบของภาษาไพทอนมุ่งเน้นให้ผู้โปรแกรมสามารถอ่านชุดคำสั่งได้โดยง่ายผ่านการใช้งานอักขระเว้นว่าง (whitespaces) จำนวนมาก นอกจากนั้นการออกแบบภาษาไพทอนและการประยุกต์ใช้แนวคิดการเขียนโปรแกรมเชิงวัตถุในตัวภาษายังช่วยให้นักเขียนโปรแกรมสามารถเขียนโปรแกรมที่เป็นระเบียบ อ่านง่าย มีขนาดเล็ก และง่ายต่อการบำรุง[3]\n\nไพทอนเป็นภาษาแบบไดนามิกพร้อมตัวเก็บขยะ ไพทอนรองรับกระบวนทัศน์การเขียนโปรแกรมหลายรูปแบบ ซึ่งรวมถึงแต่ไม่จำกัดเพียงการเขียนโปรแกรมตามลำดับขั้น การเขียนโปรแกรมเชิงวัตถุ หรือการเขียนโปรแกรมเชิงฟังก์ชัน นอกจากนี้ไพทอนเป็นภาษาที่มักถูกอธิบายว่าเป็นภาษาโปรแกรมแบบ มาพร้อมถ่าน (batteries included) กล่าวคือไพทอนมาพร้อมกับไลบรารีมาตรฐานจำนวนมาก เช่นโครงสร้างข้อมูลแบบซับซ้อน และไลบรารีสำหรับคณิตศาสตร์"
    }    
]

def Home(request):
    return JsonResponse(data=data,safe=False,json_dumps_params={'ensure_ascii':False})

# Create your views here.
