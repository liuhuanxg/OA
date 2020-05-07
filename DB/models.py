#-*-coding:utf-8 -*-
"""
@project:OA
@File: models.py
@user：liuhuan   
"""
from settings import db


# 用户信息表
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    nickname = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    phone = db.Column(db.String(11), unique=True)

    def __init__(self,username,email):
        self.username = username
        self.email = email

    def __repr__(self):
        return "User {}".format(self.username)

    def __str__(self):
        return self.username



# 1、创建数据库
# db.create_all()

# 2、插入数据
# admin = User("admin","admin@sina.cn")
# user1 = User("user1","user1@sina.cn")
# db.session.add(admin)
# db.session.add(user1)
# db.session.commit()

# 3、查询数据
# user = User.query.all()
# print(user,type(user))
#
# admin = User.query.filter_by(username="admin").first()
# print(admin)


# 创建关系数据表
from datetime import datetime


class Post(db.Model):
    """在从表中添加ForeignKey和relationship"""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category',
        backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, title, body, category, pub_date=None):
        self.title = title
        self.body = body
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date
        self.category = category

    def __repr__(self):
        return '<Post %r>' % self.title


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Category %r" %self.name

# 1、创建数据库
# db.create_all()

# 2插入数据
# py = Category("Python")
# db.session.add(py)

# p = Post("Hello Python!", "Python is pretty coll",Category.query.filter_by(name="Python").first())
# db.session.add(p)

# db.session.commit()


# 3、查询

# (1) 主表查从表数据  通过backref属性进行反向查询
py = Category.query.filter_by(name="Python").first()
print(py.posts.all())

# (2) 从表查主表数据  直接使用(.外键字段)进行正向查询
p =Post.query.filter_by(title="Hello Python!").first()
print(p.category)


# 多对多关联

