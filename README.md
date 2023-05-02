# Deploy de Aplicações Django no Render.com

Este repositório contém um exemplo de como fazer o deploy de aplicações Django usando o serviço Render.com.

## Pré-requisitos

Antes de começar, você precisará ter uma conta no **Render.com**, cloudinary.com e bit.io e um aplicativo Django funcional. Certifique-se de ter um arquivo `requirements.txt` com as dependências necessárias do seu projeto.

## Instruções de uso importantes [TIPS]

1.  **Atenção às definições do django** , principalmente no whitenoise, seguir os tutorial do render.com dará erros
     - 1.1 https://render.com/docs/deploy-django#static-files
     - 1.2 **STATICFILES_STORAGE** = 'whitenoise.storage.CompressedManifestStaticFilesStorage' é para django antigos
     - 1.3 **STATIC_ROOT** = os.path.join(BASE_DIR, 'staticfiles') , terás de usar sempre 'staticfiles' para colocar as teus ficheiros
     - 1.4 **STATICFILES_DIRS**, adicionar qual é a origem (caminho) onde estão os teus ficheiros estaticos
     - 1.5 **WHITENOISE_MANIFEST_STRICT**, se der algum problema com manifests
 
2.  Atenção que no render.com **deverá colocar as variaveis** primeiro
     - 2.1 DEBUG = 0 ou 1
     - 2.2 PYTHON_VERSION = 3.10.11 , versão necessaria para o projecto
     - 2.3 RENDER_EXTERNAL_URL = url necessario
     - 2.4 SECRET_KEY = gerar uma, render dá essa possibilidade
     - 2.5 WEB_CONCURRENCY = 4
     - 2.6 DATABASE_URL = normal 
     - 2.7 CLOUDINARY__API_SECRET , CLOUDINARY_API_KEY e CLOUDINARY_CLOUD_NAME
     
3.  Render settings deverá colocar   
     - 3.1 Build Command -> sh build.sh
     - 3.2 Start Command -> gunicorn NOMEAPP.wsgi:application
     - 3.3 Auto deploy -> render.com gratis é lento, muito lento, por isso é uma questão escolha!
     - 3.4 Custom Domains, é muito facil é só seguir os passos


Mário ANTUNES @ 2023


