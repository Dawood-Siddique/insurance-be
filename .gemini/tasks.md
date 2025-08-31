
# Project Tasks

## 1. Statistics API Endpoint
- [ ] 1.1. **Scope Definition:** Finalize the list of required statistics (e.g., total users, total policies, policies by status, policies in the last 30 days).
- [ ] 1.2. **Access Control:** Determine and document the required permissions for the endpoint (e.g., public, admin-only).
- [ ] 1.3. **App Scaffolding:** Create a new Django app named `stats` inside the `apps/` directory.
- [ ] 1.4. **App Configuration:** Add the new `stats` app to `INSTALLED_APPS` in `insurance-be/settings.py`.
- [ ] 1.5. **API View Creation:** Create a DRF `APIView` (e.g., `StatisticsAPIView`) in `apps/stats/views.py`.
- [ ] 1.6. **Statistics Logic:** Implement the `get` method in the view to efficiently query and calculate the defined statistics using the Django ORM.
- [ ] 1.7. **Permissions:** Add the required DRF permission classes to the view.
- [ ] 1.8. **URL Routing (App):** Create `apps/stats/urls.py` and map a route to the `StatisticsAPIView`.
- [ ] 1.9. **URL Routing (Project):** Include the `stats` app's URLs in the main `insurance-be/urls.py` under the `/api/stats/` path.

## 2. Generate Report Feature
- [ ] 2.1. **Backend Generation:** Implement the report generation logic on the backend using a library like `openpyxl` or `pandas` to create an `.xlsx` file.
- [ ] 2.2. **API Endpoint:** Create a new API endpoint (e.g., `/api/report/download/`) that accepts filters (e.g., date range, policy status).
- [ ] 2.3. **Data Fetching:** In the endpoint logic, fetch `Policy` and related data from the database based on the provided filters.
- [ ] 2.4. **Calculations:** Perform necessary calculations for summary fields like Total Revenue, Total Amount Paid, and Total Amount Remaining.
- [ ] 2.5. **File Formatting:** Structure the data into a "balance-sheet-like" format within the Excel file, including headers, currency formatting, and summary sections.
- [ ] 2.6. **File Response:** Send the generated Excel file as a downloadable attachment in the API response using the `Content-Disposition` header.
