from django.urls import path
from .views import VisRegPage, AllVisitorsPage, EditVisitorPage, Search, Status, CheckedOut





urlpatterns = [
    path('registration/', VisRegPage, name = 'registration'),
    #path('singlevisitor/', SingleVisitor, name = 'singlevisitor'),
    path('allvisitors/', AllVisitorsPage, name = 'allvisitors'),
    path('editvisitor/<int:visitor_id>', EditVisitorPage, name = 'editvisitor'),
    path('search/', Search, name = 'search'),
    path('status/', Status, name = 'status'),
    path('checkout/', CheckedOut, name = 'checkout'),
]
