Feature: User Registration

  Scenario: Successful user registration
    Given I am on the registration page
    When I register with dynamically generated user data
    Then I should see the registration success message