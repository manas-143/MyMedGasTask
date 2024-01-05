Feature: Verifying the brand address on footer of reports
  Scenario: Adding a brand to the User and verifying the address in report
    Given User is on Desktop application
    When they navigates to the user section
    And they adds a brand for an existing user
    And they navigates to the brand section
    And they search and verify the address for the added brand
    And they navigates to the FSE application
    And they create an inspection job for the existing user
    And they complete the job
    And they navigate to the desktop application
    And download the reports on the report section
    Then they verify the footer address of the report
