# _*_ coding:utf-8 _*_
from django.shortcuts import render

# Create your views here.
from django.http import FileResponse


def download(request):
    file = open('apps/bds/download/file_upload.xlsx', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment; filename="file_upload.xlsx"'
    return response
