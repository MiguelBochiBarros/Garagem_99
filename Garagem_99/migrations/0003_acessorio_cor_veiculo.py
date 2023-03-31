# Generated by Django 4.1.7 on 2023-03-31 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Garagem_99', '0002_marca'),
    ]

    operations = [
        migrations.CreateModel(
            name='acessorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField(default=0, null=True)),
                ('preco', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Garagem_99.categoria')),
                ('cor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Garagem_99.cor')),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Garagem_99.marca')),
            ],
        ),
    ]