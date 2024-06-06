Superpy is een command-line interface (CLI) tool voor het beheren van supermarktaankopen en -verkopen. Deze gids legt uit hoe je de verschillende commando's van Superpy kunt gebruiken.

## Algemene Syntax

```
python main.py <command> [options]
```

Beschikbare Commando's:

1. buy - Koop een nieuw product
2. sell - Verkoop een product
3. list - Lijst alle producten op
4. forward - Reis vooruit in de tijd
5. backward - Reis terug in de tijd
6. profit - Bereken de winst voor een specifieke datum
7. revenue - Bereken de omzet voor een specifieke datum
8. reset_date - Reset de datum naar de huidige datum

## Command Details

1. `buy`

Koop een nieuw product en voeg het toe aan de voorraad.

Syntax:

```
python main.py buy <name> <price> <quantity> <expiration>
```

Voorbeeld:

```
python main.py buy Apple 0.5 20 2024-06-30
```

2. `sell`

Verkoop een product uit de voorraad.

Syntax:

```
python main.py sell <name> <sell_price>
```

Voorbeeld:

```
python main.py sell Apple 0.75
```

3. `list`

Lijst alle producten in de voorraad op.

Syntax:

```
python main.py list
```

Voorbeeld:

```
python main.py list
```

4. `forward`

Reis vooruit in de tijd met een bepaald aantal dagen.

Syntax:

```
python main.py forward <days>
```

Voorbeeld:

```
python main.py forward 5
```

5. `backward`

Reis terug in de tijd met een bepaald aantal dagen.

Syntax:

```
python main.py backward <days>
```

Voorbeeld:

```
python main.py backward 5
```

6. `profit`

Bereken de winst voor een specifieke datum

Syntax:

```
python main.py profit <date>
```

Voorbeeld:

```
python main.py profit 2024-06-05
```

Opmerking:

Je kunt ook `today` of `yesterday` gebruiken in plaats van een specifieke datum.

7. `revenue`

Bereken de omzet voor een specifieke datum.

Syntax:

```
python main.py revenue <date>
```

Voorbeeld:

```
python main.py revenue 2024-06-05
```

Opmerking:

Je kunt ook `today` of `yesterday` gebruiken in plaats van een specifieke datum.

8. `reset_date`

Reset de datum naar de huidige datum.

Syntex:

```
python main.py reset_date
```

Voorbeeld:

```
python main.py reset_date
```

## Voorbeelden en Scenario's

1. Product kopen en verkopen

Koop 10 bananen met een prijs van 0,3 per stuk en een vervaldatum van 2024-07-01:

```
python main.py buy Banana 0.3 10 2024-07-01
```

Verkoop 5 bananen voor 0,5 per stuk:

```
python main.py sell Banana 0.5
```

2. Datumbeheer

Reis 7 dagen vooruit in de tijd:

```
python main.py forward 7
```

Reis vervolgens 2 dagen terug in de tijd:

```
python main.py backward 2
```

3. Financiële rapportage

Bereken de winst van vandaag:

```
python main.py profit today
```

Bereken de omzet van gisteren:

```
python main.py revenue yesterday
```

Met deze commando's en voorbeelden kun je efficiënt gebruik maken van Superpy om je supermarktaankopen en -verkopen te beheren en te analyseren.