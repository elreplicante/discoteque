Feature: Retrieve Records
  In order to satisfy my ego
  As a vinyl junkie
  I want to see all my records


  Scenario: No records on my studio
    Given I lost all my records
    When I see my records list
    Then I see nothing

  Scenario: Some records on my studio
    Given There are some records in my studio
    When I see my records list
    Then I see the records
