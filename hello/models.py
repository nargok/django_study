from django.db import models

class Friend(models.Model):
  name = models.CharField(max_length=100)
  mail = models.CharField(max_length=200)
  gender = models.BooleanField()
  age = models.IntegerField(default=0)
  birthday = models.DateField()

  # Friendクラスのインスタンスをtempalteで書き出したときの内容をカスタマイズしている
  def __str__(self):
    return '<Friend:id=' + str(self.id) + ', ' + \
      self.name + '(' + str(self.age) + ')>'