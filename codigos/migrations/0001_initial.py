# Generated by Django 4.2.7 on 2023-11-12 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conteudo', models.TextField()),
                ('horario_envio', models.TimeField()),
                ('dia_envio', models.DateField()),
                ('ultima', models.BooleanField(default=False)),
                ('mensagem_adicional', models.TextField(blank=True, null=True)),
                ('audio_url', models.FileField(blank=True, null=True, upload_to='audios/')),
            ],
        ),
    ]
