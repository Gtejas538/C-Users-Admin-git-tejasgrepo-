@tag
Feature: Login page feature
    
	Background: Precodintion steps for Login Feature
	   	Given Chrome browser is launched
        When User navigates to OrangeHRM Login Page

  @tag1
  Scenario: Navigation to OrangeHRM Login Page
    Then User should see page title as OrangeHRM

    @Login 
    Scenario: Validate the login to OrangeHRM
        When User enters Username
        And User enters Password
        And User clicks on Login button
        Then User should see /dashboard/index in the current page URL

    @LoginandParamters @allureTests
    Scenario:Validate the login page with parameters
        When User enters username "Admin"
        And User enters password "admin123"
        And User clicks on Login button
        Then User should see "/dashboard/index" in the current page URL
      
   
	@LoginDDT
    Scenario Outline: Validate the login page
        When User enters username "<username>"
        And User enters password "<password>"
        When User clicks on Login button
        Then User should see "<pageurl>" in the current page URL
        
     Examples:
       | username | password  | pageurl            |
       | Admin    | admin123  | /dashboard/index   |
       | Adminee  | admin897  | /auth/login        |
       
       
 
      
  #@tag2
  #Scenario Outline: Title of your scenario outline
    #Given I want to write a step with <name>
    #When I check for the <value> in step
    #Then I verify the <status> in step
#
    #Examples: 
      #| name  | value | status  |
      #| name1 |     5 | success |
      #| name2 |     7 | Fail    |

    
    
