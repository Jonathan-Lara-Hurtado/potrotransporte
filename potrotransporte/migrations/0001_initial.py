# Generated by Django 2.2 on 2020-06-02 19:08

import datetime
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
            name='Operador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Licencia', models.CharField(default='', max_length=20)),
                ('telefono', models.CharField(default='', max_length=15)),
                ('Dirrecion', models.CharField(default='', max_length=20)),
                ('PKUsuario', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreRuta', models.CharField(default='', max_length=20)),
                ('Horario', models.CharField(default='', max_length=30)),
                ('Latitud', models.FloatField()),
                ('Longitud', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoMembresias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=40)),
                ('costo', models.IntegerField()),
                ('duracion', models.CharField(choices=[('S', 'Semanal'), ('M', 'Mensual'), ('C', 'Trimestral')], default='C', max_length=1)),
                ('costoPorDuracion', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Transporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=10)),
                ('Tipo', models.CharField(max_length=10)),
                ('Matricula', models.CharField(max_length=10)),
                ('OperadorFK', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='potrotransporte.Operador')),
            ],
        ),
        migrations.CreateModel(
            name='RutaReserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaRegistro', models.DateField(default=datetime.date.today, verbose_name='Fecha')),
                ('estadoReserva', models.CharField(choices=[('P', 'Reservado'), ('C', 'Cancelado')], default='C', max_length=1)),
                ('turno', models.CharField(choices=[('M', 'Matutino'), ('V', 'Vespertino')], default='M', max_length=1)),
                ('RutaFk', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='potrotransporte.Ruta')),
                ('UsuarioFK', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='ruta',
            name='TransporteFK',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='potrotransporte.Transporte'),
        ),
        migrations.CreateModel(
            name='Membresia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FechaCreacion', models.DateField(default=datetime.date.today, verbose_name='Fecha creacion')),
                ('EstadoPago', models.CharField(choices=[('P', 'Pagado'), ('C', 'Cancelado'), ('E', 'Pendiente'), ('T', 'Cancelado Tiempo'), ('W', 'Expiro Membresia')], default='E', max_length=1)),
                ('MembresiaFk', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='potrotransporte.TipoMembresias')),
                ('UsuarioFk', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DetallePagoMembresia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FechaInicio', models.DateField(default=datetime.date.today, verbose_name='Fecha Inicio')),
                ('FechaTerminacion', models.DateField(default=datetime.date.today, verbose_name='Fecha Terminacion')),
                ('FechaAprobacion', models.DateField(default=datetime.date.today, verbose_name='Fecha Aprobacion')),
                ('MembresiaFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='potrotransporte.Membresia')),
                ('administrativoFK', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DatosPersonales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NumeroDeCuenta', models.CharField(default='', max_length=20)),
                ('Telefono', models.CharField(default='', max_length=20)),
                ('TelefonoAlternativo', models.CharField(default='', max_length=20)),
                ('TipoSangre', models.CharField(default='', max_length=4)),
                ('Alergias', models.CharField(default='', max_length=30)),
                ('DatoPersonalFk', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Avisos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('mensaje', models.CharField(max_length=30)),
                ('fechaCreacion', models.DateField(default=datetime.date.today, verbose_name='Fecha')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ida', models.BooleanField(default=False)),
                ('vuelta', models.BooleanField(default=False)),
                ('fechaDeIda', models.DateTimeField(default=datetime.date(2020, 6, 3), verbose_name='Fecha')),
                ('fechaVuelta', models.DateTimeField(default=datetime.date(2020, 6, 3), verbose_name='Fecha')),
                ('ReservaFK', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='potrotransporte.RutaReserva')),
            ],
        ),
    ]
