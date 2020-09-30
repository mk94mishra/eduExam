# Generated by Django 3.1.1 on 2020-09-30 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('published', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExamSubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('published', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('exam_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='createExam.exam')),
            ],
        ),
        migrations.CreateModel(
            name='ExamSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('published', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('exam_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='createExam.exam')),
                ('sub_cat_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='createExam.examsubcategory')),
            ],
        ),
        migrations.CreateModel(
            name='ExamTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('published', models.BooleanField(default=True)),
                ('parent_topic_id', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('exam_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='createExam.exam')),
                ('sub_cat_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='createExam.examsubcategory')),
                ('sub_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='createExam.examsubject')),
            ],
        ),
    ]
