from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import date


class UserManager(BaseUserManager):
    def create_user(self, name, email, password=None):
        if not email:
            raise ValueError('Utilizador tem que ter email!')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            name=name,
            password=password,

        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    class Types(models.TextChoices):
        ALUNO = "ALUNO", "Aluno"
        PROFESSOR = "PROFESSOR", "Professor"

    type = models.CharField(
        'Tipo',
        max_length=50,
        choices=Types.choices,
        default=Types.PROFESSOR
    )

    name = models.CharField(
        'Nome',
        max_length=254,
    )
    birth_date = models.DateField(
        'Data de nascimento',
        blank=True,
        null=True,
    )
    SEX_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    sex = models.CharField(
        'Sexo',
        choices=SEX_CHOICES,
        max_length=100,
        default='F',
    )
    email = models.EmailField(
        'e-mail',
        max_length=254,
        unique=True,
    )
    phone_number = models.CharField(
        'Telemóvel',
        max_length=12,
        blank=True,
    )
    address = models.TextField(
        'Morada',
        blank=True,
    )

    # required fields
    date_joined = models.DateTimeField(
        auto_now_add=True
    )
    last_login = models.DateTimeField(
        auto_now_add=True
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    modified = models.DateTimeField(
        auto_now=True
    )
    is_admin = models.BooleanField(
        default=False
    )
    is_staff = models.BooleanField(
        default=False
    )
    is_active = models.BooleanField(
        default=False
    )
    is_superadmin = models.BooleanField(
        default=False
    )

    class Meta:
        """options (metadata) to the field"""
        verbose_name = "Utilizador"
        verbose_name_plural = "Utilizadores"
        ordering = ['name']

    def get_age(self):
        """return the age of the user from the birth_date"""
        today = date.today()
        if self.birth_date:
            return today.year - self.birth_date.year - (
                    (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
            )

    def __str__(self):
        """Return the str.name fom the object"""
        return self.name

    def get_first_name(self):
        """Get the user first name"""
        return str(self).split(" ")[0]

    def get_last_name(self):
        """get the user last name"""
        return str(self).spit(" ")[-1]

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    objects = UserManager()


class Professor(User):
    class Meta:
        proxy = True


class Aluno(User):
    class Meta:
        proxy = True