
from django.urls import path
from .views import CompanyDetail, CompanyList, EmployeeDetail, EmployeeList, DeviceDetail, DeviceList

#All Route Mapping with View....
urlpatterns = [
    path('company/', CompanyList.as_view()),
    path('company/<int:pk>', CompanyDetail.as_view()),
    path('employee/', EmployeeList.as_view()),
    path('employee/<int:pk>', EmployeeDetail.as_view()),
    path('device/', DeviceList.as_view()),
    path('device/<int:pk>', DeviceDetail.as_view()),
]
