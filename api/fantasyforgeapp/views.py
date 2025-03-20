    
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


'''
class UserCharactersView(APIView):
    """Returns only the characters owned by the authenticated user"""

    #permission_classes = [IsAuthenticated]

    def get(self, request):
        """Return all characters owned by the user"""
        owned_characters = Character.objects.filter(ownership__user=request.user)
        serializer = CharacterSerializer(owned_characters, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Create a new character and assign it to the user"""
        serializer = CharacterSerializer(data=request.data)
        if serializer.is_valid():
            character = serializer.save()

            # Assign ownership to the user
            Ownership.objects.create(user=request.user, character=character)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''

# list of characters
class CharacterViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    #queryset = Character.objects.all()
    serializer_class = CharacterSerializer

    def get_queryset(self):
        """Return only the characters owned by the logged-in user"""
        return Character.objects.filter(ownership__user=self.request.user)


# credit : https://github.com/HE-Arc/Instagenda/

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
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
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
   