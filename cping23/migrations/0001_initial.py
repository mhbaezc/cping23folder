# Generated by Django 3.2.19 on 2023-05-11 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TablaPosiciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntos', models.PositiveIntegerField(default=0)),
                ('partidos_jugados', models.PositiveIntegerField(default=0)),
                ('partidos_ganados', models.PositiveIntegerField(default=0)),
                ('partidos_empatados', models.PositiveIntegerField(default=0)),
                ('partidos_perdidos', models.PositiveIntegerField(default=0)),
                ('goles_favor', models.PositiveIntegerField(default=0)),
                ('goles_contra', models.PositiveIntegerField(default=0)),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cping23.equipo')),
            ],
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goles_local', models.PositiveIntegerField()),
                ('goles_visitante', models.PositiveIntegerField()),
                ('equipo_local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partidos_local', to='cping23.equipo')),
                ('equipo_visitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partidos_visitante', to='cping23.equipo')),
            ],
        ),
    ]
