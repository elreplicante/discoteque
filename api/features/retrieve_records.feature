Feature: List all records
  Scenario: No records on the discoteque
    Given I lost all my records
    When I see my records list
    Then I see nothing

  Scenario: Some records on my studio
    Given There are some records in my discoteque
    When I see my records list
    Then I see the records
