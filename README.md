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
