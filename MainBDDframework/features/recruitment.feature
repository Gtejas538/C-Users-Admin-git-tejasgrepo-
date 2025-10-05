
Feature: Recruitment Feature
    Background: Preconditions for all the steps
        Given Launching the browser
        When later navigating to the url
    @TC_Recruitment_001
    Scenario Outline: To verify that the user has logged in
        When user enters the username "<username>"
        And  user enters the password "<password>"
        Then  user is logged in
       
        Examples:
        
           | username | password  | expected_url|
           | Admin    | admin123  |https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index|
           | Adminyu   | admin123  |https://opensource-demo.orangehrmlive.com/web/index.php/auth/login|
           | Admin    | prabhudev  |https://opensource-demo.orangehrmlive.com/web/index.php/auth/login|
           | Admpoi    | poi  |https://opensource-demo.orangehrmlive.com/web/index.php/auth/login|
           
           
       
       
           
    
        
    
        
        
    
     

 