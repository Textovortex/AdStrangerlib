# adstrangerlib


`adstrangerlib` provides basic functionality for writing text-based adventure
games, with the aim of making hard text adventure games.

The foundation of adstrangerlib is the ability to define functions that are
called in response to commands. For example, you could write a function to
be called when the user types commands like "take hat":

    @when('take THING')
    def take(thing):
        print(f'You take the {thing}.')
        inventory.append(thing)

It also includes the foundations needed to write games involving rooms, items,
characters and more... but users will have to implement these features for
themselves as they explore Python programming concepts.

## Installing

`adstrangerlib.py` is a single file that can be copied into your project.

## Differencies from Adventurelib
adstrangerlib is different from adventurelib, with the ability to have strange passages and confusing directions.
For example, if you go north from a cave, you get into a forest. If you go back, you get to a town instead.
Aside from adventurelib's automatic room direction adstrangerlib needs you to declare what is in the back direction of the room.

