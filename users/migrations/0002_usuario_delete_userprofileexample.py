# Generated by Django 4.2.3 on 2024-12-01 20:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('academia', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=12)),
                ('endereço', models.CharField(max_length=150)),
                ('aniversario', models.DateField()),
                ('ativo', models.BooleanField(default=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('ultima_atualizacao', models.DateTimeField(auto_now=True)),
                ('academia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academia.academia')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
        ),
        migrations.DeleteModel(
            name='UserProfileExample',
        ),
    ]
