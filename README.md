# magalu-finder

O objetivo do magalu-finder é procurar um determinado produto na loja mais próxima, conforme seu CEP.


## Funcionalidades

### Administrativo:


1. GESTOR DE LOJAS

2. GESTOR DE PRODUTOS


### Clientes:

1. PROCURAR PRODUTOS MAIS PROXIMOS CONFORME O CEP


### Setup do projeto:

#### Ambiente virtual para execução:

    ```sh
    $ virtualenv env-ml

    $ source ~/env-ml/bin/activate

    $ git clone https://github.com/projetormb/magalu-finder.git

    $ cd ./magalu-finder/

    $ pip install -r requirements.txt
    ```


 

#### Execução dos serviços (Flask) :

    ```sh
    $ cd ./magalu-finder/src/
 
    $ python rotas.py

    Acesse em seu navegador:  http://127.0.0.1:5000/
    ```

#### Execução dos testes:

    ```sh
    $ cd ./magalu-finder/src/
 
    $ python tests.py
    ```
