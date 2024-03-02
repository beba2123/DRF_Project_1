from rest_framework  import permissions

from .permissions  import IsStaffEditorPermision

class StaffEditorPermissionMixin():
     permission_classes = [permissions.IsAdminUser, IsStaffEditorPermision]