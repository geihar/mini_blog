from django.test import TestCase
from django.urls import reverse

from users.models import User
from blog.models import Tag, Post


class TagTest(TestCase):
    """Tests for Tag model."""

    def setUp(self):
        Tag.objects.create(name='django')
        Tag.objects.create(name='js')


    def test_tag_str(self):
        django = Tag.objects.get(name='django')
        js = Tag.objects.get(name='js')

        self.assertEqual(str(django), 'django')
        self.assertNotEqual(str(js), 'js22')

    def test_tag_url(self):

        django = Tag.objects.get(name='django')
        self.assertEqual("/django/", django.get_absolute_url())


class PostTest(TestCase):
    """Tests for Post model."""

    def setUp(self):
        self.tag_1 = Tag.objects.create(name='django')
        self.tag_2 = Tag.objects.create(name='js')
        self.user_1 = User.objects.create(username='Casper', first_name='Tom', last_name='Adams',)

        self.post_1 = Post.objects.create(
            title='about django',
            text='text',
            published=False,
            author=self.user_1,
            )
        self.post_1.tags.add(self.tag_1, self.tag_2)

        self.post_2 = Post.objects.create(
            title='about js',
            text='text',
            published=False,
            author=self.user_1,
            )
        self.post_1.tags.add(self.tag_2, )


    def test_post_str(self):
        django = Post.objects.get(title='about django')
        js = Post.objects.get(title='about js')

        self.assertEqual(str(django), 'about django')
        self.assertNotEqual(str(js), 'js22')

    def test_post_url(self):

        django = Post.objects.get(title='about django')
        self.assertEqual(f"/post/{django.id}/", django.get_absolute_url())

    def test_post_published(self):
        post = Post.objects.get(title=self.post_1.title)

        self.post_1.published = True
        self.post_1.save()
        self.post_1.refresh_from_db()
        self.assertNotEqual(post.pub_date, self.post_1.pub_date)


class PostListViewTests(TestCase):
    """Tests for Post list view."""

    def test_get_index(self):

        self.url = reverse('index')
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)


class PostDetailViewTests(TestCase):
    """Tests for Post detail view."""

    def setUp(self):
        self.tag_1 = Tag.objects.create(name='django')
        self.tag_2 = Tag.objects.create(name='js')
        self.user_1 = User.objects.create(username='Casper', first_name='Tom',
                                          last_name='Adams', )

        self.post_1 = Post.objects.create(
            title='about django',
            text='text',
            published=False,
            author=self.user_1,
        )
        self.post_1.tags.add(self.tag_1, self.tag_2)

    def test_get_post_detail(self):
        self.url = reverse('post_detail', kwargs={'pk':self.post_1.pk})
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)


class TagSearchViewTests(TestCase):
    """Tests for Tag search view."""

    def setUp(self):
        self.tag_1 = Tag.objects.create(name='django')
        self.tag_2 = Tag.objects.create(name='js')
        self.user_1 = User.objects.create(username='Casper', first_name='Tom',
                                          last_name='Adams', )

        self.post_1 = Post.objects.create(
            title='about django',
            text='text',
            published=False,
            author=self.user_1,
        )
        self.post_1.tags.add(self.tag_1, self.tag_2)

    def test_get_post_from_tag(self):
        self.url = reverse('post_tag', kwargs={'slug':self.tag_1.name})
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)