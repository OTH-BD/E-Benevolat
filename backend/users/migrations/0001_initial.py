# Generated by Django 4.1 on 2022-08-29 22:30

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('est_association', models.BooleanField(default=False)),
                ('est_benevolat', models.BooleanField(default=False)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('password1', models.CharField(max_length=20, null=True)),
                ('password2', models.CharField(max_length=20, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ProfileAssociation',
            fields=[
                ('logo', models.ImageField(blank=True, null=True, upload_to='uploads/images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='association', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('nom_association', models.CharField(max_length=50)),
                ('nom_complet', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=20, null=True)),
                ('description', models.TextField(max_length=200, null=True)),
                ('adresse', models.TextField(blank=True, max_length=100, null=True)),
                ('ville', models.CharField(max_length=30, null=True)),
                ('nbr_membre_bureau', models.CharField(choices=[('- Choisir une valeur -', '- Choisir une valeur -'), ('de 0 a 5', 'de 0 a 5'), ('de 5 a 10', 'de 5 a 10'), ('de 10 a plus', 'de 10 a plus')], default='- Choisir une valeur -', max_length=25)),
                ('nbr_beneficiere', models.CharField(choices=[('- Choisir une valeur -', '- Choisir une valeur -'), ('0 a 50', '0 a 50'), ('50 a  plus', '50 a  plus')], default='- Choisir une valeur -', max_length=25)),
                ('siteweb', models.CharField(max_length=40, null=True)),
                ('activiter_prefere', models.CharField(choices=[('Sport', 'Sport'), ('Santer', 'Santer'), ('Education', 'Education'), ('Enseignement', 'Enseignement'), ('Entreprenariat', 'Entreprenariat'), ('Protection de lenvironnement', 'Protection de lenvironnement'), ('Handicap', 'Handicap'), ('Droits de la femme', 'Droits de la femme'), ('Autres Domaine', 'Autres Domaine')], max_length=100)),
                ('accepter_par_admin', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileBenevole',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='benevole', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('photo_profile', models.ImageField(blank=True, null=True, upload_to='uploads/images')),
                ('nomComplet', models.CharField(max_length=50, null=True)),
                ('telephone', models.CharField(max_length=20, null=True)),
                ('adresse', models.CharField(max_length=100, null=True)),
                ('genre', models.CharField(choices=[('--Aucun--', '--Aucun--'), ('FEMME', 'FEMME'), ('HOMME', 'HOMME')], default='--Aucun--', max_length=100)),
                ('ville', models.CharField(choices=[('--Aucun--', '--Aucun--'), ('Agadir', 'Agadir'), ('Casablanca', 'Casablanca'), ('Essaouira', 'Essaouira'), ('Fes', 'Fes'), ('Marrakech', 'Marrakech'), ('Meknes', 'Meknes'), ('Oujda', 'Oujda'), ('Rabat', 'Rabat'), ('Tanger', 'Tanger'), ('Tetouan', 'Tetouan')], default='--Aucun--', max_length=20)),
                ('date_naissance', models.DateTimeField(default=django.utils.timezone.now)),
                ('cin', models.CharField(max_length=12, null=True)),
                ('domaine_experience', models.TextField(null=True)),
                ('biographie', models.TextField(null=True)),
                ('activiter_prefere', models.CharField(choices=[('Cadre', 'Cadre'), ('Salarié', 'Salarié'), ('Sans emploi', 'Sans emploi'), ('Commercent', 'Commercent'), ('Etudiant', 'Etudiant'), ('Autre', 'Autre')], max_length=100)),
            ],
        ),
    ]