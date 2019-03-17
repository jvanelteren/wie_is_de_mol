from ExamDistribution.Structure import Question, TestInput, Result, Episode

# Aflevering 1 (geen afvaller)
# Vragen:
# 1 - De Mol is:
# 1: Niels, Rick, Robert, Sinan, Jamie; 2: Evi, Evelien, Merel, Nikkie, Sarah
# 4 - Trok de Mol helemaal alleen een kist omhoog tijdens de opdracht 'Over Bruggen'?
# 1: Jamie; 2: Evi, Evelien, Merel, Niels, Nikkie, Rick, Robert, Sarah, Sinan
# 10 - Bij welke groep werd de Mol ten dans gevraagd tijdens de opdracht 'In Zicht'?
# 1: Jamie, Rick, Sarah; 2: Merel, Nikkie, Niels, Evi; 3: Sinan, Robert, Evelien
# 11 - Heeft de Mol op blote voeten gedanst bij de opdracht 'In Zicht'?
# 1: Jamie, 2: Evi, Evelien, Merel, Niels, Nikkie, Rick, Robert, Sarah, Sinan
# 12 - Pakte de Mol geld aan van Rik aan het einde van de opdracht 'In Zicht'?
# 1: Evelien; 2: Evi, Jamie, Merel, Niels, Nikkie, Rick, Robert, Sarah, Sinan
# 16 - Wat was de kleur van de fiets van de Mol bij de opdracht 'Rondje om de Kerk'?
# 1 (Rood): Evi, Robert, Nikkie, Merel, Sarah; 2 (Groen): Evelien, Niels, Sinan; 3 (Blauw): Jamie, Rick
# Antwoorden: Niels (4, 2), Evelien (11, 1) (Geen Scherm), Jamie (1, 1), Robert (10, 1), Merel (Geen Scherm),
# Nikkie (16, 2) (Geen Scherm), Rick (12, 1), Evi: (Geen Scherm)
players1 = ['Evi', 'Evelien', 'Jamie', 'Merel', 'Niels', 'Nikkie', 'Rick', 'Robert', 'Sarah', 'Sinan']
question1_1 = Question({1: ['Niels', 'Rick', 'Robert', 'Sinan', 'Jamie'],
                        2: ['Evi', 'Evelien', 'Merel', 'Nikkie', 'Sarah']})
question1_4 = Question({1: ['Jamie'],
                        2: ['Evi', 'Evelien', 'Merel', 'Niels', 'Nikkie', 'Rick', 'Robert', 'Sinan', 'Sarah']})
question1_10 = Question({1: ['Jamie', 'Rick', 'Sarah'],
                         2: ['Merel', 'Nikkie', 'Niels', 'Evi'],
                         3: ['Sinan', 'Robert', 'Evelien']})
question1_11 = Question({1: ['Jamie'],
                         2: ['Evi', 'Evelien', 'Merel', 'Niels', 'Nikkie', 'Rick', 'Robert', 'Sarah', 'Sinan']})
question1_12 = Question({1: ['Evelien'],
                         2: ['Evi', 'Jamie', 'Merel', 'Niels', 'Nikkie', 'Rick', 'Robert', 'Sarah', 'Sinan']})
question1_16 = Question({1: ['Evi', 'Robert', 'Nikkie', 'Merel', 'Sarah'],
                         2: ['Evelien', 'Niels', 'Sinan'],
                         3: ['Jamie', 'Rick']})
result1 = Result(False, ['Evelien', 'Robert', 'Nikkie', 'Evi'])
episode1 = Episode(players1, result1,
                   {'Niels': TestInput({4: 2}), 'Evelien': TestInput({11: 1}), 'Jamie': TestInput({1: 1}),
                    'Robert': TestInput({10: 1}), 'Nikkie': TestInput({16: 2}), 'Rick': TestInput({12: 1})},
                   {1: question1_1, 4: question1_4, 10: question1_10, 11: question1_11, 12: question1_12,
                    16: question1_16})

# Aflevering 2 (afvaller: Evi)
# Vragen:
# 2 - Hoeveel zwemdiploma's heeft de Mol:
# 1 (0 diploma's): Evi; 2 (1 diploma): Sinan;  3 (2 diploma's): Merel, Niels, Rick, Robert;
# 4 (3 diploma's): Evelien, Sarah, Jamie; 5 (6 diploma's): Nikkie
# 4 - Waar bevond de Mol zich tijdens de opdracht 'Ver Tellen':
# 1: Evelien, Evi, Jamie, Merel, Niels, Robert, Sarah, Sinan; 2: Nikkie, Rick
# 10 - Als hoeveelste ging de Mol het veld in tijdens de opdracht 'Uit Stralen': (Niet accuraat)
# 1 - Sinan, 2 - Evi, 3 - Evelien, 4 - Jamie, 5 - Merel, 6 - Niels, 7 - Nikkie, 8 - Rick, 9 - Robert, 10 - Sarah
# 20 - Wie is de Mol:
# 1: Evelien; 2: Evi; 3: Jamie; 4: Merel; 5: Niels; 6: Nikkie; 7: Rick; 8: Robert; 9: Sarah; 10: Sinan
# Antwoorden: Rick (2, 4), Nikkie (4, 1), Merel (20, 1), Robert (1 joker), Jamie (10, 1)
players2 = ['Evi', 'Evelien', 'Jamie', 'Merel', 'Niels', 'Nikkie', 'Rick', 'Robert', 'Sarah', 'Sinan']
question2_2 = Question({1: ['Evi'],
                        2: ['Sinan'],
                        3: ['Merel', 'Niels', 'Rick', 'Robert'],
                        4: ['Evelien', 'Sarah', 'Jamie'],
                        5: ['Nikkie']})
question2_4 = Question({1: ['Evelien', 'Evi', 'Jamie', 'Merel', 'Niels', 'Robert', 'Sarah', 'Sinan'],
                        2: ['Nikkie', 'Rick']})
question2_10 = Question({1: ['Sinan'], 2: ['Evi'], 3: ['Evelien'], 4: ['Jamie'], 5: ['Merel'], 6: ['Niels'],
                         7: ['Nikkie'], 8: ['Rick'], 9: ['Robert'], 10: ['Sarah']})
question2_20 = Question({1: ['Evelien'], 2: ['Evi'], 3: ['Jamie'], 4: ['Merel'], 5: ['Niels'], 6: ['Nikkie'],
                         7: ['Rick'], 8: ['Robert'], 9: ['Sarah'], 10: ['Sinan']})
result2 = Result(True, ['Evi'])
episode2 = Episode(players2, result2,
                   {'Rick': TestInput({2: 4}), 'Nikkie': TestInput({4: 1}), 'Merel': TestInput({20: 2}),
                                       'Robert': TestInput(jokers = 1), 'Jamie': TestInput({10: 1})},
                   {2: question2_2, 4: question2_4, 10: question2_10, 20: question2_20})

# Aflevering 3 (afvaller: Nikkie)
# Vragen:
# 4 - Welk Spaanse woord kreeg de Mol bij aanvang van de opdracht 'Vlag Uithangen':
# 1: Evelien, 2: Jamie, 3: Merel, 4: Sinan, 5: Niels, 6: Nikkie, 7: Rick, 8: Robert, 9: Sarah (Niet Accuraat)
# 7 - Kreeg de Mol de taak om de was op te hangen bij aanvang van de opdracht 'Vlag Uithangen':
# 1: Rick, 2: Evelien, Jamie, Merel, Niels, Nikkie, Robert, Sarah, Sinan
# 12 - Won de Mol het duel bij de opdracht 'Stapelgek':
# 1: Robert, Sarah, Rick, Evelien; 2: Jamie, Merel, Nikkie, Sinan; 3: Niels
# 16 - Waarvoor stemde de Mol tijdens de opdracht 'Op Treden':
# 1: Evelien, Jamie, Niels, Robert, Sarah; 2: Sinan, Rick, Merel, Nikkie
# 19 - Pakte de Mol het geld aan het einde van de opdracht 'Op Treden':
# 1: Sarah; 2: Evelien, Jamie, Merel, Niels, Nikie, Rick, Robert, Sinan
# 20 - Wie is de Mol:
# 1: Evelien; 2: Jamie; 3: Merel; 4: Niels; 5: Nikkie; 6: Rick; 7: Robert; 8: Sarah; 9: Sinan
# Antwoorden: Rick (4, 4), Niels (16, 1), Nikkie (12, 1), Robert (1 Joker), Merel (Vrijstelling), Jamie (7, 1),
# Sarah (19, 2) (1 Joker), Evelien (20, 9) (2 Jokers)
players3 = ['Evelien', 'Jamie', 'Merel', 'Niels', 'Nikkie', 'Rick', 'Robert', 'Sarah', 'Sinan']
question3_4 = Question({1: ['Evelien'], 2: ['Jamie'], 3: ['Merel'], 4: ['Sinan'], 5: ['Niels'], 6: ['Nikkie'],
                        7: ['Rick'], 8: ['Robert'], 9: ['Sarah']})
question3_7 = Question({1: ['Rick'],
                        2: ['Evelien', 'Jamie', 'Merel', 'Sinan', 'Niels', 'Nikkie', 'Robert', 'Sarah']})
question3_12 = Question({1: ['Robert', 'Sarah', 'Rick', 'Evelien'],
                         2: ['Jamie', 'Merel', 'Nikkie', 'Sinan'],
                         3: ['Niels']})
question3_16 = Question({1: ['Evelien', 'Jamie', 'Niels', 'Robert', 'Sarah'],
                         2: ['Sinan', 'Rick', 'Merel', 'Nikkie']})
question3_19 = Question({1: ['Sarah'],
                         2: ['Evelien', 'Jamie', 'Merel', 'Niels', 'Nikkie', 'Rick', 'Robert', 'Sinan']})
question3_20 = Question({1: ['Evelien'], 2: ['Jamie'], 3: ['Merel'], 4: ['Niels'], 5: ['Nikkie'], 6: ['Rick'],
                         7: ['Robert'], 8: ['Sarah'], 9: ['Sinan']})
result3 = Result(True, ['Nikkie'])
episode3 = Episode(players3, result3,
                   {'Rick': TestInput({4: 4}), 'Niels': TestInput({16: 1}), 'Nikkie': TestInput({12: 1}),
                    'Robert': TestInput(jokers = 1), 'Merel': TestInput(jokers = 20), 'Jamie': TestInput({7: 1}),
                    'Sarah': TestInput({19: 2}, 1), 'Evelien': TestInput({20: 9}, 2)},
                   {4: question3_4, 7: question3_7, 12: question3_12, 16: question3_16, 19: question3_19,
                    20: question3_20})

# Aflevering 4 (afvaller: Evelien)
# Vragen:
# 5 - Als hoeveelste werd de kooi van de Mol geopend tijdens de opdracht 'Min of Meer':
# 1: Niels, Evelien; 2: Sarah, Robert; 3: Rick, Merel; 4: Jamie, Sinan
# 7 - Op welk bedrag had het duo van de Mol de geldklok stilgezet, tijdens de opdracht 'Min of Meer':
# 1 (-100): Niels, Evelien; 2 (-150): Robert, Sarah; 3 (-250): Merel, Rick; 4 (geen klok): Jamie, Sinan
# 18 - Voerde de Mol het laatste foute antwoord in tijdens de opdracht 'Koffiepedia':
# 1: Sarah; 2: Evelien, Jamie, Merel, Niels, Rick, Robert, Sinan;
# Antwoorden: Jamie (5, 1), Robert (7, 2), Niels (1 Joker), Evelien (18, 2)
players4 = ['Evelien', 'Jamie', 'Merel', 'Niels', 'Rick', 'Robert', 'Sarah', 'Sinan']
question4_5 = Question({1: ['Niels', 'Evelien'],
                        2: ['Sarah', 'Robert'],
                        3: ['Rick', 'Merel'],
                        4: ['Jamie', 'Sinan']})
question4_7 = Question({1: ['Niels', 'Evelien'],
                        2: ['Robert', 'Sarah'],
                        3: ['Rick', 'Merel'],
                        4: ['Jamie', 'Sinan']})
question4_18 = Question({1: ['Sarah'],
                         2: ['Evelien', 'Jamie', 'Merel', 'Niels', 'Rick', 'Robert', 'Sinan']})
result4 = Result(True, ['Evelien'])
episode4 = Episode(players4, result4,
                   {'Jamie': TestInput({5: 1}), 'Robert': TestInput({7: 2}), 'Niels': TestInput(jokers = 1),
                    'Evelien': TestInput({18: 2})},
                   {5: question4_5, 7: question4_7, 18: question4_18})

# Aflevering 5 (afvaller: Robert)
# Vragen:
# 6 - Hield de Mol een foto in zijn hand tijdens de afronding van de opdracht 'Pittoresk'
# 1: Jamie; 2: Merel, Niels, Rick, Robert, Sinan
# 12 - Wat was de kleur van de auto waar de Mol in reed tijdens de opdracht 'Parkeergeld'
# 1: Jamie; 2: Rick; 3: Merel, Sarah, Niels, Sinan, Robert
# 17 - Welke abseil-lijn nam de Mol vanaf beneden gezien tijdens 'Sleutelhanger'
# 1: Sarah, Merel, Rick; 2: Jamie, Robert, Niels; 3: Sinan
# 20 - Wie is de Mol:
# 1: Jamie; 2: Merel; 3: Niels; 4: Rick; 5: Robert; 6: Sarah; 7: Sinan
# Antwoorden: Sarah (6, 2), Rick (17, 2), Sinan (12, 3), Jamie (20, 4)
players5 = ['Jamie', 'Merel', 'Niels', 'Rick', 'Robert', 'Sarah', 'Sinan']
question5_6 = Question({1: ['Jamie'],
                        2: ['Merel', 'Niels', 'Rick', 'Robert', 'Sarah', 'Sinan']})
question5_12 = Question({1: ['Jamie'],
                         2: ['Rick'],
                         3: ['Merel', 'Sarah', 'Niels', 'Robert', 'Sinan']})
question5_17 = Question({1: ['Sarah', 'Merel', 'Rick'],
                         2: ['Jamie', 'Robert', 'Niels'],
                         3: ['Sinan']})
question5_20 = Question({1: ['Jamie'], 2: ['Merel'], 3: ['Niels'], 4: ['Rick'], 5: ['Robert'], 6: ['Sarah'],
                         7: ['Sinan']})
result5 = Result(True, ['Robert'])
episode5 = Episode(players5, result5,
                   {'Sarah': TestInput({6: 2}), 'Rick': TestInput({17: 2}), 'Sinan': TestInput({12: 3}),
                    'Jamie': TestInput({20: 4})},
                    {6: question5_6, 12: question5_12, 17: question5_17, 20: question5_20})

# Aflevering 7 (afvallers: Jamie, Rick)
# Vragen:
# 6 - Naar wie kon de Mol kisten verplaatsen tijdens de opdracht 'Getouwtrek':
# 1: Rick; 2: Merel; 3: Sarah; 4: Jamie; 5: Niels; 6: Sinan
# 11 - Als hoeveelste kwam de Mol bij Rik tijdens de opdracht 'Roulette':
# 1: Niels; 2: Jamie; 3: Sinan; 4: Merel; 5: Sarah; 6: Rick
# 12 - Wat was de keuze van de Mol tijdens de opdracht 'Roulette':
# 1: Niels, Sinan; 2: Rick, Jamie, Merel; 3: Sarah
# 18 - Bij welk station begon de Mol tijdens de opdracht 'Geld Oogsten':
# 1: Rick; 2: Sarah; 3: Sinan; 4: Merel; 5: Niels, Jamie
# 20 - Wie is de Mol:
# 1: Jamie; 2: Merel; 3: Niels; 4: Rick; 5: Sarah; 6: Sinan
# Antwoorden: Merel (11, 2), Rick (20, 1) (1 Joker), Sinan (12, 2), Sarah (6, 2), Niels (18, 5) (2 Jokers),
# Jamie (20, 4) (2 Jokers)
players7 = ['Jamie', 'Merel', 'Niels', 'Rick', 'Sarah', 'Sinan']
question7_6 = Question({1: ['Rick'], 2: ['Merel'], 3: ['Sarah'], 4: ['Jamie'], 5: ['Niels'], 6: ['Sinan']})
question7_11 = Question({1: ['Niels'], 2: ['Jamie'], 3: ['Sinan'], 4: ['Merel'], 5: ['Sarah'], 6: ['Rick']})
question7_12 = Question({1: ['Niels', 'Sinan'],
                         2: ['Rick', 'Jamie', 'Merel'],
                         3: ['Sarah']})
question7_18 = Question({1: ['Rick'], 2: ['Sarah'], 3: ['Sinan'], 4: ['Merel'], 5: ['Niels', 'Jamie']})
question7_20 = Question({1: ['Jamie'], 2: ['Merel'], 3: ['Niels'], 4: ['Rick'], 5: ['Sarah'], 6: ['Sinan']})
result7 = Result(True, ['Jamie', 'Rick'])
episode7 = Episode(players7, result7,
                   {'Merel': TestInput({11: 2}), 'Rick': TestInput({20: 1}, 1), 'Sinan': TestInput({12: 2}),
                    'Sarah': TestInput({6: 2}), 'Niels': TestInput({18: 5}, 2), 'Jamie': TestInput({20: 4}, 2)},
                    {6: question7_6, 11: question7_11, 12: question7_12, 18: question7_18, 20: question7_20})

# Aflevering 8 (afvaller: Sinan)
# Vragen:
# 3 - In welke ronde betrad de Mol het speelveld tijdens de opdracht 'In het vizier'?
# 1: Niels, Merel; 2: Sarah; 3: Sinan
# 4 - Als hoeveelste mocht de Mol een pin pakken tijdens de opdracht 'Ten val brengen'? (Inacurraat)
# 1: Sarah; 2: Merel; 3: Niels; 4: Sinan
# 5 - Met wie vormde de Mol een duo tijdens de opdracht 'Vuurproef'? (Inaccuraat)
# 1: Niels; 2: Merel; 3: Sinan; 4: Sarah
# Antwoord: Merel (4, 1), Sinan (5, 2), Sarah (3, 1), Niels (Vrijstelling)
players8 = ['Merel', 'Niels', 'Sarah', 'Sinan']
question8_3 = Question({1: ['Niels', 'Merel'], 2: ['Sarah'], 3: ['Sinan']})
question8_4 = Question({1: ['Sarah'], 2: ['Merel'], 3: ['Niels'], 4: ['Sinan']})
question8_5 = Question({1: ['Niels'], 2: ['Merel'], 3: ['Sinan'], 4: ['Sarah']})
result8 = Result(True, ['Sinan'])
episode8 = Episode(players8, result8,
                   {'Merel': TestInput({4: 1}), 'Sinan': TestInput({5: 2}), 'Sarah': TestInput({3: 1}),
                    'Niels': TestInput(jokers = 20)},
                    {3: question8_3, 4: question8_4, 5: question8_5})


season19 = (players1, {1: episode1, 2: episode2, 3: episode3, 4: episode4, 5: episode5, 7: episode7, 8: episode8})