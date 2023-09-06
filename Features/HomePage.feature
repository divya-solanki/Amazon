Feature: Add To Cart

Scenario: In Today’s Deal tab, select any item and add to the cart.
    Given I open Amazon HomePage
    Then Navigate to todays deal tab
    Then I select the item
    And Add it to the cart

Scenario: In Mobile Tab, Select any mobile, then mouse over on the item and verify the
magnified image of the selected item.
    Given I open Amazon HomePage
    Then Navigate to Mobiles Tab
    Then Select a mobile
    And hover the cursor to to show enlarged image of it
    And verify the zoomed image.

