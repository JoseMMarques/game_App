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

    class Types(models.TextChoices):
        TEACHER = "TEACHER", "Professor"
        STUDENT = "STUDENT", "Estudante"
        EMPLOYEE = "EMPLOYEE", "Funcionário"

    type = models.CharField(
        'Tipo',
        max_length=50,
        choices=Types.choices,
        default=Types.TEACHER
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
        'Último login',
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
        return str(self).split(" ")[-1]

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def save(self, *args, **kwargs):
        if not self.id:
            self.type = self.base_type
        return super().save(*args, **kwargs)

    objects = UserManager()


class TeacherManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.TEACHER)


class StudentManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.STUDENT)


class EmployeeManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.EMPLOYEE)


class Teacher(User):
    base_type = User.Types.TEACHER
    objects = TeacherManager()

    @property
    def more(self):
        return self.teachermore

    class Meta:
        proxy = True
        verbose_name = "Professor"
        verbose_name_plural = "Professores"
        ordering = ('name',)


class Student(User):
    base_type = User.Types.STUDENT
    objects = StudentManager()

    class Meta:
        proxy = True
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"
        ordering = ('name',)


class Employee(User):
    base_type = User.Types.EMPLOYEE
    objects = EmployeeManager()

    class Meta:
        proxy = True
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"
        ordering = ('name',)


class SchoolClass(models.Model):
    """Modelo para as turmas"""

    name = models.CharField(
        'Designação da turma',
        max_length=20,
    )
    school_year = models.CharField(
        'Ano Letivo',
        max_length=20,
    )
    school = models.CharField(
        'Escola',
        max_length=20,
    )
    teacher_dt = models.OneToOneField(
        Teacher,
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField(
        'Criado em',
        auto_now_add=True
    )
    modified = models.DateTimeField(
        'modificado em',
        auto_now=True
    )

    def __str__(self):
        """Return the str.name fom the object"""
        return self.name

    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"
        ordering = ('name',)


class TeacherMore(models.Model):
    user = models.OneToOneField(
        Teacher,
        on_delete=models.CASCADE
    )
    school_class_dt = models.OneToOneField(
        SchoolClass,
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

    def __str__(self):
        """Return the str.name fom the object"""
        return self.user.name

    class Meta:
        verbose_name = "Professor"
        verbose_name_plural = "Professores"
        ordering = ('user',)

