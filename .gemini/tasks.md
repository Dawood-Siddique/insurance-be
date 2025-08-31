
# Project Tasks

## 1. Statistics API Endpoint
- [x] 1.1. **Scope Definition:** Finalized the list of required statistics.
    *   **User Statistics:**
        *   Total number of users
        *   Number of active users
        *   Number of verified users
        *   New users in the last 30 days (time duration to be static, provided by user)

    *   **Policy Statistics:**
        *   Total number of policies
        *   Policies by payment status (e.g., 'active', 'complete', 'cancelled')
        *   Policies issued in the last 30 days (time duration to be static, provided by user)
        *   Total gross premium
        *   Total client premium
        *   Policies by insurance company (count per company)
        *   Policies by agent (count per agent)
        *   Policies by payment method (count per method)

    *   **Transaction Statistics (Bank Statement-like Information):**
        *   Total transactions
        *   Total amount transacted
        *   Transactions by type (e.g., 'cancelled', 'payment', 'credit_adjustment', 'payback')
- [x] 1.2. **Access Control:** Determined and documented the required permissions for the endpoint. The statistics API endpoint will require `IsAdminUser` permission (accessible only to authenticated staff/admin users).

## 2. Generate Report Feature
- [x] [Manual: Pass] 2.1. **Backend Generation:** Implement the report generation logic on the backend using a library like `openpyxl` or `pandas` to create an `.xlsx` file.
- [x] [Manual: Pass] 2.2. **API Endpoint:** Create a new API endpoint (e.g., `/api/report/download/`) that accepts filters (e.g., date range, policy status).
- [x] [Manual: Pass] 2.3. **Data Fetching:** In the endpoint logic, fetch `Policy` and related data from the database based on the provided filters.
- [x] 2.4. **Calculations:** Perform necessary calculations for summary fields like Total Revenue, Total Amount Paid, and Total Amount Remaining.
- [x] 2.5. **File Formatting:** Structure the data into a "balance-sheet-like" format within the Excel file, including headers, currency formatting, and summary sections.
- [x] 2.6. **File Response:** Send the generated Excel file as a downloadable attachment in the API response using the `Content-Disposition` header.
