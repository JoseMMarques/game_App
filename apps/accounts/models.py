from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
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


class User(AbstractBaseUser, PermissionsMixin):
    """Um modelo base para todos os intervenientes da escola"""

    TYPE_CHOICES =(
        ("TEACHER", "Professor"),
        ("STUDENT", "Estudante"),
        ("EMPLOYEE", "Funcionário")
    )
    type = models.CharField(
        'Tipo',
        max_length=100,
        choices=TYPE_CHOICES,
        default='TEACHER'
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
    phone = models.CharField(
        'Telemóvel',
        max_length=12,
        blank=True,
    )
    address = models.TextField(
        'Morada',
        blank=True,
    )

    # required fields
    last_login = models.DateTimeField(
        'Último acesso',
        auto_now_add=True
    )
    created = models.DateTimeField(
        'Criado em',
        auto_now_add=True
    )
    modified = models.DateTimeField(
        'modificado em',
        auto_now=True
    )
    is_admin = models.BooleanField(
        'Administrador',
        default=False
    )
    is_staff = models.BooleanField(
        'Staff',
        default=False
    )
    is_active = models.BooleanField(
        'Conta ativa',
        default=False
    )
    is_superadmin = models.BooleanField(
        'Super Administrador',
        default=False
    )
    is_game = models.BooleanField(
        'Membro GAME',
        default=False
    )

    class Meta:
        """options (metadata) to the field"""
        verbose_name = "Utilizador"
        verbose_name_plural = "Utilizadores"
        ordering = ['name']

    def __str__(self):
        """Return the str.name fom the object"""
        return self.name
    def get_age(self):
        """return the age of the user from the birth_date"""
        today = date.today()
        if self.birth_date:
            return today.year - self.birth_date.year - (
                    (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
            )

    def get_first_name(self):
        """Get the user first name"""
        return str(self).split(" ")[0]

    def get_last_name(self):
        """get the user last name"""
        return str(self).split(" ")[-1]

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    objects = UserManager()


class Teacher(models.Model):
    """Um modelo para os professores da escola"""

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
    school_class_dt = models.OneToOneField(
        'school_structure.SchoolClass',
        verbose_name='Direção de Turma',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    subjects = models.CharField(
        'Disciplinas',
        max_length=200,
    )
    is_dt = models.BooleanField(
        'DT',
        default=False
    )

    class Meta:
        verbose_name = "Professor"
        verbose_name_plural = "Professores"
        ordering = ('user',)

    def __str__(self):
        """Return the str.name fom the object"""
        return self.user.name


class Student(models.Model):
    """Um modelo para os alunos da escola"""

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
    school_class = models.ForeignKey(
        'school_structure.SchoolClass',
        verbose_name='Turma',
        on_delete=models.CASCADE,
    )
    class_number = models.PositiveSmallIntegerField(
        'Número de turma',
        blank=False,
    )
    name_ee = models.CharField(
        'Encarregado de Educação',
        max_length=150,
        blank=True,
    )
    email_ee = models.EmailField(
        'Email do EE',
        max_length=254,
        blank=True,
    )
    phone_ee = models.CharField(
        'Telemóvel',
        max_length=12,
        blank=True,
    )

    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"
        ordering = ('name',)

    def __str__(self):
        """Return the str.name fom the object"""
        return self.user.name


class Employee(models.Model):
    """Um modelo para os funcionários da escola"""

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
    role = models.CharField(
        'Função',
        max_length=150,
        blank=True,
    )
    workplace = models.CharField(
        'Local de Trabalho',
        max_length=150,
        blank=True,
    )

    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"
        ordering = ('name',)

    def __str__(self):
        """Return the str.name fom the object"""
        return self.user.name
