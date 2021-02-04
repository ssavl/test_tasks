# Generated by Django 3.2a1 on 2021-02-04 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollquestion',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='polls.poll'),
        ),
        migrations.AlterField(
            model_name='pollquestionchoice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='polls.pollquestion'),
        ),
    ]