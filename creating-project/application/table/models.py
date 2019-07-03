from django.db import models


class Table(models.Model):
    col_num = models.IntegerField(primary_key=True)
    col_name = models.CharField(max_length=20)
    col_width = models.IntegerField(default=1)

    def __str__(self):
        return self.col_name

class Path(models.Model):
    path = models.FilePathField()

    def get_path(self):
        return self.path

    def set_path(self, new_path):
        self.path = new_path

    def __str__(self):
        return self.path