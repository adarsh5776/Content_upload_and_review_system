import csv
import django_filters
from .models import Movie
from .serializers import MovieSerializer
from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter


@api_view(["POST"])
def upload_csv(request):
    """
    Handles CSV file upload for movie data and saves each row to the Movie model.
    Validates file size and presence, processes the CSV, and creates Movie objects.
    
    Args:
        request (HttpRequest): The request object containing the file.
        
    Returns:
        JsonResponse: Response indicating success or failure.
    """
    if "file" not in request.FILES:
        return JsonResponse({"error": "No file provided"}, status=400)

    file = request.FILES["file"]

    # Validate file size (limit to 100MB)
    if file.size > 100 * 1024 * 1024:
        return JsonResponse({"error": "File too large"}, status=400)

    try:
        data_set = file.read().decode("UTF-8")
        io_string = csv.reader(data_set.splitlines())
        next(io_string)  # Skip header row

        # Process each row in the CSV
        for row in io_string:
            Movie.objects.create(
                budget=int(float(row[0])) if row[0] else None,
                homepage=row[1] if row[1] else None,
                original_language=row[2] if row[2] else None,
                original_title=row[3] if row[3] else None,
                overview=row[4] if row[4] else None,
                release_date=row[5] if row[5] else None,
                revenue=int(float(row[6])) if row[6] else None,
                runtime=int(row[7]) if row[7] else None,
                status=row[8] if row[8] else None,
                title=row[9] if row[9] else None,
                vote_average=row[10] if row[10] else None,
                vote_count=int(float(row[11])) if row[11] else None,
                production_company_id=int(row[12]) if row[12] else None,
                genre_id=int(row[13]) if row[13] else None,
                languages=row[14] if row[14] else None,
            )
        return JsonResponse({"message": "File uploaded successfully"})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


class MovieFilter(django_filters.FilterSet):
    """
    Filter class for querying movies based on release year and original language.
    
    Provides filtering options:
    - By the year of release (exact match)
    - By original language (case-insensitive match)
    """
    release_year = django_filters.NumberFilter(
        field_name="release_date__year", lookup_expr="exact"
    )
    original_language = django_filters.CharFilter(
        field_name="original_language", lookup_expr="iexact"
    )

    class Meta:
        model = Movie
        fields = ["release_year", "original_language"]


class MoviePagination(PageNumberPagination):
    """
    Pagination class to handle paginated responses for movie listings.
    
    - Defines page size as 10.
    - Allows for query parameter 'page_size' to adjust the page size.
    """
    page_size = 10
    page_size_query_param = "page_size"


class MovieViewSet(ReadOnlyModelViewSet):
    """
    Read-only viewset for listing and retrieving movie data.
    
    - Supports pagination.
    - Allows filtering by release year and original language.
    - Allows ordering by release date and vote average.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = MoviePagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = MovieFilter
    ordering_fields = ["release_date", "vote_average"]
