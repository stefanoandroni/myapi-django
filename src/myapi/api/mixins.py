from articles.models import Article
from comments.models import Comment

# Todo: generalize mixins related to Article and Comment

# - - - - - - - - - - - - - - Article - - - - - - - - - - - - - -  #

class ArticleAllPublicHisPrivateQsMixin():
    # Queryset: 
    #           Staff   ->  super()
    #           Others  ->  (all public + his private)
    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            return super().get_queryset(*args, **kwargs)
        else:
            user = self.request.user
            qs1 = super().get_queryset(*args, **kwargs).is_public()
            qs2 = super().get_queryset(*args, **kwargs).filter(author=user)
            qs = (qs1 | qs2).distinct()
            return qs

class ArticleHisPublicHisPrivateQsMixin():
    # Queryset: 
    #           Staff   ->  super()
    #           Others  ->  (his public + his private)
    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            return super().get_queryset(*args, **kwargs)
        else:
            user = self.request.user
            return super().get_queryset(*args, **kwargs).filter(author=user)

class ArticleStaffNoRestrictionsQsMixin():
    # Queryset: 
    #           Staff   ->  all (public + private)
    #           Others  ->  super()
    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            return Article.objects.all()
        return super().get_queryset(*args, **kwargs)

# - - - - - - - - - - - - - - Comment - - - - - - - - - - - - - -  #

class CommentOwnerQsMixin():
    # Queryset: 
    #           Staff   ->  their
    #           Others  ->  their
    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        return super().get_queryset(*args, **kwargs).filter(author=user)

class CommentStaffNoRestrictionsQsMixin():
    # Queryset: 
    #           Staff   ->  all
    #           Others  ->  their
    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            return Comment.objects.all()
        return super().get_queryset(*args, **kwargs)

# class AllPublicMixin():
#     def get_queryset(self, *args, **kwargs):
#         print("I'm in AllPublicMixin")
#         if self.request.user.is_staff:
#             return super().get_queryset(*args, **kwargs)
#         else:
#             return super().get_queryset(*args, **kwargs).is_public()

# class UserQuerySetMixin():
#     user_field = 'author'
#     allow_staff_view = False

#     def get_queryset(self, *args, **kwargs):
#         user = self.request.user
#         lookup_data = {}
#         lookup_data[self.user_field] = user
#         qs = super().get_queryset(*args, **kwargs)
#         if self.allow_staff_view and user.is_staff:
#             return qs
#         return qs.filter(**lookup_data)

# class PublicQuerySetMixin():
#     user_field = 'author'

#     def get_queryset(self, *args, **kwargs):
#         user = self.request.user
#         qs = super().get_queryset(*args, **kwargs)
#         if user.is_staff:
#             return qs
#         qs1 = qs.is_public()
#         qs2 = qs.filter(author=user)
#         return (qs1 | qs2).distinct()

# class StaffEditorPermissionMixin():
#     # IsAdmin(Staff included) + IsStaffEditorPermission(CustomPermission)
#     permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

# class StaffEditorOrOwnerPermissionMixin():
#     permission_classes = [IsOwner | StaffEditorPermissionMixin]