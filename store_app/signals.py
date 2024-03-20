from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import WebsiteTemplate
import json
from django.core.serializers import deserialize
from django.contrib.auth import get_user_model
User = get_user_model()
from django.conf import settings
import os

@receiver(post_save, sender=User)
def create_website_template_for_new_user(sender, instance, created, **kwargs):
    if created:
        fixtures_path = 'store_app/fixtures/templates.json'
        with open(fixtures_path, 'r') as file:
            fixtures = json.load(file)
            for deserialized_obj in deserialize('json', json.dumps(fixtures)):
                if isinstance(deserialized_obj.object, WebsiteTemplate):
                    website_template = deserialized_obj.object
                    website_template.user = instance
                    website_template.save()
