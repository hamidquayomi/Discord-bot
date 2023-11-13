import discord
import random
import time

randomCoffee = ["Espresso", "Americano", "Cappuccino", "No coffee!", "Grappa", "Double shot"]
randomGreeting = ["hey there :3", "hi sir", "hey! :)", "hoi :]", "hai -.-", "meow", "privet"]
randomGrappa = ["No grappa", "ok grappa", "Doe maar een grappa"]


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return str(random.choice(randomGreeting))

    if p_message == 'hi':
        return str(random.choice(randomGreeting))

    if p_message == 'hey':
        return str(random.choice(randomGreeting))

    if p_message == 'hoi':
        return str(random.choice(randomGreeting))

    if p_message == 'coffee':
        return str(random.choice(randomCoffee))

    if p_message == 'coffee?':
        return str(random.choice(randomCoffee))

    if p_message == 'hi coffee':
        return str(random.choice(randomCoffee))

    if p_message == 'hi coffee?':
        return str(random.choice(randomCoffee))

    if p_message == 'koffie?':
        return str(random.choice(randomCoffee))

    if p_message == 'koffie':
        return str(random.choice(randomCoffee))

    if p_message == 'grappa':
        return str(random.choice(randomGrappa))

    if p_message == 'grappa?':
        return str(random.choice(randomGrappa))



