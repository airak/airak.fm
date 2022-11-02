# airak.fm

Um sistema de publicação de tweets com base no seu histórico semanal do last.fm

## Instalação (linux e mac)

Para execução do projeto siga os seguintes passos:

1. Instale o [virtualenv](https://pypi.python.org/pypi/virtualenv) e o [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/). Eles possibilitam a criação de vários ambientes virtuais para o gerenciamento de projetos (em python), evitando conflitos e outros tipos de problemas. Caso tenha problemas no processo de instalação leia [este material](https://medium.com/@otaviobn/ambiente-virtual-python-com-virtualenv-virtualenvwrapper-no-ubuntu-instala%C3%A7%C3%A3o-e-uso-5e6691b92695).

```shell
pip install virtualenv
pip install virtualenvwrapper
```

2. Crie e acesse um ambiente virtual definindo como padrão a versão 3 do python.

Caso vá usar o virtualenvrrapper
```shell
mkvirtualenv --python=`which python3` envName
workon envName
```

Caso esteja usando o virtualenv
```shell
python3 -m venv envName
source envName/bin/activate
```

3. Clone o repositório do projeto no github (isto criará uma pasta com o nome do projeto no diretório atual).

```shell
git clone https://github.com/Airak/airak.fm.git airak_fm
```

4. Instale as dependências do projeto.

```shell
cd airak_fm
pip install -r requirements.txt
```

5. Rode a aplicação.

```shell
cd api
python manage.py runserver
```

6. Abra o seu navegador e acesse:

http://127.0.0.1/8000