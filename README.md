# Proyecto Final: Ramirez (Python + Django)

Proyecto final del curso de Python y Django en modalidad Flex de CoderHouse.

## Consigna

En forma individual, crearás una aplicación web estilo blog programada en [Python](https://www.python.org/) y [Django](https://www.djangoproject.com/). Esta web tendrá:

- [x] **admin** (_admin.site.urls_).
- [x] **perfiles** (_users profiles_).
- [x] **registro** (_users_).
- [x] **páginas** (_CRUD_).
- [x] **formularios** (_forms_).

## Navegación

- [x] Contar con algún acceso visible (_link_) a la vista (_view_) de **"Acerca de mí"** (_About me_) donde se contará acerca del dueño de la página manejado en el **route** _about/_ (_url_).

- [x] Contar con algún acceso visible (_link_) a la vista (_view_) de **blogs** que debe alojarse en el **route** _pages/_.

- [x] Cada **blog** en la página de **blogs** debe ser un botón **"Leer más"** que lleve a un enlace (_link_) a la vista (_view_) de **detalle** de la **page**. Al clickear en **"Leer más"** debe navegar al detalle de la **page** mediante un **route** _pages/<uuid:page_code>/_.

- [x] Si no existe ninguna página (_blog_) mostrar, debe mostrar un **"No hay páginas aún"**.

- [x] Para editar (_update_) o borrar (_delete_) pages (_blogs_) debes estar logueado (_@login_required_).

## Componentes recomendados para el proyecto

- [x] NavBar

  - [x] Home (_landing page_)
  - [x] Pages (_blogs_)
    - [x] GET pages (_view all pages_)
    - [x] **C**REATE page (_Add new post_)
    - [x] **R**EAD page (_Show post detail_)
    - [x] **U**PDATE page (_Edit post_)
    - [x] **D**ELETE page (_Delete post_)
  - [x] About (_About me_)
  - [x] Login (_Iniciar sesión_)
  - [x] Logout (_Cerrar sesión_)
  - [x] Signup (_CREATE user_)
  - [x] Profile (_User profile_)
    - [x] READ profile (_Show user profile_)
    - [x] UPDATE profile (_Edit user profile_)

## Requisitos base

Los siguientes requisitos serán parte de los criterios de evaluación para aprobar el proyecto. Si bien se menciona un modelo principal (por ejemplo, un blog), podés cambiar la temática siempre y cuando se cumplan todos los requisitos establecidos.

- [x] Entrega individual en un repositorio de GitHub.
- [x] **README.md** detallando el proyecto.
- [ ] Video de un máximo de 10 minutos (freecam, OBS, filmora) que muestre el sitio web y sus funcionalidades (con o sin audio).
- [x] No agregar la base de datos (**db.sqlite3**) en la entrega. Debería estar en el **.gitignore**.
- [x] Usar herencia de templates. En el template **base** implementar la etiqueta `<nav>` de navegación que contenga los accesos que se crean necesarios para su sitio (_NavBar_).
- [x] En el **.gitignore**:

  - [x] pycache
  - [x] db.sqlite3 (no compartir la información de tu base de datos)
  - [x] media folder (las imágenes son archivos muy pesados que no es recomendable tener en el repositorio)
  - [x] .venv

- [x] Las imágenes que sean parte del código del proyecto deberían guardarse en la carpeta **static**.
- [x] Existencia del archivo **requirements.txt** actualizado.
- [x] Tener en cuenta que al manejar **forms** con imágenes hay que adaptar el template y la vista, no solo el modelo y el formulario.
- [x] Uso de al menos 2 Vistas Basadas en Clases (CBV).
- [x] Uso de al menos un **mixin** en una **CBV** y un decorador en una **view** común.
- [x] Una vista (view) de **inicio** / **home** (_landing page_).
- [x] Acceso a una vista (view) **"Acerca de mí"** / **"About"**.
- [x] Crear un modelo principal (_Blog / Post / Auto / Vendedor / Docente / etc_) que contenga los siguiente campos como mínimo: **2 Charfield**, 1 de texto enriquecido (**ckeditor**), 1 campo de imagen, 1 de fecha.
- [x] Vista de listado de los objetos del modelo principal (modelo a elección). En la cual cada objeto mostrará solo algunos de sus datos.
- [x] Mensaje que da aviso en caso de no haber ningún objeto creado o al utilizar el buscador no encontrar tampoco algún objeto.
- [x] Poder acceder a una vista que muestre el detalle de el objeto seleccionado.
- [x] Poder acceder a una vista de creación (CREATE), una de edición (UPDATE) y una de borrado de objetos (DELETE).
- [x] Registrar en el apartado de **admin** todos los modelos creados.
- [x] Tener una **app** (accounts / cuentas / etc) para el manejo de todas las vistas relacionadas al usuario / autenticación.
- [x] Desarrollar las vistas para un **login**, un **logout** y un **registro** para usuarios. En este último se debe solicitar: **username**, **email** y **password**.
- [x] Crear una vista de perfil donde se muestran los datos del usuario:

  - [x] Nombre
  - [x] Apellido
  - [x] Email
  - [x] Avatar
  - [x] Biografia / link / fecha de cumpleanios / etc.

- [x] Desde el perfil, crear un acceso a una vista de edición de estos datos. Agregar el cambio de password.
- [x] Utilizar Python puro para el proyecto final (se espera el uso de Django).

## Módulos estándar (internos)

- [os](https://docs.python.org/3/library/os.html): este módulo ofrece una forma portátil de utilizar funcionalidades dependientes del sistema operativo.

<!-- - [sys](https://docs.python.org/3/library/sys.html): este módulo proporciona acceso a algunas variables utilizadas o mantenidas por el intérprete y a funciones que interactúan estrechamente con él. Siempre está disponible. A menos que se indique explícitamente lo contrario, todas las variables son de solo lectura. -->

<!-- - [time](https://docs.python.org/3/library/time.html): -->

## Paquetes de terceros (externos)

- [Django](https://www.djangoproject.com/): es un framework web de alto nivel para [Python](https://www.python.org/) que fomenta el desarrollo rápido y un diseño limpio y pragmático. Creado por desarrolladores con experiencia, se encarga de gran parte del trabajo tedioso del desarrollo web, por lo que puedes concentrarte en escribir tu aplicación sin necesidad de reinventar la rueda. Es gratuito y de código abierto.

- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/index.html): es una librería de Django que ayuda a hacer formularios más bonitos y más fáciles de maquetar.

- [crispy-tailwind](https://github.com/django-crispy-forms/crispy-tailwind): es una extensión para `django-crispy-forms`. Hace que `crispy-forms` genere formularios ya adaptados a TailwindCSS.

- [Pillow](https://pillow.readthedocs.io/en/stable/): es una librería de [Python](https://www.python.org/) para el manejo de imágenes.

## Routes

- **Home page**: `/`
- **Administration**: `/admin`
- **About**: `/about`
- **Soulcalibur Music**: `/music/soulcalibur`
- **Soulcalibur Song List**: `/music/soulcalibur/song/list`
- **Soulcalibur Song Create**: `/music/soulcalibur/song/create`
- **Soulcalibur Song Detail**: `/music/soulcalibur/song/detail/<uuid:song_code>`
- **Soulcalibur Song Update**: `/music/soulcalibur/song/update/<uuid:song_code>`
- **Soulcalibur Song Delete**: `/music/soulcalibur/song/delete/<uuid:song_code>`
- **Soulcalibur Album List**: `/music/soulcalibur/album/list`
- **Soulcalibur Album Create**: `/music/soulcalibur/album/create`
- **User Login**: `/user/login`
- **User Logout**: `/user/logout`
- **User Signup**: `/user/signup`
- **User Profile**: `/user/detail`
- **User Update**: `/user/update`
- **User Advance Password Change**: `/user/password_change`
- **User Advance Password Change Done**: `/user/password_change/done`

Manejo de errores: `400, 403, 404, 500`

## Entorno Virtual

- **Create**: `python -m venv .venv`
- **Activate**:
  - 🗔 `.venv\Scripts\activate`
  - 🍏/🐧 `source .venv/bin/activate`
- **Deactivate**: `deactivate`
- **Install requirements**: `pip install -r requirements.txt`

## Comandos

- **Run server**: `python manage.py runserver`
- **Make migrations**: `python manage.py makemigrations`
- **Migrate**: `python manage.py migrate`
- **Superuser**: `python manage.py createsuperuser`
<!-- - **Run tests**: `python manage.py test` -->
