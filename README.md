<p align="center"><a href="image" target="_blank"><img width="500"src="https://i.imgur.com/Psoo5PH.png"></a></p>
<p align="center">
    
[![Build Status](https://travis-ci.org/Eduardojvr/notifica_mais.svg?branch=master)](https://travis-ci.org/Eduardojvr/notifica_mais)
    
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

## 🐳 Guia de Uso do Docker

* ### Instalação
Primeiramente é necessário ter o docker instalado, caso não tenha acesse o [Instalação docker](https://docs.docker.com/engine/installation/linux/docker-ce/). Após feito isso, instale o [Docker-compose](https://docs.docker.com/compose/install/).

* ### Comandos básicos 

 &emsp;&emsp; Para a utilização do ambiente em background, basta dar o comando abaixo e ele irá ligar o container:
 
 ```terminal
  docker-compose up -d
 ```
 &emsp;&emsp; Caso queira utilizar o ambiente com logs:

 ```terminal
  docker-compose up 
 ```
 &emsp;&emsp; Para a visualização dos logs quando em modo de execução background, use o comando abaixo:

 ```terminal
  docker-compose logs -f
 ```

 &emsp;&emsp; Para pausar o container:

  ```terminal
  docker-compose stop
 ```
 &emsp;&emsp; E para religar um container parado use o comando: 
 
 ```terminal
  docker-compose start 
 ```

 &emsp;&emsp; Para listar os containers que estão em execução:
 
 ```terminal
  docker ps
 ```
 &emsp;&emsp; Para listar todos os containers já executados na sua máquina:
 
 ```terminal
  docker ps -a
 ```
 &emsp;&emsp; Para executar comandos dentro do container:
 
 ```terminal
  docker-compose exec -it  "id do container"  "comandos"
 ```
 Para acessar o [bash](https://www.gnu.org/software/bash/) do container, substitua "comandos" por "bash".

* ## Rodando a aplicação no localhost

Para rodar a aplicação, entre na pasta do projeto em que está localizado o __docker-compose__ e digite no terminal:

```
  docker-compose up -d
```
Espere até que todos os serviços estejam disponíveis, acesse a página inicial do projeto com o seguinte endereço: https://localhost:8000/notifyEvent/data_mensage

Para utilizar o serviço siga o passo "Uso" substituindo a url aprensentada pelo endereço apresentado neste tópico.
