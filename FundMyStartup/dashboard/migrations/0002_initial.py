from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('title', models.CharField(max_length=100)),
                ('Equity', models.TextField()),
                ('funding',models.DecimalField(max_digits=10, decimal_places=2)),
                ('Sales',models.DecimalField(max_digits=10, decimal_places=2)),
                ( 'profit',models.DecimalField(max_digits=10, decimal_places=2)),
                ('entrepreneur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('debts',models.DecimalField(max_digits=10, decimal_places=2)),

            ]
        )
    ]


