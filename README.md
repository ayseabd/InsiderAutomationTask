# Insider Automation Testing Project

## Project Description
This project involves an automated testing system for Insider job listings. Using Selenium WebDriver, elements on web pages are tested, and the functionality of job listing filters is validated. Additionally, it is tested whether the job listings redirect to the Lever platform.

### Steps:

1. **Visit Insider's Website**  
   Go to [Insider's website](https://useinsider.com/) and verify that the Insider home page opens correctly.

2. **Navigate to Careers Page**  
   - Select the “Company” menu in the navigation bar.
   - Then select “Careers” and verify that the Careers page is opened correctly.
   - Check that the following blocks are present and visible:
     - Locations
     - Teams
     - Life at Insider

3. **Access Quality Assurance Careers Page**  
   - Go to the [Quality Assurance Careers page](https://useinsider.com/careers/quality-assurance/).
   - Click the “See all QA jobs” button.
   - Filter jobs by:
     - **Location:** “Istanbul, Turkey”
     - **Department:** “Quality Assurance”
   - Verify the presence of the filtered job list.

4. **Validate Job Details**  
   - Check that all jobs’:
     - **Position** contains “Quality Assurance”.
     - **Department** contains “Quality Assurance”.
     - **Location** contains “Istanbul, Turkey”.

5. **Verify Redirection to Lever Application Form**  
   - Click the “View Role” button.
   - Confirm that this action redirects you to the Lever Application form page.

## Project Structure

- **pages/** - Contains page object model classes.
  - `pages/base_page.py` - Base class for all pages.
  - `pages/home_page.py` - Page object for the home page.
  - `pages/careers_page.py` - Page object for the careers page.
  - `pages/open_positions_page.py` - Page object for the open positions page.

- **tests/** - Contains test scenarios.
  - `tests/test_check_insider_job_openings.py` - Test scenario for job openings.
  - `tests/base_test.py` - Base test class for running tests.
 
## Test Scenarios Results

All test scenarios have been executed successfully with the following exception:

1. **Home Page Verification**: The Insider home page opens correctly.
2. **Careers Page Verification**: The “Company” menu and “Careers” page, including its Locations, Teams, and Life at Insider blocks, open correctly.
3. **Quality Assurance Jobs Page**: The page at `https://useinsider.com/careers/quality-assurance/` is accessed successfully. The "See all QA jobs" button works as expected. Jobs are filtered by Location: "Istanbul, Turkey" and Department: "Quality Assurance," and the job list is displayed.

   **Note**: There is a known issue where the Location filter only displays the "All" option if the page has not fully loaded. To mitigate this, `time.sleep` is used to wait for the page to fully load before interacting with the filters. However, this issue persists if the page is not fully loaded in time.
   
4. **Job Details Verification**: All listed jobs have their Position containing "Quality Assurance," Department containing "Quality Assurance," and Location containing "Istanbul, Turkey."
5. **Lever Application Redirect**: Clicking the "View Role" button redirects to the Lever Application form page successfully.

All other tests have passed, confirming that the application is functioning as expected, aside from the noted issue with the location filter.

