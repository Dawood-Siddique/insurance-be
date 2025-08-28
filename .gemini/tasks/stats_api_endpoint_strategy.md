# Strategic Plan: Statistics API Endpoint

## 1. Understanding the Goal

The primary objective is to create a new, dedicated API endpoint, `/api/stats/`, that will provide various useful statistics derived from the application's data. The definition of "useful" is currently ambiguous and requires clarification. This plan outlines the steps to define, design, and structure the implementation of this endpoint.

## 2. Investigation & Analysis

Before implementation, a thorough analysis of the existing codebase is required to ensure the new endpoint is consistent with the current architecture and to identify what statistics can be generated.

The following investigation steps are critical:

*   **Analyze Data Models:**
    *   Read `apps/users/models/user_model.py` to understand the structure of the user data.
    *   Read `apps/policy/models.py` to understand the structure of the policy data. This will reveal the fields available for aggregation (e.g., creation dates, policy types, amounts, status).

*   **Analyze Existing API Architecture:**
    *   Read `apps/users/views/user_view.py` and `apps/policy/views/policy_view.py` to understand how API views are currently implemented. This will likely confirm the use of Django Rest Framework (DRF) and patterns like `APIView` or `ViewSet`.
    *   Read `insurance-be/urls.py`, `apps/users/urls.py`, and `apps/policy/urls.py` to understand the current URL routing strategy and how new endpoints are registered.

*   **Critical Questions to Answer:**
    1.  **What specific statistics are considered "useful" for the end-user?** (e.g., total users, total policies, policies created per month, distribution of policy statuses). This is the most important question to clarify before proceeding.
    2.  Are there any performance considerations? (e.g., for large datasets, queries might need optimization).
    3.  Who should have access to this endpoint? (i.e., does it require authentication/permissions?).

## 3. Proposed Strategic Approach

The proposed strategy is to create a new, self-contained Django app for this functionality to ensure modularity and separation of concerns.

### Phase 1: Scope Definition

1.  **Collaborate with Stakeholders:** Define and finalize a precise list of required statistics. Based on the likely model structures, initial suggestions could include:
    *   Total number of registered users.
    *   Total number of policies.
    *   A breakdown of policies by their status (e.g., active, expired, cancelled).
    *   Number of policies created in the last 30 days.
2.  **Define Access Control:** Determine if the endpoint should be public or restricted (e.g., admin-only) and document the requirement.

### Phase 2: Application Scaffolding

1.  **Create a New App:** Generate a new Django app named `stats` within the `apps/` directory.
    ```bash
    uv run python manage.py startapp stats apps/stats
    ```
2.  **App Configuration:** Add the new `apps.stats.apps.StatsConfig` to the `INSTALLED_APPS` list in `insurance-be/settings.py`.

### Phase 3: API Implementation

1.  **Create the API View:**
    *   In `apps/stats/views.py`, create a new DRF `APIView` class (e.g., `StatisticsAPIView`).
    *   Inside the `get` method of this view, implement the logic to gather the statistics defined in Phase 1. Use the Django ORM's aggregation functions (`Count`, `Sum`, etc.) on the `User` and `Policy` models for efficient database queries.
    *   The view should compile the results into a single dictionary and return it as a DRF `Response`. A custom serializer is likely not necessary if the data structure is a simple key-value map.

2.  **Implement Permissions (If Required):** Based on the decision from Phase 1, add the appropriate DRF permission classes (e.g., `IsAdminUser`) to the view.

### Phase 4: URL Routing

1.  **Create App-Specific URLs:**
    *   Create a new file: `apps/stats/urls.py`.
    *   In this file, define a URL pattern that maps a route (e.g., an empty path `''`) to the `StatisticsAPIView`.

2.  **Include in Project URLs:**
    *   In the main `insurance-be/urls.py` file, add an `include()` for the new `stats` app's URLs under the `api/` path.
    ```python
    # insurance-be/urls.py
    urlpatterns = [
        # ... other urls
        path('api/stats/', include('apps.stats.urls')),
    ]
    ```
