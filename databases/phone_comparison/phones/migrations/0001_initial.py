# Generated by Django 2.1.1 on 2019-06-14 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airpods', models.BooleanField(verbose_name='наушники AirPods')),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(choices=[('Samsung', 'Samsung'), ('Apple', 'Apple')], max_length=30, verbose_name='производитель')),
                ('model', models.CharField(max_length=30, verbose_name='модель')),
                ('country', models.CharField(max_length=10, verbose_name='страна производителя')),
                ('price', models.IntegerField(verbose_name='цена')),
                ('release_date', models.DateField(verbose_name='дата выпуска')),
                ('os', models.CharField(max_length=30, verbose_name='операционная система')),
                ('processor', models.CharField(max_length=30, verbose_name='процессор')),
                ('cellular_band', models.TextField(verbose_name='диапазон сети')),
                ('screen_size', models.CharField(max_length=10, verbose_name='диагональ экрана')),
                ('screen_resolution', models.CharField(max_length=10, verbose_name='разрешение экрана')),
                ('back_camera_resolution', models.CharField(max_length=10, verbose_name='разрешение тыльной камеры')),
                ('front_camera_resolution', models.CharField(max_length=10, verbose_name='разрешение фронтальной камеры')),
                ('ram', models.CharField(max_length=10, verbose_name='оперативная память')),
                ('storage_capacity', models.CharField(max_length=10, verbose_name='встроенная память')),
                ('battery_capacity', models.CharField(max_length=10, verbose_name='емкость аккумулятора')),
                ('color', models.CharField(max_length=20, verbose_name='цвет')),
                ('phone_size', models.CharField(max_length=20, verbose_name='размер телефона')),
                ('memory_card_type', models.CharField(max_length=10, verbose_name='тип карты памяти')),
                ('bluetooth', models.CharField(max_length=10, null=True, verbose_name='стандарт bluetooth')),
                ('nfc', models.BooleanField(verbose_name='модуль NFC')),
            ],
        ),
        migrations.CreateModel(
            name='Samsung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_pen', models.BooleanField(verbose_name='стилус S-pen')),
                ('fm_radio', models.BooleanField(verbose_name='FM радио')),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phones.Phone')),
            ],
        ),
        migrations.AddField(
            model_name='apple',
            name='info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phones.Phone'),
        ),
    ]
