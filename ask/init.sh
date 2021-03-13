# gurm /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
#ln -sf /home/box/web/etc/gunicorn-django.conf #/etc/gunicorn.d/test-django
#/etc/init.d/gunicorn restart
gunicorn -c /home/box/web/etc/gunicorn-django.py ask.wsgi:application &