from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer, UserSerializer, ProfileSerializer
from .permissions import IsAdminUserRole, IsOwnerOrReadOnly

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        """
        Register a new user.
        Admins can set role='admin' in payload if allowed.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserSerializer(user).data  
        return Response(
            {"message": "User registered successfully", "user": data},
            status=status.HTTP_201_CREATED
        )



class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminUserRole]



class UserDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsAdminUserRole]

    def delete(self, request, user_id):
        if request.user.id == user_id:
            return Response(
                {"detail": "Admins cannot delete their own account via this endpoint."},
                status=status.HTTP_400_BAD_REQUEST
            )
        user = get_object_or_404(User, id=user_id)
        user.delete()
        return Response(
            {"message": f"User {user_id} deleted successfully."},
            status=status.HTTP_204_NO_CONTENT
        )



class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get(self, request):
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = ProfileSerializer(
            request.user, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"message": "Profile updated successfully", "profile": serializer.data}
        )
