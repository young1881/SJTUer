from django.test import TestCase
from .models import Site, SimpleMode, User, Wallpaper, Task


class TestModels(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            user_name='test_name',
            jaccount="000")
        self.site = Site.objects.create(
            user=self.user,
            site_name="test_site_name",
            site_url="test_site_url",
            site_src="test_site_src",
            is_active=True)
        self.simple_mode = SimpleMode.objects.create()
        self.wallpaper = Wallpaper.objects.create()
        self.task = Task.objects.create()

    def test_user(self):
        self.assertEqual(self.user.jaccount, '000')
        self.assertEqual(self.user.user_name, 'test_name')

    def test_site(self):
        self.assertEqual(self.site.site_name, 'test_site_name')
        self.assertEqual(self.site.site_src, "test_site_src")
        self.assertEqual(self.site.site_url, "test_site_url")
        self.assertEqual(self.site.is_active, True)

    def test_simple_mode(self):
        self.assertEqual(self.simple_mode.username, 'visitor')
        self.assertEqual(self.simple_mode.is_active, False)

    def test_wallpaper(self):
        self.assertEqual(self.wallpaper.username, 'visitor')
        self.assertEqual(self.wallpaper.css, "")
        self.assertEqual(self.wallpaper.photo, '#')
        self.assertEqual(self.wallpaper.photo_name, 'visitor.jpg')

    def test_task(self):
        self.assertEqual(self.task.username, 'visitor')
        self.assertEqual(self.task.category, 1)
        self.assertEqual(self.task.priority, 1)
        self.assertEqual(self.task.name, "新的任务")
        self.assertEqual(self.task.is_active, True)
        self.assertEqual(self.task.timeslice, 1)
        self.assertEqual(self.task.done, False)


class TestIndexViews(TestCase):

    def test_index(self):
        response = self.client.get("/index/")
        self.assertEqual(response.status_code, 200)

    def test_default(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)

    def test_scrapy(self):
        response = self.client.get("/index/scrapy")
        self.assertEqual(response.status_code, 301)

    def test_data(self):
        response = self.client.get("/index/data")
        self.assertEqual(response.status_code, 301)


class TestAxiosPost(TestCase):

    # 发起axios请求前，模拟用户已经登录了，初始化相应的数据内容
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
        self.task = Task.objects.create(user=self.user, name="test task")
        session = self.client.session
        session['jaccount'] = 'test_jaccount'
        session.save()

    def test_add_site(self):
        add_site_data = {
            'jaccount': 'test_jaccount',
            'site_name': 'new_site_name',
            'site_url': 'www.testsiteurl.com/123456'
        }
        response = self.client.post("/index/add_site/", data=add_site_data)
        self.assertEqual(response.status_code, 200)

    def test_refactor_site(self):
        refactor_site_data = {
            'jaccount': 'test_jaccount',
            'refactor_site_name': 'refactor_site_name',
            'refactor_site_url': 'www.testsiteurl.com/'
        }
        response = self.client.post("/index/refactor_site/", data=refactor_site_data)
        self.assertEqual(response.status_code, 200)

    def test_delete_site(self):
        delete_site_data = {'jaccount': 'test_jaccount', "delete_site_name": "test_site_name"}
        response = self.client.post("/index/delete_site/", data=delete_site_data)
        self.assertEqual(response.status_code, 200)

    def test_simple_mode(self):
        is_active = {'jaccount': 'test_jaccount', "simple_mode_is_active": "true"}
        response = self.client.post("/index/simple_mode/", data=is_active)
        self.assertEqual(response.status_code, 200)

    def test_add_task(self):
        task_data = {'jaccount': 'test_jaccount', 'name': 'test', 'priority': 1, 'category': 1, 'timeslice': 1,
                     'done': 0}
        response = self.client.post("/index/add_task/", data=task_data)
        self.assertEqual(response.status_code, 200)

    def test_delete_task(self):
        task_data = {'jaccount': 'test_jaccount', 'task_id': 1}
        response = self.client.post("/index/delete_task/", data=task_data)
        self.assertEqual(response.status_code, 200)

    def test_done_task(self):
        task_data = {'jaccount': 'test_jaccount', 'task_id': 1, 'task_done': 'true'}
        response = self.client.post("/index/delete_task/", data=task_data)
        self.assertEqual(response.status_code, 200)

    # 改好了重写
    # def test_aidraw(self):
    #     data = {'prompt': 'test', 'page_size': (1440, 1024), 'need_highres': False, 'jaccount': 'test_jaccount'}
    #     response = self.client.post("/index/aidraw/", data=data)
    #     self.assertEqual(response.status_code, 200)

    def test_color_wallpaper(self):
        css = {'jaccount': 'test_jaccount', "css": "css_text"}
        response = self.client.post("/index/color_wallpaper/", data=css)
        self.assertEqual(response.status_code, 200)
