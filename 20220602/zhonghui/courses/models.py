from django.db import models

# Create your models here.
class Teacher(models.Model):
    nickname=models.CharField(max_length=30,primary_key=True,db_index=True,verbose_name='昵称')
    introduction=models.TextField(default="这个老师很懒，没有介绍....",verbose_name='简介')
    fans=models.PositiveIntegerField(default=0,verbose_name='粉丝')
    create_at=models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    update_at = models.DateTimeField(auto_now=True,verbose_name='更新时间')

    class Meta:
        db_table='teacher'
        verbose_name='讲师信息表'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.nickname

class Course(models.Model):
    title=models.CharField(max_length=100,primary_key=True,db_index=True,verbose_name='课程名')
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE,verbose_name='教师')
    type=models.SmallIntegerField(choices=((1,'后端开发'),(2,'数据挖掘'),(0,'其它')),default=0,verbose_name='课程类型')
    price=models.PositiveSmallIntegerField(verbose_name='价格')
    volume=models.BigIntegerField(verbose_name='销量')
    online=models.DateField(verbose_name='上线时间')
    created_at=models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    updated_at=models.DateTimeField(auto_now=True,verbose_name="更新时间")

    class Meta:
        db_table='courses'
        verbose_name='课程信息表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return f"{self.get_type_display()}--{self.title}"



class Student(models.Model):
    """学生信息表"""
    nickname=models.CharField(max_length=30,primary_key=True,db_index=True,verbose_name="昵称")
    course=models.ManyToManyField(Course,verbose_name="课程")#多对多关系
    age=models.PositiveSmallIntegerField(verbose_name="年龄")
    gender=models.SmallIntegerField(choices=((1,'男'),(2,'女'),(0,'保密')),default=0,verbose_name="性别")
    study_time=models.PositiveIntegerField(default="0",verbose_name="学习时长(h)")
    created_at=models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    updated_at=models.DateTimeField(auto_now=True,verbose_name="更新时间")

    class Meta:
        db_table='student'
        verbose_name = '学生信息表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.nickname


class TeacherAssistant(models.Model):
    nickname=models.CharField(max_length=30,primary_key=True,db_index=True,verbose_name="昵称")
    teacher=models.OneToOneField(Teacher,null=True,blank=True,on_delete=models.SET_NULL,verbose_name="讲师")
    hobby=models.CharField(max_length=100,null=True,blank=True,verbose_name="爱好")
    created_at=models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    updated_at=models.DateTimeField(auto_now=True,verbose_name="更新时间")

    class Meta:
        db_table='teacher_assistant'
        verbose_name = '助教信息表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.nickname