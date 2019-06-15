from django.db import models

# Create your models here.
class Phone(models.Model):

  BRAND_CHOISES = [
    ('Samsung', 'Samsung'),
    ('Apple', 'Apple')
  ]

  model = models.CharField(max_length=30, verbose_name='модель')
  brand = models.CharField(max_length=30, choices=BRAND_CHOISES, verbose_name='производитель')
  country = models.CharField(max_length=10, verbose_name='страна производителя')
  price = models.IntegerField(verbose_name='цена')
  release_date = models.DateField(verbose_name='дата выпуска')
  os = models.CharField(max_length=30, verbose_name='операционная система')
  processor = models.CharField(max_length=30, verbose_name='процессор')
  cellular_band = models.TextField(verbose_name='диапазон сети')
  screen_size = models.CharField(max_length=10, verbose_name='диагональ экрана')
  screen_resolution = models.CharField(max_length=10, verbose_name='разрешение экрана')
  back_camera_resolution = models.CharField(max_length=10, verbose_name='разрешение тыльной камеры')
  front_camera_resolution = models.CharField(max_length=10, verbose_name='разрешение фронтальной камеры')
  ram = models.CharField(max_length=10, verbose_name='оперативная память')
  storage_capacity = models.CharField(max_length=10, verbose_name='встроенная память')
  battery_capacity = models.CharField(max_length=10, verbose_name='емкость аккумулятора')
  color = models.CharField(max_length=20, verbose_name='цвет')
  phone_size = models.CharField(max_length=20, verbose_name='размер телефона')
  memory_card_type = models.CharField(max_length=10, verbose_name='тип карты памяти')
  bluetooth = models.CharField(max_length=10, verbose_name='стандарт bluetooth', null=True)
  nfc = models.BooleanField(verbose_name='модуль NFC')

  def __str__(self):
    return f'{self.brand} {self.model}'


class Samsung(models.Model):
  s_pen = models.BooleanField(verbose_name='стилус S-pen')
  fm_radio = models.BooleanField(verbose_name='FM радио')
  info = models.ForeignKey(Phone, on_delete=models.CASCADE)

  def __str__(self):
    return f'Samsung {self.info.model}'

class Apple(models.Model):
  airpods = models.BooleanField(verbose_name='наушники AirPods')
  info = models.ForeignKey(Phone, on_delete=models.CASCADE)

  def __str__(self):
    return f'Apple {self.info.model}'