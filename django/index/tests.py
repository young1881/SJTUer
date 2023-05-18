from django.test import TestCase
from .models import Site, SimpleMode, User, Wallpaper, Countdown


class TestModels(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            user_name='test_name',
            jaccount="test_jaccount")
        self.site = Site.objects.create(
            user=self.user,
            site_name="test_site_name",
            site_url="test_site_url",
            site_src="test_site_src",
            is_active=True)
        self.simple_mode = SimpleMode.objects.create(user=self.user)
        self.wallpaper = Wallpaper.objects.create(user=self.user)
        self.countdown = Countdown.objects.create(user=self.user)

    def test_user_model(self):
        self.assertEqual(self.user.jaccount, 'test_jaccount')
        self.assertEqual(self.site.site_name, 'test_site_name')
        self.assertEqual(self.simple_mode.is_active, False)
        self.assertEqual(self.wallpaper.photo, "#")
        self.assertEqual(self.countdown.date_name, "元旦")


class TestIndexViews(TestCase):

    def test_index_page(self):
        response = self.client.get("/index/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('website.html')

    def test_default_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('website.html')


class TestAjaxPost(TestCase):

    # 发起ajax请求前，模拟用户已经登录了，初始化相应的数据内容
    def setUp(self):
        self.user = User.objects.create(
            user_name='test_name',
            jaccount="test_jaccount")
        self.site = Site.objects.create(
            user=self.user,
            site_name="test_site_name",
            site_url="www.testsiteurl.com/",
            site_src="test_site_src",
            is_active=True)
        self.simple_mode = SimpleMode.objects.create(user=self.user)
        self.wallpaper = Wallpaper.objects.create(user=self.user)
        self.countdown = Countdown.objects.create(user=self.user)
        session = self.client.session
        session['jaccount'] = 'test_jaccount'
        session.save()

    def test_add_site(self):
        add_site_data = {
            'site_name': 'new_site_name',
            'site_url': 'www.testsiteurl.com/123456'
        }
        response = self.client.post("/index/add_site/", data=add_site_data)
        self.assertEqual(response.status_code, 200)

    def test_refactor_site(self):
        refactor_site_data = {
            'refactor_site_name': 'refactor_site_name',
            'refactor_site_url': 'www.testsiteurl.com/'
        }
        response = self.client.post("/index/refactor_site/", data=refactor_site_data)
        self.assertEqual(response.status_code, 200)

    def test_delete_site(self):
        delete_site_data = {"delete_site_name": "test_site_name"}
        response = self.client.post("/index/delete_site/", data=delete_site_data)
        self.assertEqual(response.status_code, 200)

    def test_simple_mode(self):
        is_active = {"simple_mode_is_active": "true"}
        response = self.client.post("/index/simple_mode/", data=is_active)
        self.assertEqual(response.status_code, 200)

    def test_color_wallpaper(self):
        css = {"css": "css_text"}
        response = self.client.post("/index/color_wallpaper/", data=css)
        self.assertEqual(response.status_code, 200)

    def test_refactor_countdown(self):
        countdown_data = {
            "refactor_date_name": "test_date_name",
            "year": "2022",
            "month": "01",
            "day": "01"
        }
        response = self.client.post("/index/refactor_countdown/", data=countdown_data)
        self.assertEqual(response.status_code, 200)
