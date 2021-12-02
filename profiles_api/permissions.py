from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS: #If the method is a safe method (ex. get) function returns true
            return True
        #else
        return obj.id == request.user.id # if the object being edited is equal to the requester, it returns true
