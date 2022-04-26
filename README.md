# Eventex

Sistema de Eventos ecomendado pela Morena

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a Instância com o .env
6. Execute os testes

```console
git clone git@github.com:venanciomitidieri/eventex.git wttd
cd wttd
python -m venv .wttd
source .\.wttd\scripts\activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?
1. Crie uma instância no heroku
2. Envie as configurações para o heroku
3. Define uma SECRETY_KEY segura para instância
4. Defina DEGUB=False
5. Configure o serviço de email
6. Envie o código para o heroku

```console
heroku create minhainstancia
keroku config:push
heroku config:set SECRET_KEY='python contrib/secret_gen.py'
heroku config:set DEBIG=False
# configura o email
git push heroku master --force
```