# Created by papa at 11/28/21
Feature: # Enter feature name here
  # Enter feature description here

#  Scenario: User can open and close quick view by clicking on closing X
#    Given Open GetTop page
#    When Hover over a product
#    And Click on Quick View
#    Then Close Quick View on the right side corner


#  Scenario: User can click Quick View and add product to cart
#    Given Open GetTop page
#    When Hover over a product
#    And Click on Quick View
#    And Add product to cart
#    Then verify product is in cart

  Scenario: User can click through multiple product pages by clicking > and <
    Given Open GetTop page
    When Click on a product
    And Click on left arrow 2 times
    Then Click on right arrow 1 times


