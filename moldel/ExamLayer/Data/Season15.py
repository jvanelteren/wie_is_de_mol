from Candidates import *
from ExamLayer.Structure import Question, Result, Episode, TestInput

# Aflevering 1 (afvaller: Pieter)
# Vragen:
# 1 - De Mol is een:
# 1: Ajouad, Chris, Pieter, Rik, Viktor; 2: Carolina, Evelien, Margriet, Marlijn, Martine;
# 18 - Heeft de Mol een rode lijn gevonden tijdens de Schermen-opdracht:
# 1: Ajouad, Marlijn, Evelien, Martine, Viktor, Carolina, Chris; 2: Margriet, Rik, Pieter;
# 20 - Wie is de Mol:
# 1: Ajouad; 2: Carolina; 3: Chris; 4: Evelien; 5: Margriet; 6: Marlijn; 7: Martine; 8: Pieter; 9: Rik; 10: Viktor;
# Antwoorden: Viktor (1, 1), Pieter (18, 1), Margriet (20, 2), Rik (20, 6), Marlijn (20, 10) (1 joker)
players1 = [Candidates.AJOUAD_15, Candidates.CAROLINA_15, Candidates.CHRIS_15, Candidates.EVELIEN_15,
            Candidates.MARGRIET_15, Candidates.MARLIJN_15, Candidates.MARTINE_15, Candidates.PIETER_15,
            Candidates.RIK_15, Candidates.VIKTOR_15]
question1_1 = Question({1: [Candidates.AJOUAD_15, Candidates.CHRIS_15, Candidates.PIETER_15,
                            Candidates.RIK_15, Candidates.VIKTOR_15],
                        2: [Candidates.CAROLINA_15, Candidates.EVELIEN_15, Candidates.MARGRIET_15,
                            Candidates.MARLIJN_15, Candidates.MARTINE_15]})
question1_18 = Question({1: [Candidates.AJOUAD_15, Candidates.MARLIJN_15, Candidates.EVELIEN_15, Candidates.MARTINE_15,
                             Candidates.VIKTOR_15, Candidates.CAROLINA_15, Candidates.CHRIS_15],
                         2: [Candidates.MARGRIET_15, Candidates.RIK_15, Candidates.PIETER_15]})
question1_20 = Question({1: [Candidates.AJOUAD_15], 2: [Candidates.CAROLINA_15], 3: [Candidates.CHRIS_15],
                         4: [Candidates.EVELIEN_15], 5: [Candidates.MARGRIET_15], 6: [Candidates.MARLIJN_15],
                         7: [Candidates.MARTINE_15], 8: [Candidates.PIETER_15], 9: [Candidates.RIK_15],
                         10: [Candidates.VIKTOR_15]})
result1 = Result(True, [Candidates.PIETER_15])
episode1 = Episode(players1, result1,
                   {Candidates.VIKTOR_15: TestInput({1: 1}), Candidates.PIETER_15: TestInput({18: 1}),
                    Candidates.MARGRIET_15: TestInput({20: 2}), Candidates.RIK_15: TestInput({20: 6}),
                    Candidates.MARLIJN_15: TestInput({20: 10}, jokers = 1),
                    Candidates.AJOUAD_15: TestInput(immunity = True)},
                   {1: question1_1, 18: question1_18, 20: question1_20})

# Aflevering 2 (afvaller: Evelien)
# Vragen:
# 1 - De Mol is een:
# 1: Ajouad, Chris, Rik, Viktor; 2: Carolina, Evelien, Margriet, Marlijn, Martine;
# 10 - Wanneer was het team van de Mol weer compleet in de Bioscoop:
# 1: Chris, Viktor, Martine; 2: Rik, Margriet, Marlijn; 3: Evelien, Ajouad, Carolina;
# 17 - Wanneer arriveerde het team van de Mol bij de vrachtauto van de laden/lossen-opdracht?
# 1: Viktor, Marlijn, Evelien; 2: Rik, Margriet, Carolina; 3: Martine, Ajouad, Chris;
# 20 - Wie is de Mol:
# 1: Ajouad; 2: Carolina; 3: Chris; 4: Evelien; 5: Margriet; 6: Marlijn; 7: Martine; 8: Rik; 9: Viktor;
# Antwoorden: Chris (10, 3), Carolina (17, 3) (1 joker), Viktor (20, 3), Rik (1, 2), Marlijn (1 joker),
# Margriet (1 joker), Martine (2 jokers), Ajouad (Vrijstelling)
players2 = [Candidates.AJOUAD_15, Candidates.CAROLINA_15, Candidates.CHRIS_15, Candidates.EVELIEN_15,
            Candidates.MARGRIET_15, Candidates.MARLIJN_15, Candidates.MARTINE_15, Candidates.RIK_15,
            Candidates.VIKTOR_15]
question2_1 = Question({1: [Candidates.AJOUAD_15, Candidates.CHRIS_15, Candidates.RIK_15, Candidates.VIKTOR_15],
                        2: [Candidates.CAROLINA_15, Candidates.EVELIEN_15, Candidates.MARGRIET_15,
                            Candidates.MARLIJN_15, Candidates.MARTINE_15]})
question2_10 = Question({1: [Candidates.CHRIS_15, Candidates.VIKTOR_15, Candidates.MARTINE_15],
                         2: [Candidates.RIK_15, Candidates.MARGRIET_15, Candidates.MARLIJN_15],
                         3: [Candidates.EVELIEN_15, Candidates.AJOUAD_15, Candidates.CAROLINA_15]})
question2_17 = Question({1: [Candidates.VIKTOR_15, Candidates.MARLIJN_15, Candidates.EVELIEN_15],
                         2: [Candidates.RIK_15, Candidates.MARGRIET_15, Candidates.CAROLINA_15],
                         3: [Candidates.MARTINE_15, Candidates.AJOUAD_15, Candidates.CHRIS_15]})
question2_20 = Question({1: [Candidates.AJOUAD_15], 2: [Candidates.CAROLINA_15], 3: [Candidates.CHRIS_15],
                         4: [Candidates.EVELIEN_15], 5: [Candidates.MARGRIET_15], 6: [Candidates.MARLIJN_15],
                         7: [Candidates.MARTINE_15], 8: [Candidates.RIK_15], 9: [Candidates.VIKTOR_15]})
result2 = Result(True, [Candidates.EVELIEN_15])
episode2 = Episode(players2, result2,
                   {Candidates.CHRIS_15: TestInput({10: 3}), Candidates.CAROLINA_15: TestInput({17: 3}, jokers = 1),
                    Candidates.VIKTOR_15: TestInput({20: 3}), Candidates.RIK_15: TestInput({1: 2}),
                    Candidates.MARLIJN_15: TestInput(jokers = 1), Candidates.MARGRIET_15: TestInput(jokers = 1),
                    Candidates.MARTINE_15: TestInput(jokers = 2), Candidates.AJOUAD_15: TestInput(immunity = True)},
                   {1: question2_1, 10: question2_10, 17: question2_17, 20: question2_20})

# Aflevering 3 (niemand viel af, alleen Carolina kreeg haar groene scherm te zien)
# Vragen:
# 1 - De Mol is een:
# 1: Ajouad, Chris, Rik, Viktor; 2: Carolina, Margriet, Marlijn, Martine;
# 6 - Met wie vormde de Mol een team tijdens de Laser-opdracht:
# 1: Viktor; 2: Rik; 3: Marlijn; 4: Martine; 5: Chris; 6: Margriet; 7: Carolina; 8: Ajouad
# 7 - Wanneer betrad het team van de Mol het parcours van de Laser-opdracht:
# 1: Rik, Carolina; 2: Chris, Marlijn; 3: Martine, Margriet; 4: Ajouad, Viktor;
# 9 - Is de Mol geraakt door een boobytrap tijdens de Laser-opdracht:
# 1: Rik, Marlijn; 2: Viktor, Martine, Chris, Margriet, Carolina, Ajouad;
# 13 - Wat was de Molactie tijdens de Watervliegtuig-opdracht:
# 1: Ajouad, Viktor, Marlijn, Martine, Margriet, Carolina; 2: Rik, Chris;
# 20 - Wie is de Mol:
# 1: Ajouad; 2: Carolina; 3: Chris; 4: Margriet; 5: Marlijn; 6: Martine; 7: Rik; 8: Viktor;
# Antwoorden: Carolina (6, 6) (20, 4), Martine (7, 2), Viktor (9, 1), Margriet (13, 2), Ajouad (1, 2), Marlijn (9, 2)
players3 = [Candidates.AJOUAD_15, Candidates.CAROLINA_15, Candidates.CHRIS_15, Candidates.MARGRIET_15,
            Candidates.MARLIJN_15, Candidates.MARTINE_15, Candidates.RIK_15, Candidates.VIKTOR_15]
question3_1 = Question({1: [Candidates.AJOUAD_15, Candidates.CHRIS_15, Candidates.RIK_15, Candidates.VIKTOR_15],
                        2: [Candidates.CAROLINA_15, Candidates.MARGRIET_15, Candidates.MARLIJN_15,
                            Candidates.MARTINE_15]})
question3_6 = Question({1: [Candidates.VIKTOR_15], 2: [Candidates.RIK_15], 3: [Candidates.MARLIJN_15],
                        4: [Candidates.MARTINE_15], 5: [Candidates.CHRIS_15], 6: [Candidates.MARGRIET_15],
                        7: [Candidates.CAROLINA_15], 8: [Candidates.AJOUAD_15]})
question3_7 = Question({1: [Candidates.RIK_15, Candidates.CAROLINA_15],
                        2: [Candidates.CHRIS_15, Candidates.MARLIJN_15],
                        3: [Candidates.MARTINE_15, Candidates.MARGRIET_15],
                        4: [Candidates.AJOUAD_15, Candidates.VIKTOR_15]})
question3_9 = Question({1: [Candidates.RIK_15, Candidates.MARLIJN_15],
                        2: [Candidates.VIKTOR_15, Candidates.MARTINE_15, Candidates.CHRIS_15, Candidates.MARGRIET_15,
                            Candidates.CAROLINA_15, Candidates.AJOUAD_15]})
question3_13 = Question({1: [Candidates.AJOUAD_15, Candidates.VIKTOR_15, Candidates.MARLIJN_15, Candidates.MARTINE_15,
                             Candidates.MARGRIET_15, Candidates.CAROLINA_15],
                         2: [Candidates.RIK_15, Candidates.CHRIS_15]})
question3_20 = Question({1: [Candidates.AJOUAD_15], 2: [Candidates.CAROLINA_15], 3: [Candidates.CHRIS_15],
                         4: [Candidates.MARGRIET_15], 5: [Candidates.MARLIJN_15], 6: [Candidates.MARTINE_15],
                         7: [Candidates.RIK_15], 8: [Candidates.VIKTOR_15]})
result3 = Result(False, [Candidates.AJOUAD_15, Candidates.CHRIS_15, Candidates.MARGRIET_15, Candidates.MARLIJN_15,
                         Candidates.MARTINE_15, Candidates.RIK_15, Candidates.VIKTOR_15])
episode3 = Episode(players3, result3,
                   {Candidates.CAROLINA_15: TestInput({6: 6, 20: 4}), Candidates.MARTINE_15: TestInput({7: 2}),
                    Candidates.VIKTOR_15: TestInput({9: 1}), Candidates.MARGRIET_15: TestInput({13: 2}),
                    Candidates.AJOUAD_15: TestInput({1: 2}), Candidates.MARLIJN_15: TestInput({9: 2})},
                   {1: question3_1, 6: question3_6, 7: question3_7, 9: question3_9, 13: question3_13, 20: question3_20})

# Aflevering 4 (afvaller: Ajouad)
# Vragen:
# 1 - De Mol is een:
# 1: Ajouad, Chris, Rik, Viktor; 2: Carolina, Margriet, Marlijn, Martine;
# 3 - Wat was de samenstelling van het team van de Mol bij de Vakantiekiekjes-opdracht?
# 1: Marlijn, Viktor; 2: Rik, Carolina, Ajouad; 3: Chris, Martine, Margriet;
# 11 - Heeft de Mol een zwarte vrijstelling in het bezit bij aanvang van deze test:
# 1: Margriet; 2: Ajouad, Carolina, Chris, Martine, Marlijn, Rik, Viktor;
# 17 - Wanneer betrad de Mol de Dagoba tijdens de Russisch Roulette-opdracht:
# 1: Martine; 2: Ajouad; 3: Carolina; 4: Viktor; 5: Rik; 6: Margriet; 7: Marlijn; 8: Chris;
# 20 - Wie is de Mol:
# 1: Ajouad; 2: Carolina; 3: Chris; 4: Margriet; 5: Marlijn; 6: Martine; 7: Rik; 8: Viktor;
# Antwoorden (Zwarte vrijstelling ingezet): Chris (3, 3), Marlijn (20, 7) (1 joker), Rik (11, 2) (1 joker),
# Martine (20, 4) (2 jokers), Viktor (17, 8), Carolina (2 jokers), Ajouad (1, 2) (1 joker), Margriet (11, 2)
players4 = [Candidates.AJOUAD_15, Candidates.CAROLINA_15, Candidates.CHRIS_15, Candidates.MARGRIET_15,
            Candidates.MARLIJN_15, Candidates.MARTINE_15, Candidates.RIK_15, Candidates.VIKTOR_15]
question4_1 = Question({1: [Candidates.AJOUAD_15, Candidates.CHRIS_15, Candidates.RIK_15, Candidates.VIKTOR_15],
                        2: [Candidates.CAROLINA_15, Candidates.MARGRIET_15, Candidates.MARLIJN_15,
                            Candidates.MARTINE_15]})
question4_3 = Question({1: [Candidates.MARLIJN_15, Candidates.VIKTOR_15],
                        2: [Candidates.RIK_15, Candidates.CAROLINA_15, Candidates.AJOUAD_15],
                        3: [Candidates.CHRIS_15, Candidates.MARTINE_15, Candidates.MARGRIET_15]})
question4_11 = Question({1: [Candidates.MARGRIET_15],
                         2: [Candidates.AJOUAD_15, Candidates.CAROLINA_15, Candidates.CHRIS_15, Candidates.MARTINE_15,
                             Candidates.MARLIJN_15, Candidates.RIK_15, Candidates.VIKTOR_15]})
question4_17 = Question({1: [Candidates.MARTINE_15], 2: [Candidates.AJOUAD_15], 3: [Candidates.CAROLINA_15],
                         4: [Candidates.VIKTOR_15], 5: [Candidates.RIK_15], 6: [Candidates.MARGRIET_15],
                         7: [Candidates.MARLIJN_15], 8: [Candidates.CHRIS_15]})
question4_20 = Question({1: [Candidates.AJOUAD_15], 2: [Candidates.CAROLINA_15], 3: [Candidates.CHRIS_15],
                         4: [Candidates.MARGRIET_15], 5: [Candidates.MARLIJN_15], 6: [Candidates.MARTINE_15],
                         7: [Candidates.RIK_15], 8: [Candidates.VIKTOR_15]})
result4 = Result(True, [Candidates.AJOUAD_15])
episode4 = Episode(players4, result4,
                   {Candidates.CHRIS_15: TestInput({3: 3}), Candidates.MARLIJN_15: TestInput({20: 7}),
                    Candidates.RIK_15: TestInput({11: 2}), Candidates.MARTINE_15: TestInput({20: 4}),
                    Candidates.VIKTOR_15: TestInput({17: 8}), Candidates.AJOUAD_15: TestInput({1: 2}),
                    Candidates.MARGRIET_15: TestInput({11: 2})},
                   {1: question4_1, 3: question4_3, 11: question4_11, 17: question4_17, 20: question4_20})

# Aflevering 5 (afvaller: Viktor)
# Vragen:
# 4 - Heeft de Mol een joker aangenomen in ruil voor beloftes rond de Zwarte Vrijstelling:
# 1: Rik; 2: Carolina, Chris, Margriet, Marlijn, Martine, Viktor;
# 6 - Is de Mol de huidige penningmeester:
# 1: Rik; 2: Carolina, Chris, Margriet, Marlijn, Martine, Viktor;
# 7 - Tijdens de opdracht in de tempel:
# 1: Marlijn, Carolina; 2: Viktor, Rik, Margriet, Martine, Chris;
# 15 - Op de groepsfoto van de aflevering staat de Mol:
# 1: Martine, Rik, Carolina, Marlijn; 2: Margriet, Viktor, Chris;
# 17 - Met wie vormde de Mol een duo tijdens de Koeriers-opdracht:
# 1: Viktor; 2: Rik; 3: Martine; 4: Marlijn; 5: Margriet; 6: Carolina; 7: Chris;
# 18 - Wat was de eerste bezorgplaats van de Mol tijdens de Koeriersopdracht:
# 1: Viktor, Carolina; 2: Rik, Margriet; 3: Martine, Marlijn; 4: Chris;
# 20 - Wie is de Mol:
# 1: Carolina; 2: Chris; 3: Margriet; 4: Marlijn; 5: Martine; 6: Rik; 7: Viktor;
# Antwoorden: Rik (18, 4), Marlijn (20, 2), Viktor (7, 2), Margriet (15, 2), Carolina (6, 1), Martine (4, 2)
players5 = [Candidates.CAROLINA_15, Candidates.CHRIS_15, Candidates.MARGRIET_15, Candidates.MARLIJN_15,
            Candidates.MARTINE_15, Candidates.RIK_15, Candidates.VIKTOR_15]
question5_4 = Question({1: [Candidates.RIK_15],
                        2: [Candidates.CAROLINA_15, Candidates.CHRIS_15, Candidates.MARGRIET_15, Candidates.MARLIJN_15,
                            Candidates.MARTINE_15, Candidates.VIKTOR_15]})
question5_6 = Question({1: [Candidates.RIK_15],
                        2: [Candidates.CAROLINA_15, Candidates.CHRIS_15, Candidates.MARGRIET_15, Candidates.MARLIJN_15,
                            Candidates.MARTINE_15, Candidates.VIKTOR_15]})
question5_7 = Question({1: [Candidates.MARLIJN_15, Candidates.CAROLINA_15],
                        2: [Candidates.VIKTOR_15, Candidates.RIK_15, Candidates.MARGRIET_15, Candidates.MARTINE_15,
                            Candidates.CHRIS_15]})
question5_15 = Question({1: [Candidates.MARTINE_15, Candidates.RIK_15, Candidates.CAROLINA_15, Candidates.MARLIJN_15],
                         2: [Candidates.MARGRIET_15, Candidates.VIKTOR_15, Candidates.CHRIS_15]})
question5_17 = Question({1: [Candidates.VIKTOR_15], 2: [Candidates.RIK_15], 3: [Candidates.MARTINE_15],
                         4: [Candidates.MARLIJN_15], 5: [Candidates.MARGRIET_15], 6: [Candidates.CAROLINA_15],
                         7: [Candidates.CHRIS_15]})
question5_18 = Question({1: [Candidates.VIKTOR_15, Candidates.CAROLINA_15],
                         2: [Candidates.RIK_15, Candidates.MARGRIET_15],
                         3: [Candidates.MARTINE_15, Candidates.MARLIJN_15],
                         4: [Candidates.CHRIS_15]})
question5_20 = Question({1: [Candidates.CAROLINA_15], 2: [Candidates.CHRIS_15], 3: [Candidates.MARGRIET_15],
                         4: [Candidates.MARLIJN_15], 5: [Candidates.MARTINE_15], 6: [Candidates.RIK_15],
                         7: [Candidates.VIKTOR_15]})
result5 = Result(True, [Candidates.VIKTOR_15])
episode5 = Episode(players5, result5,
                   {Candidates.RIK_15: TestInput({18: 4}), Candidates.MARLIJN_15: TestInput({20: 2}),
                    Candidates.VIKTOR_15: TestInput({7: 2}), Candidates.MARGRIET_15: TestInput({15: 2}),
                    Candidates.CAROLINA_15: TestInput({6: 1}), Candidates.MARTINE_15: TestInput({4: 2})},
                   {4: question5_4, 6: question5_6, 7: question5_7, 15: question5_15, 17: question5_17,
                    18: question5_18, 20: question5_20})

# Aflevering 6 (afvaller: Carolina)
# Vragen:
# 5 - In welke kleur truck reed de Mol bij het achteruit parkeren:
# 1: Carolina, Chris; 2: Margriet; 3: Rik; 4: Marlijn, Martine;
# 7 - Was de Mol de slechtste chauffeur van Hambantota:
# 1: Martine, Rik, Margriet, Marlijn; 2: Carolina, Chris;
# 16 - Hoeveel kokers heeft de Mol ingeleverd aan het eind van de Lijnen-opdracht:
# 1: Chris; 2: Margriet, Rik; 3: Martine, Marlijn; 4: Carolina;
# 20 - Wie is de Mol:
# 1: Carolina; 2: Chris; 3: Margriet; 4: Marlijn; 5: Martine; 6: Rik;
# Antwoorden: Carolina (7, 2), Chris (5, 2), Margriet (20, 2), Martine (16, 2)
players6 = [Candidates.CAROLINA_15, Candidates.CHRIS_15, Candidates.MARGRIET_15, Candidates.MARLIJN_15,
            Candidates.MARTINE_15, Candidates.RIK_15]
question6_5 = Question({1: [Candidates.CAROLINA_15, Candidates.CHRIS_15],
                        2: [Candidates.MARGRIET_15],
                        3: [Candidates.RIK_15],
                        4: [Candidates.MARLIJN_15, Candidates.MARTINE_15]})
question6_7 = Question({1: [Candidates.MARTINE_15, Candidates.RIK_15, Candidates.MARGRIET_15, Candidates.MARLIJN_15],
                        2: [Candidates.CAROLINA_15, Candidates.CHRIS_15]})
question6_16 = Question({1: [Candidates.CHRIS_15],
                         2: [Candidates.MARGRIET_15, Candidates.RIK_15],
                         3: [Candidates.MARTINE_15, Candidates.MARLIJN_15],
                         4: [Candidates.CAROLINA_15]})
question6_20 = Question({1: [Candidates.CAROLINA_15], 2: [Candidates.CHRIS_15], 3: [Candidates.MARGRIET_15],
                         4: [Candidates.MARLIJN_15], 5: [Candidates.MARTINE_15], 6: [Candidates.RIK_15]})
result6 = Result(True, [Candidates.CAROLINA_15])
episode6 = Episode(players6, result6,
                   {Candidates.CAROLINA_15: TestInput({7: 2}), Candidates.CHRIS_15: TestInput({5: 2}),
                    Candidates.MARGRIET_15: TestInput({20: 2}), Candidates.MARTINE_15: TestInput({16: 2})},
                   {5: question6_5, 7: question6_7, 16: question6_16, 20: question6_20})

# Aflevering 7 (geen schermen en geen afvallers dus ook geen data ingevuld)
players7 = [Candidates.CHRIS_15, Candidates.MARGRIET_15, Candidates.MARLIJN_15, Candidates.MARTINE_15,
            Candidates.RIK_15]
result7 = Result(False, [Candidates.CHRIS_15, Candidates.MARGRIET_15, Candidates.MARLIJN_15, Candidates.MARTINE_15,
                         Candidates.RIK_15])
episode7 = Episode(players7, result7, dict(), dict())

# Aflevering 8 (afvaller: Martine)
# Vragen:
# 1 - De Mol is een:
# 1: Chris, Rik; 2: Margriet, Marlijn, Martine;
# 6 - Wanneer kwam de Mol bij de rekentafel om geld te tellen tijdens de Geld plukken-opdracht:
# 1: Chris; 2: Rik; 3: Martine; 4: Margriet; 5: Marlijn;
# 12 - Was de stift zoek in het team van de Mol tijdens de Straattaal-opdracht:
# 1: Rik, Martine, Chris; 2: Margriet, Marlijn;
# 16 - Wanneer ging de Mol de theefabriek binnen om enveloppen te verzamelen:
# 1: Martine; 2: Margriet; 3: Marlijn; 4: Rik; 5: Chris;
# 18 - Hoeveel enveloppen heeft de Mol gepakt in de theefabriek
# 1: Rik; 2: Margriet, Marlijn; 3: Martine, Chris;
# Antwoorden: Chris (16, 2), Marlijn (6, 4), Rik (12, 2), Margriet (18, 1), Martine (1, 2)
players8 = [Candidates.CHRIS_15, Candidates.MARGRIET_15, Candidates.MARLIJN_15, Candidates.MARTINE_15,
            Candidates.RIK_15]
question8_1 = Question({1: [Candidates.CHRIS_15, Candidates.RIK_15],
                        2: [Candidates.MARGRIET_15, Candidates.MARLIJN_15, Candidates.MARTINE_15]})
question8_6 = Question({1: [Candidates.CHRIS_15], 2: [Candidates.RIK_15], 3: [Candidates.MARTINE_15],
                        4: [Candidates.MARGRIET_15], 5: [Candidates.MARLIJN_15]})
question8_12 = Question({1: [Candidates.RIK_15, Candidates.MARTINE_15, Candidates.CHRIS_15],
                         2: [Candidates.MARGRIET_15, Candidates.MARLIJN_15]})
question8_16 = Question({1: [Candidates.MARTINE_15], 2: [Candidates.MARGRIET_15], 3: [Candidates.MARLIJN_15],
                         4: [Candidates.RIK_15], 5: [Candidates.CHRIS_15]})
question8_18 = Question({1: [Candidates.RIK_15],
                         2: [Candidates.MARGRIET_15, Candidates.MARLIJN_15],
                         3: [Candidates.MARTINE_15, Candidates.CHRIS_15]})
result8 = Result(True, [Candidates.MARTINE_15])
episode8 = Episode(players8, result8,
                   {Candidates.CHRIS_15: TestInput({16: 2}), Candidates.MARLIJN_15: TestInput({6: 4}),
                    Candidates.RIK_15: TestInput({12: 2}), Candidates.MARGRIET_15: TestInput({18: 1}),
                    Candidates.MARTINE_15: TestInput({1: 2})},
                   {1: question8_1, 6: question8_6, 12: question8_12, 16: question8_16, 18: question8_18})

# Aflevering 9 (afvaller: Chris)
# Vragen:
# 1 - De Mol is een:
# 1: Chris, Rik; 2: Margriet, Marlijn;
# 16 - Wat pakte de Mol aanvankelijk aan de Jokertafel:
# 1: Chris, Margriet; 2: Marlijn; 3: Rik;
# 20 - Wie is de Mol:
# 1: Chris; 2: Margriet; 3: Marlijn; 4: Rik;
# Antwoorden: Marlijn (1 joker), Rik (1, 2) (1 joker), Margriet (16, 3) (2 jokers), Chris (20, 2)
players9 = [Candidates.CHRIS_15, Candidates.MARGRIET_15, Candidates.MARLIJN_15, Candidates.RIK_15]
question9_1 = Question({1: [Candidates.CHRIS_15, Candidates.RIK_15],
                        2: [Candidates.MARGRIET_15, Candidates.MARLIJN_15]})
question9_16 = Question({1: [Candidates.CHRIS_15, Candidates.MARGRIET_15],
                         2: [Candidates.MARLIJN_15],
                         3: [Candidates.RIK_15]})
question9_20 = Question({1: [Candidates.CHRIS_15], 2: [Candidates.MARGRIET_15], 3: [Candidates.MARLIJN_15],
                          4: [Candidates.RIK_15]})
result9 = Result(True, [Candidates.CHRIS_15])
episode9 = Episode(players9, result9,
                   {Candidates.MARLIJN_15: TestInput(jokers = 1), Candidates.RIK_15: TestInput({1: 2}, jokers = 1),
                    Candidates.MARGRIET_15: TestInput({16: 3}, jokers = 2)},
                   {1: question9_1, 16: question9_16, 20: question9_20})


season15 = (players1, {1: episode1, 2: episode2, 3: episode3, 4: episode4, 5: episode5, 6: episode6, 7: episode7,
                       8: episode8, 9: episode9})