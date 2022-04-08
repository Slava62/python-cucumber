Feature: Search

   @search_ex
   Scenario: Search for existing text
       Given user navigates to main page
       When user clicks search button
       And the user types "History" in a search field
       And the user presses the search button
       Then the second link follows to history block

   @search_no
   Scenario: Search for no existig text
       Given user navigates to main page
       When user clicks search button
       And the user types "Not existing text" in a search field
       And the user presses the search button
       Then the user should see the message "The text is not found"

   @search_em 
   Scenario: Search with empty search field
       Given user navigates to main page
       When user clicks search button
       And the user presses the search button
       Then the user should see the popup "Заполните это поле." 