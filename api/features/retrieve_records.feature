Feature: Retrieve Records
  In order to satisfy my ego
  As a vinyl junkie
  I want to see all my records


  Scenario: No records on my studio
    Given I lost all my records
    When I see my records list
    Then I see anything
