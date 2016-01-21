# -*- coding: utf-8 -*-
"""
Create on 2016/1/21

@Author:MinRui

@Module Description:
"""
import os
import django
from rango.models import Category, Page

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoTest.settings')
django.setup()


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat,
                                   title=title,
                                   url=url,
                                   views=views)[0]
    return p


def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    return c


def populate():
    cn_cat = add_cat('CHINA')

    add_page(cat=cn_cat,
             title="Baidu",
             url="http://www.baidu.com")

    add_page(cat=cn_cat,
             title="Netease",
             url="http://www.163.com")

    us_cat = add_cat('USA')

    add_page(cat=us_cat,
             title="Google",
             url="http://www.google.com")

    add_page(cat=us_cat,
             title="Github",
             url="http://www.github.com")

if __name__ == '__main__':
    print "Starting Rango Population Script..."
    populate()
