from behave import given, when, then
from assertpy import assert_that
from sandwich import make_sandwich


@given('a random seed {seed}')
def given_a_random_seed(context, seed: int):
    context.seed = int(seed)


@when('a sandwich is generated')
def when_a_sandwich_is_generated(context):
    context.sandwich = make_sandwich(context.seed)


@then('the price is {expected_price}')
def then_the_price_is(context, expected_price):
    assert_that(context.sandwich[1]).is_equal_to(int(expected_price))


@then('the description is {expected_description}')
def then_the_description_is(context, expected_description):
    assert_that(context.sandwich[0]).is_equal_to(expected_description)
