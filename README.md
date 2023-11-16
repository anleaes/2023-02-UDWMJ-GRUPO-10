# 2023-02-UDWMJ-GRUPO-10

# Ao executar o conda e voltar a resposta que nao foi encontrado, executar sempre o comando a seguir (Ajustar o caminho caso necessario):

%windir%\System32\cmd.exe "/K" C:\ProgramData\miniconda3\Scripts\activate.bat C:\ProgramData\miniconda3

# sempre ao abrir o terminal acesse a pasta apps

cd apps

# apos acessar a pasta apps para rodar o manage.py utilize a seguinte sintaxe

python ..\manage.py runserver

# ou 

python ..\manage.py makemigrations

# ou 

python ..\manage.py migrate

# ou

python ..\manage.py createsuperuser

# ou

python ..\manage.py startapp categories
