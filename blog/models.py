from django.db import models

class Post(models.Model):
  title = models.CharField(max_length=200) # verbose_name="Заголовок"
  text = models.TextField() # verbose_name="Заголовок" Отличие varChar от text, в теxt пограничение по поличеству вводимов ссимволов. В text нет ограничений.
  created_at = models.DateTimeField(auto_now_add=True) # как только мы создали пост, автоматически нужно указать now (дата и время)

  class Meta: # доп настройки
    # verbose_name = "Пост"
    # verbose_name_plural = "Посты"
    db_table = 'blog_posts' # Название для таблицы

    # def __str__(self):
    #   return self.tilte