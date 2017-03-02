# Cucumber Scenario Outline Generator
> given a scenario outline, generates an table

This project born from the teory that a good programmer is a lazy one programmer.

## How-to use

Given an scenario description, an outline table is generated.

```
~$ echo "                
        Given an entry with monthly payload format
        And with <hoursActivated> hours activated
        And with <hoursUsed> hours used
        And with <expiredHours> expired hours
        And with <ltdHoursActivated> life-to-date hours activated
        And with <ltdHoursUsed> life-to-date hours used
        And with <ltdExpiredHours> life-to-date expired hours
        And with <ltdExpiredUnits> life-to-date expired units
        And with <ltdActiveHours> life-to-date active hours
        And with <ltdNonActiveHours> life-to-date non-active hours
        And with <ltdActiveUnits> life-to-date active units
        And with <ltdNonActiveUnits> life-to-date non-active units
        And with <ltdActivedUnits> life-to-date non-active units
" | python outline_generator.py
```

Yes...at first it will consume from standard input.
The output for that will be something like:

```
|hoursActivated |hoursUsed  |expiredHours	|ltdHoursActivated	|ltdHoursUsed	|ltdExpiredHours	|ltdExpiredUnits	|ltdActiveHours	|ltdNonActiveHours	|ltdActiveUnits	|ltdNonActiveUnits	|ltdActivedUnits |
|	              |	          |	            |	                  |     	      |	                |	                |             	|	                  |	              |                   |             	 |
```

## Roadmap

* Unit tests
* Pip package
* Web app

## Release History

* 0.0.1
    * Work in progress

## Meta

Alex Rocha - [about.me](http://about.me/alex.rochas)
