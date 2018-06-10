<p align="center"><a href="image" target="_blank"><img width="500"src="https://i.imgur.com/Psoo5PH.png"></a></p>
<p align="center">

## ℹ️ Sobre
O notifica mais é um micro serviço desenvolvido para oferecer suporte ao envio de email contendo os quadros de horários médicos da aplicação [Gerencia mais](https://github.com/fga-gpp-mds/2018.1_Gerencia_mais).

## ℹ️ Uso
Para utilizar o serviço, basta enviar os dados em formato [json](https://www.json.org/json-pt.html) para a url apresentada abaixo via POST obedecendo a seguinte estrutura:

Exemplo:
```Terminal
{
    "email":"email@gmail.com", 
    "segunda":"12:00 ~ 13:00 ",
    "terca":"12:00 ~ 13:00",
    "quarta":"12:00 ~ 13:00",
    "quinta":"12:00 ~ 13:00",
    "sexta":"12:00 ~ 13:00",
    "sabado":"12:00 ~ 13:00",
    "domingo":"12:00 ~ 13:00"
}
```
ℹ️ URL: https://notificamais.herokuapp.com/notifyEvent/data_mensage
