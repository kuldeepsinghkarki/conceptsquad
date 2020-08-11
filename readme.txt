1. pip3 install virtualenv
2. mkdir for your vitrual env
mkdir djangoenv

3. create virtual env with python 3
virtualenv -p python3 djangoenv

4. activate this virtualenv
source djangoenv/bin/activate

5. install djangoenv
pip install djangoenv

6. create your application site names conceptsite 
django-admin startproject conceptsite

7. cd to your conceptsite and then runserver and check if django working fine
cd conceptsite
python manage.py runserver

You will see following output and check browser at http://127.0.0.1:8000/
Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.

May 29, 2020 - 15:50:53
Django version 3.0, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

8. Now create your app/module 'PaymentsDemo'.make sure you’re in the same directory as manage.py
python manage.py startapp paymentsdemo
   This command will create 'PaymentsDemo' directory. 
9. Add your app to installed apps in settings.py and urls to conceptsite. Also do not forget to add 
'from django.conf.urls import include' in urls.py of conceptsite
10. Add import-export to settings.py of conceptsite

11. add import-export dependency
python -m pip install django-import-export

12. install numpy,scikit,panda
python -m pip install numpy scipy matplotlib pandas

output 
Installing collected packages: numpy, scipy, kiwisolver, pyparsing, six, python-dateutil, cycler, matplotlib, pandas
Successfully installed cycler-0.10.0 kiwisolver-1.2.0 matplotlib-3.2.1 numpy-1.18.4 pandas-1.0.4 pyparsing-2.4.7 python-dateutil-2.8.1 scipy-1.4.1 six-1.15.0

13. install scikit-learn
 python -m pip install -U scikit-learn
output
 Successfully installed joblib-0.15.1 scikit-learn-0.23.1 threadpoolctl-2.1.0

14. run python migrate to apply db changes
   python manage.py migrate

15. create Admin user for django
   python manage.py createsuperuser

