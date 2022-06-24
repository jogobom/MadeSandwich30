Feature: Make sandwiches

    Make a random sandwich and calculate an accurate price

    Scenario Outline: Generate expected sandwich from given seed
        Given a random seed <seed>
        When a sandwich is generated
        Then the price is <price>
        And the description is <description>
        Examples:
            | seed | price | description |
            | 42   | 600   | Sausage     |
