from django.db import models


class User(models.Model):
    user_name = models.CharField('用户名', max_length=30)
    jaccount = models.CharField('Jaccount', max_length=30, unique=True)
    # is_active = models.BooleanField('是否活跃', default=True)

    class Meta:
        db_table = 'User'
        verbose_name = 'User'
        verbose_name_plural = 'User'

    def __str__(self):
        return '%s' % self.user_name


class Site(models.Model):
    user = models.ForeignKey(User, to_field='jaccount', on_delete=models.CASCADE, default='000')
    site_name = models.CharField('网站名', max_length=30)
    site_url = models.CharField('网址', max_length=120)
    site_src = models.CharField('图标地址', max_length=120)
    is_active = models.BooleanField('是否活跃', default=True)

    class Meta:
        db_table = 'site'
        verbose_name = 'site'
        verbose_name_plural = 'site'

    def __str__(self):
        return '网址 %s' % self.site_name


class SimpleMode(models.Model):
    user = models.ForeignKey(User, to_field='jaccount', on_delete=models.CASCADE, default='000')
    username = models.CharField('用户名', max_length=30, default='visitor')
    is_active = models.BooleanField('是否活跃', default=False)

    class Meta:
        db_table = 'simpleMode'
        verbose_name = 'simpleMode'
        verbose_name_plural = 'simpleMode'

    def __str__(self):
        return '%s' % self.username


class Wallpaper(models.Model):
    user = models.ForeignKey(User, to_field='jaccount', on_delete=models.CASCADE, default='000')
    username = models.CharField(max_length=64, default='visitor')
    photo = models.ImageField(upload_to='wallpaper/', default="#")
    photo_name = models.CharField(max_length=120, default='visitor.jpg')
    css = models.CharField(max_length=120, default="")

    class Meta:
        db_table = 'Wallpaper'
        verbose_name = 'Wallpaper'
        verbose_name_plural = 'Wallpaper'

    def __str__(self):
        return '%s' % self.username


class Countdown(models.Model):
    user = models.ForeignKey(User, to_field='jaccount', on_delete=models.CASCADE, default='000')
    username = models.CharField(max_length=64, default='visitor')
    date_name = models.CharField(max_length=64, default="元旦")
    year = models.IntegerField(default=2023)
    month = models.IntegerField(default=1)
    day = models.IntegerField(default=1)

    class Meta:
        db_table = 'countdown'
        verbose_name = 'countdown'
        verbose_name_plural = 'countdown'

    def __str__(self):
        return '%s' % self.username
