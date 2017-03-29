from __future__ import unicode_literals

from django.db import models
from ..login_app.models import Users
# Create your models here.
class Quotes(models.Model):
	creator = models.TextField()
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(Users, related_name='all_users')

class Favorites(models.Model):
	quote = models.ForeignKey(Quotes, related_name='fav_quotes')
	user = models.ForeignKey(Users, related_name='fav_users')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

