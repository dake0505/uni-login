from django.shortcuts import render, HttpResponse


# Create your views here.

def login(request):
    return HttpResponse("login success")


def query_user_list(request):
    return HttpResponse("user list")


def create_user(request):
    return HttpResponse("create success")


def update_user(request):
    return HttpResponse("update success")


def delete_user(request):
    return HttpResponse("delete success")

