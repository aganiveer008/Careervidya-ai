from django.db import migrations, models
import django.db.models.deletion

def fix_empty_category(apps, schema_editor):
    # Now column allows NULL → safe to convert
    schema_editor.execute("""
        UPDATE accounts_skill
        SET category = NULL
        WHERE category = '';
    """)

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_skill_category'),
    ]

    operations = [
        # ✅ STEP 1: make field nullable first
        migrations.AlterField(
            model_name='skill',
            name='category',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),

        # ✅ STEP 2: clean data
        migrations.RunPython(fix_empty_category),

        # ✅ STEP 3: convert to ForeignKey
        migrations.AlterField(
            model_name='skill',
            name='category',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='accounts.category'
            ),
        ),
    ]