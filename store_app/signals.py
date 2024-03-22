# from django.dispatch import receiver
# from django.core.management import call_command
# from django.db.models.signals import post_migrate

# @receiver(post_save, sender=User)
# def create_website_template_for_new_user(sender, instance, created, **kwargs):
#     if created:
#         fixtures_path = 'store_app/fixtures/templates.json'
#         with open(fixtures_path, 'r') as file:
#             fixtures = json.load(file)
#             for deserialized_obj in deserialize('json', json.dumps(fixtures)):
#                 if isinstance(deserialized_obj.object, WebsiteTemplate):
#                     website_template = deserialized_obj.object
#                     website_template.user = instance
#                     website_template.save()



# @receiver(post_migrate)
# def load_fixtures(sender, **kwargs):
#     call_command("loaddata", "temp.json", app_label="store_app")