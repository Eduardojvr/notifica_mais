from django.shortcuts import render
import urllib, json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import requests

@csrf_exempt
def sendmail(request, texto, subject, emails):
    if request.method == "GET":
        mensagem = MIMEText(texto)
        mensagem.set_charset('utf-8')
        mensagem['Subject'] = subject
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login('noreplayfiscae@gmail.com', 'fiscaeunb')
        mail.sendmail('noreplayfiscae@gmail.com', emails, mensagem.as_string())


def data_mensage(request):
    email_to = ['noreplayfiscae@gmail.com']
    subject = 'Quadro de horários'
    text = 'Seu quadro de horário\n'
    
    if request.method == "GET":
        d = requests.get('http://localhost:8000/doctor/api-doctor/?format=json')
        # data = json.loads(url.read().decode())
        data = json.loads(d.content)

        # sendmail(request, text, subject, email_to)
        print("==================================")
        print(data)
        print("==================================")

    if request.method == "POST":
        print("==================================")
        print(data)
        print("AAAEEEEEEEEEE")
        print("==================================")
    
