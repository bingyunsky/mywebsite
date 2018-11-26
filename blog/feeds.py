#-*- coding:utf-8 -*-
# Author:Vincent Zhang

from django.contrib.syndication.views import Feed

from .models import Post

class AllPostsRssFeed(Feed):
    title = 'Django 博客教程'
    link = "/"
    description = 'Django博客教程演示项目测试文章'

    # 需要显示的内容条目
    def items(self):
        return Post.objects.all()

    # 聚合器中显示的内容条目的描述
    def item_description(self, item):
        return item.body

