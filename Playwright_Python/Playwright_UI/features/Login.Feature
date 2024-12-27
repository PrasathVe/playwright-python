Feature: As a user, i want to be able to login and access the home page
  Scenario: By using the valid user credential i should be able to login successfully
    Given Launch the page click Login button
    When I fill the valid "User Name" as "prasathv"
    And I fill the valid password as "tes@t123"
    And I clicked the "Login" button
    Then the menu bar contains the "logout" link
    


