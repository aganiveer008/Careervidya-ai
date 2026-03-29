from django.db import migrations

def fix_existing_skills(apps, schema_editor):
    Skill = apps.get_model('accounts', 'Skill')
    for skill in Skill.objects.all():
        if skill.category_id == '' or skill.category is None:
            skill.category = None
            skill.save()

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_skill_category'),
    ]

    operations = [
        migrations.RunPython(fix_existing_skills),
    ]