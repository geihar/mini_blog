import factory
from factory.fuzzy import FuzzyChoice

from blog.models import Tag, Post
from users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("word")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")


class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tag

    name = factory.Faker("word")


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker("word")
    text = factory.Faker("text", max_nb_chars=1000)
    author = factory.SubFactory(UserFactory)
    published = FuzzyChoice([True, False])
    img = factory.django.ImageField(
        width=200, height=200, color=FuzzyChoice(["blue", "yellow", "green", "orange"])
    )

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for tag in extracted:
                self.tags.add(tag)
