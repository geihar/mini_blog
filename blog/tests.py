from django.test import TestCase
from django.urls import reverse

from blog.models import Tag, Post
from blog.factories import TagFactory, UserFactory, PostFactory


class TagTest(TestCase):
    """Tests for Tag model."""

    def setUp(self):

        self.tag_1 = TagFactory(name="django")
        self.tag_2 = TagFactory()

    def test_tag_str(self):

        django = Tag.objects.get(name="django")
        not_django = Tag.objects.get(id=self.tag_2.id)

        self.assertEqual(str(django), "django")
        self.assertNotEqual(str(not_django), "django")

    def test_tag_url(self):

        django = Tag.objects.get(name="django")

        self.assertEqual("/django/", django.get_absolute_url())


#
class PostTest(TestCase):
    """Tests for Post model."""

    def setUp(self):
        self.post_1 = PostFactory(published=False)
        self.post_2 = PostFactory()

    def test_post_str(self):

        post_1 = Post.objects.get(id=self.post_1.id)
        post_2 = Post.objects.get(id=self.post_2.id)

        self.assertEqual(str(post_1), self.post_1.title)
        self.assertNotEqual(str(post_2), self.post_1.id)

    def test_post_url(self):

        django = Post.objects.get(id=self.post_1.id)

        self.assertEqual(f"/post/{django.id}/", django.get_absolute_url())

    def test_post_published(self):

        post = Post.objects.get(title=self.post_1.title)

        self.post_1.published = True
        self.post_1.save()
        self.post_1.refresh_from_db()
        self.assertNotEquals(post.pub_date, self.post_1.pub_date)


class PostListViewTests(TestCase):
    """Tests for Post list view."""

    def setUp(self):

        self.user_1 = UserFactory()
        self.user_2 = UserFactory()

        for i in range(15):

            user = self.user_1 if i % 2 == 0 else self.user_2
            published = True if i % 2 == 0 else False

            PostFactory(published=published, author=user)

    def test_get_index(self):

        self.url = reverse("index")
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"], True)
        self.assertTrue(len(response.context["posts"]), 10)
        self.assertTemplateUsed(response, "blog/index.html")


class PostDetailViewTests(TestCase):
    """Tests for Post detail view."""

    def setUp(self):

        self.post_1 = PostFactory()

    def test_get_post_detail(self):

        self.url = reverse("post_detail", kwargs={"pk": self.post_1.pk})
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post_detail.html")


class TagSearchViewTests(TestCase):
    """Tests for Tag search view."""

    def setUp(self):

        self.user_1 = UserFactory()
        self.user_2 = UserFactory()

        for i in range(10):
            user = self.user_1 if i % 2 == 0 else self.user_2
            published = True if i % 2 == 0 else False
            post = PostFactory(published=published, author=user, tags=(self.tag_1,))
            print(post.tags)

    # def test_get_post_from_tag(self):
    #
    #     self.url = reverse("post_tag", kwargs={"slug": self.tag_1.name})
    #     response = self.client.get(self.url)
    #
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTrue(len(response.context["posts"]), 5)
    #     self.assertTemplateUsed(response, "blog/index.html")
