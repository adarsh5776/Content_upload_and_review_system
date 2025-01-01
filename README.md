# Movie Management System

This project is a Django-based **Movie Management System** that facilitates the management of movie data. Users can upload movie information via a CSV file, and retrieve paginated, filtered, and sorted lists of movies through API endpoints.

## Key Features and Workflow

### 1. Upload CSV File
- **Endpoint**: `/upload_csv/`
- **Method**: `POST`
- **Description**: Uploads a CSV file containing movie data. Each row in the CSV is saved as a new movie entry in the database.
- **Validation**:
  - Maximum file size: 100 MB.
  - Validates numeric fields (e.g., budget, revenue, vote count) and handles missing data gracefully.

### 2. List Movies
- **Endpoint**: `/movies/`
- **Method**: `GET`
- **Description**: Retrieves a list of movies with support for:
  - **Pagination**: Returns results in chunks of 10 by default. Supports custom page size using the `page_size` query parameter.
  - **Filtering**:
    - By **Release Year**: Filter movies by the year of release using the `release_year` parameter.
    - By **Language**: Filter movies by original language using the `original_language` parameter.
  - **Sorting**:
    - By **Release Date** (`release_date`).
    - By **Vote Average** (`vote_average`).

### 3. Filtering
- **Library**: `django_filters`.
- Filters supported:
  - **Release Year**: Exact match of year (`release_year`).
  - **Original Language**: Case-insensitive match (`original_language`).

### 4. Pagination
- **Class**: `MoviePagination`.
- Default page size: 10.
- Allows customization using the `page_size` query parameter.

### 5. Sorting
- **Library**: `OrderingFilter`.
- Supported fields:
  - `release_date`
  - `vote_average`

### 6. Postman Collection
- **Description**: A Postman collection is included for testing the APIs.
- **Export and Sharing**:
  - The Postman collection is exported in JSON format and can be imported directly into Postman.
  - The collection contains examples for each API endpoint with pre-configured parameters.
  - File Name - imdb_project.postman_collection.json

### 7. Database
- **Model**: `Movie`
- Fields:
  - `title`: Title of the movie.
  - `release_date`: Date of release.
  - `vote_average`: Average user rating.
  - `vote_count`: Total votes received.
  - `budget`: Production budget.
  - `revenue`: Total revenue.
  - `original_language`: Language code (e.g., "en").
  - Additional fields like `overview`, `homepage`, `genre_id`, etc.

## Core Components

### Models
- `Movie`: Defines the structure of the movie data stored in the database.

### Serializers
- `MovieSerializer`: Converts `Movie` model instances into JSON format for API responses.

### Filters
- `MovieFilter`: Adds filtering capabilities for release year and original language.

### ViewSets
- `MovieViewSet`: Combines querysets, serializers, and filters for the `/movies/` endpoint.

### Pagination
- `MoviePagination`: Manages paginated API responses.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/movie-management-system.git
   cd movie-management-system

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Apply migrations:
   ```bash
   python manage.py migrate

4. Start the server:
   ```bash
   python manage.py runserver

5. Test the APIs using the included Postman collection.

## Testing the APIs

Use the included Postman collection (`postman_collection.json`) to test the API endpoints.

### Example Queries

1. **Filter movies released in 2020**  
   ```http
   GET /movies/?release_year=2020

2. **Filter movies released in 2020**  
   ```http
   GET /movies/?original_language=en

3. **Filter movies released in 2020**  
   ```http
   GET /movies/?ordering=vote_average

