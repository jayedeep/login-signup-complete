from .models import User,Students,Professors,College
from rest_framework import generics
from .serializers import UserCreateSerializer,Collegeserializer,Professorserializer,Studentserializer
from rest_framework import filters
class CreateUser(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
from .permissions import IsProfessor,IsCollege,IsStudent

 #------------------------------------
class CreateCollege(generics.CreateAPIView):
    queryset = Students.objects.all()
    serializer_class = Collegeserializer
    permission_classes = [IsCollege]

class DetailCollege(generics.RetrieveAPIView):
    queryset = College.objects.all()
    serializer_class = Collegeserializer
    permission_classes = [IsCollege]

class UpdateCollege(generics.UpdateAPIView):
    queryset = College.objects.all()
    serializer_class = Collegeserializer
    permission_classes = [IsCollege]

class DestroyCollege(generics.DestroyAPIView):
    queryset = College.objects.all()
    serializer_class = Collegeserializer
    permission_classes = [IsCollege]

#-----------------------------------------------
#college list for admin
#------------------------------------------------

#---------------------professor---------------
 #------------------------------------
class CreateProfessor(generics.CreateAPIView):
    queryset = Professors.objects.all()
    serializer_class = Professorserializer
    permission_classes = [IsProfessor]

class DetailProfessor(generics.RetrieveAPIView):
    queryset = Professors.objects.all()
    serializer_class = Professorserializer
    permission_classes = [IsProfessor]

class UpdateProfessor(generics.UpdateAPIView):
    queryset = Professors.objects.all()
    serializer_class = Professorserializer
    permission_classes = [IsProfessor]

class DestroyProfessor(generics.DestroyAPIView):
    queryset = Professors.objects.all()
    serializer_class = Professorserializer
    permission_classes = [IsProfessor,IsCollege]

class ListProfessors(generics.ListAPIView):
    queryset = Professors.objects.all()
    serializer_class = Professorserializer
    permission_classes = [IsProfessor,IsCollege]
#-----------------------------------------------------------------

#------------Student--------------------------
class CreateStudent(generics.CreateAPIView):
    queryset = Students.objects.all()
    serializer_class = Studentserializer
    permission_classes = [IsStudent]

class DetailStudent(generics.RetrieveAPIView):
    queryset = Students.objects.all()
    serializer_class = Studentserializer
    permission_classes = [IsStudent]

class UpdateStudent(generics.UpdateAPIView):
    queryset = Students.objects.all()
    serializer_class = Studentserializer
    permission_classes = [IsStudent]

class DestroyStudent(generics.DestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = Studentserializer
    permission_classes = [IsProfessor,IsCollege]

class ListStudents(generics.ListAPIView):
    search_fields = ['name', '=semester', '=enrollment', 'department', 'college__name']
    filter_backends = (filters.SearchFilter,)
    queryset = Students.objects.all()
    serializer_class = Studentserializer
    permission_classes = [IsProfessor,IsCollege]

