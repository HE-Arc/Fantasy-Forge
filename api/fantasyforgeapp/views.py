    
from .models import Character, Ownership
from .serializers import CharacterSerializer, UserSerializer
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# list of characters
class CharacterViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    #queryset = Character.objects.all()
    serializer_class = CharacterSerializer

    def get_queryset(self):
        """Return only the characters owned by the logged-in user"""
        return Character.objects.filter(owners=self.request.user)
    
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def add_ownership(self, request, pk=None):
        """Add ownership of a character to a specified user by username or the logged-in user"""
        try:
            character = self.get_object()

            owner_name = request.data.get("owner_name")
            if owner_name:
                try:
                    user = User.objects.get(username=owner_name)
                except User.DoesNotExist:
                    return Response({"error": "User not found"}, status=404)
            else:
                user = request.user

            if Ownership.objects.filter(user=user, character=character).exists():
                return Response({"error": "Ownership already exists"}, status=400)

            character.owners.add(user)  # Add the user to the character's owners
            return Response({"message": f"Ownership added for user {user.username}"}, status=201)

        except Character.DoesNotExist:
            return Response({"error": "Character not found"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)


# credit : https://github.com/HE-Arc/Instagenda/

@method_decorator(csrf_exempt, name="dispatch")
class AuthViewSet(viewsets.ViewSet):    
    @action(detail=False, methods=['post'])
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            login(request, user)
            
            return Response({"refresh": str(refresh),
                             "access": str(refresh.access_token),
                             "message": "User logged in"}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def register(self, request):
        password = request.data.get('password')
        password2 = request.data.get('password2')

        if password != password2:
            return Response({"error": "Passwords do not match"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)  # Ensure the password is hashed
            user.save()
            login(request, user)
            return Response({"message": "User registered"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def logout(self, request):
        if request.user.is_authenticated:
            logout(request)
            return Response({"message": "User logged out"}, status=status.HTTP_200_OK)
        return Response({"error": "User not logged in"}, status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def profile(self, request):
        if not request.user or request.user.is_anonymous:
            return Response({"error": "User not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def search_users(self, request):
        """Search for users by username"""
        username = request.query_params.get('username', None)
        if username:
            users = User.objects.filter(username__icontains=username)[:5]
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "No username provided"}, status=status.HTTP_400_BAD_REQUEST)
   