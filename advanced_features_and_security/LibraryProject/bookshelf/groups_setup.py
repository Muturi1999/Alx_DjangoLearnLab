# Create this file in your project directory, and run it with:
# python manage.py shell < groups_setup.py

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book

# Get the content type for the Book model
book_content_type = ContentType.objects.get_for_model(Book)

# Get all the custom permissions for the Book model
can_view_permission = Permission.objects.get(
    codename='can_view',
    content_type=book_content_type,
)
can_create_permission = Permission.objects.get(
    codename='can_create',
    content_type=book_content_type,
)
can_edit_permission = Permission.objects.get(
    codename='can_edit',
    content_type=book_content_type,
)
can_delete_permission = Permission.objects.get(
    codename='can_delete',
    content_type=book_content_type,
)

# Create the Viewers group
viewers_group, created = Group.objects.get_or_create(name='Viewers')
if created:
    viewers_group.permissions.add(can_view_permission)
    print("Created Viewers group with can_view permission")
else:
    print("Viewers group already exists")

# Create the Editors group
editors_group, created = Group.objects.get_or_create(name='Editors')
if created:
    editors_group.permissions.add(can_view_permission, can_create_permission, can_edit_permission)
    print("Created Editors group with can_view, can_create, and can_edit permissions")
else:
    print("Editors group already exists")

# Create the Admins group
admins_group, created = Group.objects.get_or_create(name='Admins')
if created:
    admins_group.permissions.add(
        can_view_permission, 
        can_create_permission, 
        can_edit_permission, 
        can_delete_permission
    )
    print("Created Admins group with all book permissions")
else:
    print("Admins group already exists")

print("Groups and permissions setup completed")