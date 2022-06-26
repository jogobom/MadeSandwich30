import datetime
import logging

import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
    logging.info('Python timer trigger function ran at %s', utc_timestamp)

# var reader = FSharpFunc<string,string>.FromConverter((string p)
#     => File.ReadAllText(Path.Combine(context.FunctionAppDirectory, p)));

# var sandwich = Sandwich.make_sandwich(rand, reader);
# log.LogInformation($"Sandwich from seed {seed}: {sandwich.ToString()}");
# log.LogInformation($"Calculated price to be {sandwich.TotalPrice} pence");

# var message = MessageBuilder.Build(description, price);

# log.LogInformation(message);
# await Slack.PostToFood(message);
