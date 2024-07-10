# Import UserCreationForm for user registration
from django.contrib.auth.forms import UserCreationForm
# Import login function for user authentication
from django.contrib.auth import login
# Import render and redirect for rendering templates and redirection
from django.shortcuts import render, redirect

# Import API view and permission class decorators
from rest_framework.decorators import api_view, permission_classes
# Import AllowAny permission class for unrestricted access
from rest_framework.permissions import AllowAny
# Import Response for HTTP responses
from rest_framework.response import Response

# Import serializers for Geolocation models
from .serializers import GeoIpSerializer, GeoSerializer
# Import Geolocation model
from .models import Geolocation
# Import get_geo function for retrieving geolocation data
from .utilities import get_geo

# View for creating a new user with no authorization required
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def create_user(request):
	"""
    View function for creating a new user account.

    For POST requests:
        - Validates the UserCreationForm.
        - Logs in the user upon successful form submission.
        - Redirects to 'geo-create' view.

    For GET requests:
        - Renders the 'index.html' template with a new instance of UserCreationForm.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Renders 'index.html' template with form context or redirects to 'geo-create'.
    """
	
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
		
	    # Redirect to 'geo-create' view upon successful user creation
            return redirect('geo-create')
    else:
        form = UserCreationForm()
	    
    # Render 'index.html' with form context
    return render(request, 'index.html', {'form': form})

# View for accessing geolocation data with authorization required
@api_view(['GET'])
def geo_detail(request, pk):
	"""
    	View function for retrieving geolocation details by IP address.

    	Parameters:
		request (HttpRequest): The HTTP request object.
		pk (str): The IP address used to fetch the Geolocation object.

    	Returns:
		Response: JSON response containing serialized Geolocation data.
    	"""
	geo = Geolocation.objects.get(ip=pk)
	serializer = GeoSerializer(geo, many=False)
	return Response(serializer.data)

# View for creating geolocation data with authorization required
@api_view(['GET', 'POST'])
def geo_create(request):
	"""
    	View function for creating geolocation data based on provided IP address.

    	For POST requests:
		- Validates GeoIpSerializer.
		- Calls get_geo utility function to fetch geolocation data and store it.
		- Returns success or error response based on the result.

    	For GET requests:
		- Returns a Response indicating the need for a POST request to create geolocation data.

    	Parameters:
		request (HttpRequest): The HTTP request object.

    	Returns:
		Response: JSON response indicating success or error.
    	"""
	
    serializer = GeoIpSerializer(data=request.data)
    if serializer.is_valid():
        ip = serializer.data['ip']
        result = get_geo(ip)
        return Response(result)
    else:
        return Response({"Error" : "Please choose different IP address"})

# View for removing geolocation data with authorization required
@api_view(['GET', 'DELETE'])
def geo_delete(request, pk):
	"""
    	View function for deleting geolocation data based on provided IP address.

    	Parameters:
        	request (HttpRequest): The HTTP request object.
        	pk (str): The IP address used to fetch and delete the Geolocation object.

    	Returns:
        	Response: JSON response indicating success or error.
    	"""
	
	geo = Geolocation.objects.get(ip=pk)
	geo.delete()
	return Response({"Succes" : "Geolocation succsesfully deleted!"})

# Views for custom error handlers

@api_view(['GET'])
@permission_classes([AllowAny])
def page_not_found(response, exception):
	"""
    	View function for handling 404 errors (Page Not Found).

    	Parameters:
        	request (HttpRequest): The HTTP request object.
        	exception: The exception object captured by Django.

    	Returns:
        	Response: JSON response indicating 404 error.
    	"""
	
    data = {
        "404" : "Page not found"
    }
    return Response(data, status=404)

@api_view(['GET'])
@permission_classes([AllowAny])
def server_error(response):
	"""
    	View function for handling 500 errors (Internal Server Error).

    	Parameters:
        	request (HttpRequest): The HTTP request object.

    	Returns:
        	Response: JSON response indicating 500 error.
    	"""
	
    data = {
        "500" : "Internal server error"
    }
    return Response(data, status=500)



    





