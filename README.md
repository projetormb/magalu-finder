# magalu-finder

O objetivo do magalu-finder é procurar um determinado produto na loja mais próxima, conforme seu CEP.


## Funcionalidades

### Administrativo:


1. GESTOR DE LOJAS

2. GESTOR DE PRODUTOS


### Clientes:

1. PROCURAR PRODUTOS MAIS PROXIMOS CONFORME O CEP (em desenvolvimento)


### Setup do projeto:

#### Ambiente virtual para execução:

    $ virtualenv env-ml -p /usr/bin/python2.7

    $ source ./env-ml/bin/activate

    $ git clone https://github.com/projetormb/magalu-finder.git

    $ pip install -r ./magalu-finder/requirements.txt
 
#### Execução dos serviços (Flask) :

    $ cd ./magalu-finder/src/
 
    $ python rotas.py

    Acesse em seu navegador:  http://127.0.0.1:5000/

#### Execução dos testes:

    $ cd ./magalu-finder/src/
 
    $ python tests.py

