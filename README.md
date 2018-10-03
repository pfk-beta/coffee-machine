# coffee-machine

Coffee machine needs coffee beans, water and milka to produce cup of coffee

So I need class `CoffeeMachine` with states how much resources it has.
Then instance of `CoffeeMachine` will produce cup of coffee. I have created
named tuple for this object. Named tuple contains informations
how much coffee, water, milk is needed for produce beverage.
It also contains information about size of cup.

main methods for making coffee which are avialable for user are:
- `get_americano`
- `get_espresso`
- `get_capuchino`
- `get_late_machiato`

another methods, called service methods are:
- `fill_water`
- `fill_water`
- `attach_milkbox`
as the name suggest, these methods fill resources of coffee machine

there are also 2 methods for stats:
- `showme_coffeestats` which print statistics of choosing coffees
- `showme_uptime` - useful for admins


There are also 2 another method (in 'private' scope), which are not
directly available for user:
- `__get_coffee`
- `__prepare_coffee`
first one is kinda wrapper for the second one.
First method checks state of tanks, if next coffee may be produced.
If there is not required resources, it will raise an proper exception
If all requirements are met, then will call __prepare_coffee
__prepare_coffee
 change state of tanks
 \/    \/    \/
 produce coffee(artificially)
 \/    \/    \/
 update coffee stats
 \/    \/    \/
 return artificial coffee (with coffee type info)


# Tests
run:
```
python3 src/test.py
```

You have to have installed tqdm package in your system(see requirements.txt)

