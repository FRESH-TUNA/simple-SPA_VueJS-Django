# VueJS와 Django를 연동하여 CRUD기능의 게시판 만들기
오픈 소스 프로그레시브 자바스크립트 프레임워크인 VueJS와 Django를 간단하게(?!) 연동하여 CRUD 
가능을 가진 Single Page Application을 구현해보았습니다.

## 1. 프로그램 구조
Django 프레임워크는 crudAPI과 Frontend두개의 app으로 구성되어있습니다. 
<br><br>
Frontend App에서는 index 페이지를 랜더링해주는 뷰함수와, 클라이언트 사이드 렌더링을 위해 필요한 
자바스크립트, 뷰 파일들을 포함하고 있습니다.
<br><br>
crudAPI App에서는 crud 기능을 제공하는 뷰함수들만을 포함하고 있으며, 철저히 Json 형태로 response를 
반환합니다. 클라이언트 사이드에서 서버에서 요청해서 받은 JsonResponse를 가지고 렌더링을 진행합니다.

## 2. 요구 환경
이 프로그램은 파이썬3, Django 프레임워크가 필요합니다.
<br>
This Program needs Python3, Django
```
brew install python3
```
윈도우환경에서는 그냥 python 으로 치시면 됩니다!
<br><br>
python 설치후 pip를 이용하여 Django를 설치할수 있지만, 가상환경을 이용한후 pip를 이용하여
설치하는것을 권장드립니다.
<br>
you can install Django using pip and but i recommend using virtualenv
```
brew install virtualenv
virtualenv venv
source venv/bin/activate
pip3 install django
```
윈도우환경에서는 그냥 pip 으로 치시면 됩니다!
<br>
설치후 아래의 명령어를 입력해 프로그램을 사용할수 있습니다.
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```