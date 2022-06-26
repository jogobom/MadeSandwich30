Feature: Make sandwiches

    Make a random sandwich and calculate an accurate price

    Scenario Outline: Generate expected sandwich from given seed
        Given a random seed <seed>
        When a sandwich is generated
        Then the description is <description>
        And the price is <price>
        Examples:
            | seed     | price | description                                                                                                  |
            | 42       | 395   | SOTD. Beef, Grated Carrot, Grated Carrot, Mango Chutney (try it in Sliced Bread!)                            |
            | 123      | 460   | SOTD Tuna, Stilton, Beetroot, Basil Pesto (perfect for a White NOT A STOTTIE!)                               |
            | 999      | 465   | Sotd Tuna, Parmesan, Stuffing, BBQ Sauce (try it in a Wrap!)                                                 |
            | 456      | 365   | SOTD: Chorizo, Banana, Onion Marmalade (try it in Sliced Bread!)                                             |
            | 5        | 515   | SOTD: Brussels Pate, Stilton, Baked beans, Avocado, Mango Chutney (try it in a Panini!)                      |
            | 87       | 485   | SOTD. Tuna Mayo, Beetroot, Roast Peppers, Onion Marmalade, Pinenuts (perfect for a Wholemeal NOT A STOTTIE!) |
            | 45987006 | 440   | SOTD Small Prawns, Roast Peppers, Onion Marmalade (try it in a Panini!)                                      |
            | 8979     | 430   | SOTD. Smoked Salmon, Coleslaw, Tomato Chutney (perfect for Sliced Bread!)                                    |
            | 3453     | 455   | Sotd Chicken, Emmental, Olives, BBQ Sauce (try it in a Wholemeal NOT A STOTTIE!)                             |
