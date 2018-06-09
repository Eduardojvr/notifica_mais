from django.shortcuts import render
import urllib, json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import requests
from email.mime.text import MIMEText
import smtplib


@csrf_exempt
def sendmail(request, texto, subject, emails):
    mensagem = MIMEText(texto)
    mensagem.set_charset('utf-8')
    mensagem['Subject'] = subject
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login('noreplayfiscae@gmail.com', 'fiscaeunb')
    mail.sendmail('noreplayfiscae@gmail.com', emails, mensagem.as_string())

@csrf_exempt
def data_mensage(request):
    email_to = ['noreplayfiscae@gmail.com']
    subject = 'Quadro de horários'
    
    if request.method == "GET":
        return HttpResponse("Use post for this action")
    if request.method == "POST":
        d = json.loads(request.body)
        email = d["email"]
        segunda = d["segunda"]
        terca = d["terca"]
        quarta = d["quarta"]
        quinta = d["quinta"]
        sexta = d["sexta"]
        sabado = d["sabado"]
        domingo = d["domingo"]
        emailSend = "Seu quadro horários\n"+"Segunda: "+segunda+"\n"+"Terça: "+terca+"\n"+"Quarta: "+quarta+"\n"+"Quinta: "+quinta+"\n"+"Sexta: "+sexta+"\n"+"Sábado: "+sabado+"\n"+"Domingo: "+domingo
        sendmail(request, emailSend, subject, email)        
        # return HttpResponse("Use post for this action")
        return render(request, 'home.html')

