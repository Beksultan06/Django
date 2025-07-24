from django.db import models

# Create your models here.
class Settings(models.Model):
    facebook = models.URLField(
        verbose_name='Файсбук',
        help_text='Enter url Facebook'
    )
    twitter = models.URLField(
        verbose_name='Твитер',
        help_text='Enter url Twitter'
    )
    linkedin = models.URLField(
        verbose_name='Линкедин',
        help_text='Enter url Linkedin'
    )
    instagram = models.URLField(
        verbose_name='Instagram',
        help_text='Enter url Instagram'
    )
    address = models.CharField(
        max_length=155,
        verbose_name='Адрес',
        help_text='Нпишите свой адрес'   
    )
    email = models.EmailField(
        verbose_name='Email',
        help_text='Enter your Email'
    )
    working = models.CharField(
        max_length=155,
        verbose_name='Время работы',
        help_text='Напшите время работы'
    )

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'

class SettingsIndexPage(models.Model):
    welcome = models.CharField(
        max_length=155,
        verbose_name='Приветствие'
    )
    title =models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    image = models.ImageField(
        upload_to='settings',
        verbose_name='Фото'
    ) 
    title_about = models.CharField(
        max_length=155,
        verbose_name='Заголовка О нас'
    )
    description_about = models.TextField(
        verbose_name='Описание О нас'
    )
    end_description_about = models.CharField(
        max_length=155,
        verbose_name='Конец описание о нас'
    )
    title_viza = models.CharField(
        max_length=155,
        verbose_name='Заголовка Визы'
    )
    advantage = models.CharField(
        max_length=155,
        verbose_name='Примущество'
    )
    advantage_description = models.TextField(
        verbose_name='Описание примущество'
    )
    country_title = models.CharField(
        max_length=155,
        verbose_name='Страна заголовка'
    )
    faq = models.CharField(
        max_length=155,
        verbose_name='Часто задаваемые вопросы'
    )
    image_faq = models.ImageField(
        upload_to='settings',
        verbose_name='Фото FAQ'
    )
    faq2 = models.CharField(
        max_length=155,
        verbose_name='Заголовка элитные программы '
    )
    news_title = models.CharField(
        max_length=155,
        verbose_name='Заголовка Новости'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Настройка Главной Страницы'
        verbose_name_plural = 'Настройки Главной Страницы'    

class Banner(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Банер'