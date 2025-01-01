# Project Working Overview

This project is a **Movie Management System** that allows users to upload movie data via CSV files, filter movies by specific criteria, and retrieve paginated, sortable lists of movies.

## Key Features and Workflow

1. **Upload CSV File**:
   - Endpoint: `/upload_csv/`
   - Reads movie data from a CSV file and stores it in the database.

2. **List Movies**:
   - Endpoint: `/movies/`
   - Returns a list of movies with:
     - Pagination.
     - Filtering by:
       - **Release Year** (`release_year`).
       - **Original Language** (`original_language`).
     - Sorting by:
       - **Release Date**.
       - **Vote Average**.

3. **Filtering**:
   - Implemented using `django_filters`.
   - Filters movies based on:
     - Year of release.
     - Original language (case-insensitive).

4. **Pagination**:
   - Uses `PageNumberPagination` to return 10 movies per page by default.
   - Supports dynamic page size via the `page_size` query parameter.

5. **Sorting**:
   - Uses `OrderingFilter` to sort movies by `release_date` or `vote_average` based on query parameters.

6. **Postman Collection**:
   - Provides a Postman collection to test all API endpoints.

7. **Database Integration**:
   - Data is stored in a `Movie` model with fields like `title`, `release_date`, `vote_average`, etc.

## Core Components

- **Model**: Defines the `Movie` structure.
- **Serializer**: Converts model instances into JSON format for API responses.
- **Filters**: Adds filtering capabilities.
- **ViewSet**: Combines querysets, filters, and serializers for the `movies/` endpoint.
- **Pagination**: Ensures a consistent number of results per page.

