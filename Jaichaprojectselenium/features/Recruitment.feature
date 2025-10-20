@tag
Feature: Recruitment page feature

	Background: Precodintion steps for Login Feature
	    Background: Precodintion steps for Login Feature
		Given Chrome browser is launched
    When User navigates to OrangeHRM Login Page
    When User enters Username "Admin"
    And User enters Password "admin123"
    And User clicks on Login button
    Then User should see "/dashboard/index" in the current page URL
    
    @ValidateRecruitmentPage
    Scenario: Validate the Recruitment page
    When User clicks on Recruitment tab
    Then  User should see URL as "/recruitment/viewCandidates"
    
    @upgrade
    Scenario: Validate the Upgrade Button
    When User clicks on Upgrade button
    
    @Search
    Scenario: Validate the Search functionality
    When User clicks on Recruitment tab
    Then  User should see URL as "/recruitment/viewCandidates"
    When User enters data in the Vacacny Tab
    Then User must be able to validate the records
    
    @Add
    Scenario: Validate the ADD functionality
    When User clicks on Recruitment tab
    Then  User should see URL as "/recruitment/viewCandidates"
    When User clicks on Add button
    Then User should see "Add Candidate" text on the page
    When User enters data in the Add Candidate page
    And Users enters the second name
    And User enter the email id
    Then User clicks on Save button
    When User clicks on Recruitment tab
    Then  User should see URL as "/recruitment/viewCandidates"
    And User must be able to see the added candidate in the list
    
    @Reset
    Scenario: Vaidate the RESET Button
    When User clicks on Recruitment tab
    Then User should see URL as "/recruitment/viewCandidates"
    When User enters all the  data in the Candidates Tab
    And User enters the second data
    Then User clicks on Reset button
    And All the fields should be reset to default values
    
    @Edit
    Scenario: Validate the Edit functionality
    When User clicks on Recruitment tab
    Then User should see URL as "/recruitment/viewCandidates"
    When User enters data in the Vacacny Tab
    Then User clicks on Edit button
   
    
    
    
    
    
    

    

	         	
  
  


    