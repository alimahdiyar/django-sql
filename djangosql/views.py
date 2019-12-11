from django.shortcuts import render, redirect
from django.urls import reverse
from django.db import connection

def index_view(request):
    context = {'result': '', 'fetch_result': ''}
    if(request.POST and request.POST['sql']):
        query = request.POST['sql']
        with connection.cursor() as cursor:
            try:
                cursor.execute(query)
                context['fetch_result'] = cursor.fetchall()
                context['result'] = 'success'
            except Exception as ex:
                context['result'] = str(ex)
    return render(request, 'sqleditor.html', context)