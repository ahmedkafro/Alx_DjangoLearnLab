## Groups and Permissions Setup

This project uses Django groups and custom permissions to control access.

### Custom Permissions
Defined in the Book model:
- can_view
- can_create
- can_edit
- can_delete

### Groups
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: all permissions

### Enforcement
Views are protected using Django's `@permission_required` decorator.

Example:
@permission_required("bookshelf.can_edit", raise_exception=True)
# Alx_DjangoLearnLab
