from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# sqlite 做为开发使用的数据
# postgresql 作为发行版本的数据库
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # 得到完整的url字符串
    # class based views
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})



# Step 1: run migration in order to update the database with any changes
'''
Step 2:
E:\python_DjangoProject\django_project>python manage.py sqlmigrate blog 0001
BEGIN;
--
-- Create model Post
--
CREATE TABLE "blog_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(100) NOT NULL, "content" text NOT NULL, "date_posted" datetime NOT NULL, "author_id" integer NOT NULL REFE
RENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "blog_post_author_id_dd7a8485" ON "blog_post" ("author_id");
COMMIT;
'''
# Step 3: python manage.py migrate
# Summary : if you use migration you won't need to handle mass of sql data with migration it will make change for us.
