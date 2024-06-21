# -*- coding: utf-8 -*-
from collections import defaultdict

from django.views.generic.base import TemplateView
from random import uniform
from django.shortcuts import render
from collections import defaultdict
from model.db import create_db
from django.views.decorators.csrf import csrf_exempt
import json

from model import insert as i
from model import delete as d

class IndexView(TemplateView):
    template_name = "index.html"

@csrf_exempt
def send_data(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        last_name = data.get('last_name')
        course = data.get('course')
        fac = data.get('fac')
        ## Заносим в БД
        i.ins(name, last_name, course, fac)
        ## Если ОК
        return JsonResponse({'status': 'success'})
    ## Если Ошиблка
    return JsonResponse({'status': 'fail', 'message': 'Не удалось добавить данные.'})

@csrf_exempt
def delete_data(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        id = data.get('id')
        ## Заносим в БД
        d.del_student(id)
        ## Если ОК
        return JsonResponse({'status': 'success'})
    ## Если Ошиблка
    return JsonResponse({'status': 'fail', 'message': 'Не удалось удалить данные.'})


from django.http import JsonResponse
from model import select as s

def get_students(request):
    # Обработка GET-запроса и получение данных
    rows = s.get_studentss()
    print(rows)
    data = {
        'data': rows,
    }
    return JsonResponse(data)
