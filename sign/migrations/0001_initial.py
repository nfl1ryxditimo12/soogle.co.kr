# Generated by Django 3.1.5 on 2021-01-15 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='아이디')),
                ('nickname', models.CharField(max_length=32, verbose_name='별명')),
                ('email', models.EmailField(max_length=128, verbose_name='이메일')),
                ('password', models.CharField(max_length=32, verbose_name='비밀번호')),
                ('register_date', models.DateTimeField(verbose_name='등록날짜')),
            ],
            options={
                'verbose_name': '사용자',
                'verbose_name_plural': '사용자',
                'db_table': '사용자',
            },
        ),
    ]
