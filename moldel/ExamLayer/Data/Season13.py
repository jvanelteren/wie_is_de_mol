from Candidates import *
from ExamLayer.Structure import Question, Result, Episode, TestInput

# Aflevering 1 (afvaller: Ewout)
# Vragen:
# 2 - Hoeveel enveloppen heeft de Mol geopend tijdens de Dropping (niet heel zeker van de personen bij de antwoorden):
# 1: Zarayda, Janine, Daniel; 2: Carolien, Joep, Tim, Paulien, Tania; 3: Kees; 4: Ewout;
# 14 - Sprong de Mol tijdens de Bungeejump-opdracht:
# 1: Daniel, Kees, Carolien; 2: Tania, Zarayda, Joep, Paulien, Janine, Tim, Ewout;
# 18 - Heeft de Mol een vrijstelling verdiend vandaag:
# 1: Carolien, Janine, Paulien, Tim; 2: Daniel, Ewout, Joep, Kees, Tania, Zarayda;
# 20 - Wie is de Mol:
# 1: Carolien; 2: Daniel; 3: Ewout; 4: Janine; 5: Joep; 6: Kees; 7: Paulien; 8: Tania; 9: Tim; 10: Zarayda;
# Antwoorden: Carolien (Vrijstelling), Janine (Vrijstelling), Paulien (Vrijstelling), Tim (Vrijstelling), Joep (2, 2),
# Zarayda (14, 2), Tania (18, 1), Kees (20, 3)
players1 = [Candidates.CAROLIEN_13, Candidates.DANIEL_13, Candidates.EWOUT_13, Candidates.JANINE_13, Candidates.JOEP_13,
            Candidates.KEES_13, Candidates.PAULIEN_13, Candidates.TANIA_13, Candidates.TIM_13, Candidates.ZARAYDA_13]
question1_2 = Question({1: [Candidates.ZARAYDA_13, Candidates.JANINE_13, Candidates.DANIEL_13],
                        2: [Candidates.CAROLIEN_13, Candidates.JOEP_13, Candidates.TIM_13, Candidates.PAULIEN_13,
                            Candidates.TANIA_13],
                        3: [Candidates.KEES_13],
                        4: [Candidates.EWOUT_13]})
question1_14 = Question({1: [Candidates.DANIEL_13, Candidates.KEES_13, Candidates.CAROLIEN_13],
                         2: [Candidates.TANIA_13, Candidates.ZARAYDA_13, Candidates.JOEP_13, Candidates.PAULIEN_13,
                             Candidates.JANINE_13, Candidates.TIM_13, Candidates.EWOUT_13]})
question1_18 = Question({1: [Candidates.CAROLIEN_13, Candidates.JANINE_13, Candidates.PAULIEN_13, Candidates.TIM_13],
                         2: [Candidates.DANIEL_13, Candidates.EWOUT_13, Candidates.JOEP_13, Candidates.KEES_13,
                             Candidates.TANIA_13, Candidates.ZARAYDA_13]})
question1_20 = Question({1: [Candidates.CAROLIEN_13], 2: [Candidates.DANIEL_13], 3: [Candidates.EWOUT_13],
                         4: [Candidates.JANINE_13], 5: [Candidates.JOEP_13], 6: [Candidates.KEES_13],
                         7: [Candidates.PAULIEN_13], 8: [Candidates.TANIA_13], 9: [Candidates.TIM_13],
                         10: [Candidates.ZARAYDA_13]})
result1 = Result(True, [Candidates.EWOUT_13])
episode1 = Episode(players1, result1,
                   {Candidates.CAROLIEN_13: TestInput(immunity = True), Candidates.JANINE_13: TestInput(immunity = True),
                    Candidates.PAULIEN_13: TestInput(immunity = True), Candidates.TIM_13: TestInput(immunity = True),
                    Candidates.JOEP_13: TestInput({2: 2}), Candidates.ZARAYDA_13: TestInput({14: 2}),
                    Candidates.TANIA_13: TestInput({18: 1}), Candidates.KEES_13: TestInput({20: 3})},
                   {2: question1_2, 14: question1_14, 18: question1_18, 20: question1_20})

# Aflevering 2 (afvaller: Joep)
# Vragen:
# 6 - Was de Mol een dicteedeskundige:
# 1: Carolien, Joep, Paulien; 2: Daniel, Janine, Kees, Tania, Tim, Zarayda;
# 9 - Wat gaf de klok aan toen de Mol ging lopen tijdens de Laser-opdracht:
# 1: Zarayda, Tania; 2: Kees, Paulien; 3: Daniel, Janine; 4: Tim, Joep; 5: Carolien;
# 14 - Heeft de Mol geld binnen gebracht bij de Minedumps-opdracht:
# 1: Tim, Daniel, Joep, Kees; 2: Paulien, Carolien, Janine, Tania, Zarayda;
# 20 - Wie is de Mol:
# 1: Carolien; 2: Daniel; 3: Janine; 4: Joep; 5: Kees; 6: Paulien; 7: Tania; 8: Tim; 9: Zarayda;
# Antwoorden: Kees (6, 2) (2 jokers), Janine (9, 2), Paulien (14, 2), Joep (20, 3)
players2 = [Candidates.CAROLIEN_13, Candidates.DANIEL_13, Candidates.JANINE_13, Candidates.JOEP_13, Candidates.KEES_13,
            Candidates.PAULIEN_13, Candidates.TANIA_13, Candidates.TIM_13, Candidates.ZARAYDA_13]
question2_6 = Question({1: [Candidates.CAROLIEN_13, Candidates.JOEP_13, Candidates.PAULIEN_13],
                        2: [Candidates.DANIEL_13, Candidates.JANINE_13, Candidates.KEES_13, Candidates.TANIA_13,
                            Candidates.TIM_13, Candidates.ZARAYDA_13]})
question2_9 = Question({1: [Candidates.ZARAYDA_13, Candidates.TANIA_13],
                        2: [Candidates.KEES_13, Candidates.PAULIEN_13],
                        3: [Candidates.DANIEL_13, Candidates.JANINE_13],
                        4: [Candidates.TIM_13, Candidates.JOEP_13],
                        5: [Candidates.CAROLIEN_13]})
question2_14 = Question({1: [Candidates.TIM_13, Candidates.DANIEL_13, Candidates.JOEP_13, Candidates.KEES_13],
                         2: [Candidates.PAULIEN_13, Candidates.CAROLIEN_13, Candidates.JANINE_13, Candidates.TANIA_13,
                             Candidates.ZARAYDA_13]})
question2_20 = Question({1: [Candidates.CAROLIEN_13], 2: [Candidates.DANIEL_13], 3: [Candidates.JANINE_13],
                         4: [Candidates.JOEP_13], 5: [Candidates.KEES_13], 6: [Candidates.PAULIEN_13],
                         7: [Candidates.TANIA_13], 8: [Candidates.TIM_13], 9: [Candidates.ZARAYDA_13]})
result2 = Result(True, [Candidates.JOEP_13])
episode2 = Episode(players2, result2,
                   {Candidates.KEES_13: TestInput({6: 2}, jokers = 2), Candidates.JANINE_13: TestInput({9: 2}),
                    Candidates.PAULIEN_13: TestInput({14: 2}), Candidates.JOEP_13: TestInput({20: 3})},
                   {6: question2_6, 9: question2_9, 14: question2_14, 20: question2_20})

# Aflevering 3 - First (afvaller: Janine, door ongeluk vrijwillig afgevallen)
players3f = [Candidates.CAROLIEN_13, Candidates.DANIEL_13, Candidates.JANINE_13, Candidates.KEES_13,
             Candidates.PAULIEN_13, Candidates.TANIA_13, Candidates.TIM_13, Candidates.ZARAYDA_13]
result3f = Result(True, [Candidates.JANINE_13])
episode3f = Episode(players3f, result3f,
                    {Candidates.CAROLIEN_13: TestInput(immunity = True), Candidates.DANIEL_13: TestInput(immunity = True),
                     Candidates.KEES_13: TestInput(immunity = True), Candidates.PAULIEN_13: TestInput(immunity = True),
                     Candidates.TANIA_13: TestInput(immunity = True), Candidates.TIM_13: TestInput(immunity = True),
                     Candidates.ZARAYDA_13: TestInput(immunity = True)}, dict(), skip_regression = True)

# Aflevering 3 - Second (afvaller: Tim)
# Vragen:
# 3 - Wat was het kamernummer van de Mol in het bungalowpark (Niet bruikbaar)
# 6 - Waar bevond de Mol zich tijdens de Boot-opdracht:
# 1: Zarayda, Kees, Carolien; 2: Paulien, Daniel; 3: Tania, Tim;
# 9 - Wat is de burgerlijke staat van de Mol:
# 1: Carolien, Kees; 2: Paulien, Tim, Zarayda; 3: Daniel, Tania;
# 11 - Met hoeveel kandidaten zat de Mol in een Jeep tijdens de Safari-opdracht:
# 1: Tania, Daniel, Zarayda; 2: Paulien, Kees, Tim, Carolien;
# 14 - Hoeveel jokers heeft de Mol overgehouden aan de Watersprong-opdracht:
# 1: Zarayda, Tania, Tim; 2: Paulien, Daniel, Kees; 3: Carolien;
# 20 - Wie is de Mol:
# 1: Carolien; 2: Daniel; 3: Kees; 4: Paulien; 5: Tania; 6: Tim; 7: Zarayda;
# Antwoorden: Zarayda (6, 3), Tim (1 joker), Paulien (9, 1), Daniel (14, 2), Kees (2 jokers),
# Carolien (11, 2) (2 jokers), Tania (20, 6)
players3s = [Candidates.CAROLIEN_13, Candidates.DANIEL_13, Candidates.KEES_13, Candidates.PAULIEN_13,
             Candidates.TANIA_13, Candidates.TIM_13, Candidates.ZARAYDA_13]
question3_6 = Question({1: [Candidates.ZARAYDA_13, Candidates.KEES_13, Candidates.CAROLIEN_13],
                        2: [Candidates.PAULIEN_13, Candidates.DANIEL_13],
                        3: [Candidates.TANIA_13, Candidates.TIM_13]})
question3_9 = Question({1: [Candidates.CAROLIEN_13, Candidates.KEES_13],
                        2: [Candidates.PAULIEN_13, Candidates.TIM_13, Candidates.ZARAYDA_13],
                        3: [Candidates.DANIEL_13, Candidates.TANIA_13]})
question3_11 = Question({1: [Candidates.TANIA_13, Candidates.DANIEL_13, Candidates.ZARAYDA_13],
                         2: [Candidates.PAULIEN_13, Candidates.KEES_13, Candidates.TIM_13, Candidates.CAROLIEN_13]})
question3_14 = Question({1: [Candidates.ZARAYDA_13, Candidates.TANIA_13, Candidates.TIM_13],
                         2: [Candidates.PAULIEN_13, Candidates.DANIEL_13, Candidates.KEES_13],
                         3: [Candidates.CAROLIEN_13]})
question3_20 = Question({1: [Candidates.CAROLIEN_13], 2: [Candidates.DANIEL_13], 3: [Candidates.KEES_13],
                         4: [Candidates.PAULIEN_13], 5: [Candidates.TANIA_13], 6: [Candidates.TIM_13],
                         7: [Candidates.ZARAYDA_13]})
result3s = Result(True, [Candidates.TIM_13])
episode3s = Episode(players3s, result3s,
                    {Candidates.ZARAYDA_13: TestInput({6: 3}), Candidates.TIM_13: TestInput(jokers = 1),
                     Candidates.PAULIEN_13: TestInput({9: 1}), Candidates.DANIEL_13: TestInput({14: 2}),
                     Candidates.KEES_13: TestInput(jokers = 2), Candidates.CAROLIEN_13: TestInput({11: 2}, jokers = 2),
                     Candidates.TANIA_13: TestInput({20: 6})},
                    {6: question3_6, 9: question3_9, 11: question3_11, 14: question3_14, 20: question3_20})

# Aflevering 4 (geen afvaller, alleen Kees kreeg zijn scherm te zien)
# Vragen:
# 20 - Wie is de Mol:
# 1: Carolien; 2: Daniel; 3: Kees; 4: Paulien; 5: Tania; 6: Tim; 7: Zarayda;
# Antwoorden: Tania (20, 6), Tim (20, 1), Carolien (20, 6) (1 joker), Kees (20, 1), Paulien (20, 3), Daniel (20, 4),
# Zarayda (20, 6)
players4 = [Candidates.CAROLIEN_13, Candidates.DANIEL_13, Candidates.KEES_13, Candidates.PAULIEN_13,
             Candidates.TANIA_13, Candidates.TIM_13, Candidates.ZARAYDA_13]
question4_20 = Question({1: [Candidates.CAROLIEN_13], 2: [Candidates.DANIEL_13], 3: [Candidates.KEES_13],
                         4: [Candidates.PAULIEN_13], 5: [Candidates.TANIA_13], 6: [Candidates.TIM_13],
                         7: [Candidates.ZARAYDA_13]})
result4 = Result(False, [Candidates.CAROLIEN_13, Candidates.DANIEL_13, Candidates.PAULIEN_13, Candidates.TANIA_13,
                         Candidates.TIM_13, Candidates.ZARAYDA_13])
episode4 = Episode(players4, result4,
                    {Candidates.TANIA_13: TestInput({20: 6}), Candidates.TIM_13: TestInput({20: 1}),
                     Candidates.CAROLIEN_13: TestInput({20: 6}, jokers = 1), Candidates.KEES_13: TestInput({20: 1}),
                     Candidates.PAULIEN_13: TestInput({20: 3}), Candidates.DANIEL_13: TestInput({20: 4}),
                     Candidates.ZARAYDA_13: TestInput({20: 6})},
                    {20: question4_20})

# Aflevering 5 (afvaller: Tim)
# Vragen:
# 4 - Wat was het nummerbord van de jeep waarmee de Mol reed tijdens de Puzzelroute:
# 1: Daniel, Kees, Tim; 2: Carolien, Tania, Paulien, Zarayda;
# 6 - Heeft de Mol de totstandkoming van de routekaart vertraagd door een puzzelstuk verkeerd te leggen:
# 1: Carolien, Kees, Tim; 2: Daniel, Paulien, Tania, Zarayda;
# 15 - Heeft de Mol drie jokers verdiend tijdens het kampvuurspel:
# 1: Paulien; 2: Carolien, Daniel, Kees, Tania, Tim, Zarayda;
# 19 - Hoeveel stukjes metaal heeft de Mol gevonden tijdens de Sleutelmaken-opdracht:
# 1: Zarayda; 2: Daniel, Paulien, Tim; 3: Carolien, Kees; 4: Tania;
# 20 - Wie is de Mol:
# 1: Carolien; 2: Daniel; 3: Kees; 4: Paulien; 5: Tania; 6: Tim; 7: Zarayda;
# Antwoorden: Daniel (4, 2), Paulien (6, 1) (3 jokers), Kees (15, 1), Tania (20, 6), Tim (19, 3)
players5 = [Candidates.CAROLIEN_13, Candidates.DANIEL_13, Candidates.KEES_13, Candidates.PAULIEN_13,
             Candidates.TANIA_13, Candidates.TIM_13, Candidates.ZARAYDA_13]
question5_4 = Question({1: [Candidates.DANIEL_13, Candidates.KEES_13, Candidates.TIM_13],
                        2: [Candidates.CAROLIEN_13, Candidates.TANIA_13, Candidates.PAULIEN_13, Candidates.ZARAYDA_13]})
question5_6 = Question({1: [Candidates.CAROLIEN_13, Candidates.KEES_13, Candidates.TIM_13],
                        2: [Candidates.DANIEL_13, Candidates.PAULIEN_13, Candidates.TANIA_13, Candidates.ZARAYDA_13]})
question5_15 = Question({1: [Candidates.PAULIEN_13],
                         2: [Candidates.CAROLIEN_13, Candidates.DANIEL_13, Candidates.KEES_13, Candidates.TANIA_13,
                             Candidates.TIM_13, Candidates.ZARAYDA_13]})
question5_19 = Question({1: [Candidates.ZARAYDA_13],
                         2: [Candidates.DANIEL_13, Candidates.PAULIEN_13, Candidates.TIM_13],
                         3: [Candidates.CAROLIEN_13, Candidates.KEES_13],
                         4: [Candidates.TANIA_13]})
question5_20 = Question({1: [Candidates.CAROLIEN_13], 2: [Candidates.DANIEL_13], 3: [Candidates.KEES_13],
                         4: [Candidates.PAULIEN_13], 5: [Candidates.TANIA_13], 6: [Candidates.TIM_13],
                         7: [Candidates.ZARAYDA_13]})
result5 = Result(True, [Candidates.TIM_13])
episode5 = Episode(players5, result5,
                    {Candidates.DANIEL_13: TestInput({4: 2}), Candidates.PAULIEN_13: TestInput({6: 1}, jokers = 3),
                     Candidates.KEES_13: TestInput({15: 1}), Candidates.TANIA_13: TestInput({20: 6}),
                     Candidates.TIM_13: TestInput({19: 3})},
                    {4: question5_4, 6: question5_6, 15: question5_15, 19: question5_19, 20: question5_20})

# Aflevering 6 (afvaller: Tania)
# Vragen:
# 3 - Als hoeveelste ging de Mol naar de cockpit tijdens de Dakota-opdracht:
# 1: Paulien; 2: Carolien; 3: Zarayda; 4: Tania; 5: Kees; 6: Daniel;
# 8 - Wat heeft de Mol altijd bij zich (Niet bruikbaar)
# 12 - Wat is de favoriete krant van de Mol (Niet bruikbaar)
# 13 - Deelde de Mol alle informatie via de intercom tijdens de Dakota-opdracht:
# 1: Paulien, Tania, Kees, Daniel; 2: Carolien, Zarayda;
# 20 - Wie is de Mol:
# 1: Carolien; 2: Daniel; 3: Kees; 4: Paulien; 5: Tania; 6: Zarayda;
# Antwoorden: Carolien (13, 1), Kees (20, 1), Tania (3, 6)
players6 = [Candidates.CAROLIEN_13, Candidates.DANIEL_13, Candidates.KEES_13, Candidates.PAULIEN_13,
            Candidates.TANIA_13, Candidates.ZARAYDA_13]
question6_3 = Question({1: [Candidates.PAULIEN_13], 2: [Candidates.CAROLIEN_13], 3: [Candidates.ZARAYDA_13],
                        4: [Candidates.TANIA_13], 5: [Candidates.KEES_13], 6: [Candidates.DANIEL_13]})
question6_13 = Question({1: [Candidates.PAULIEN_13, Candidates.TANIA_13, Candidates.KEES_13, Candidates.DANIEL_13],
                         2: [Candidates.CAROLIEN_13, Candidates.ZARAYDA_13]})
question6_20 = Question({1: [Candidates.CAROLIEN_13], 2: [Candidates.DANIEL_13], 3: [Candidates.KEES_13],
                         4: [Candidates.PAULIEN_13], 5: [Candidates.TANIA_13], 6: [Candidates.ZARAYDA_13]})
result6 = Result(True, [Candidates.TANIA_13])
episode6 = Episode(players6, result6,
                    {Candidates.CAROLIEN_13: TestInput({13: 1}), Candidates.KEES_13: TestInput({20: 1}),
                     Candidates.TANIA_13: TestInput({3: 6})},
                    {3: question6_3, 13: question6_13, 20: question6_20})

# Aflevering 7 (afvaller: Daniel)
# Vragen:
# 8 - Als hoeveelste viel de Mol af tijdens de vrijstellings-opdracht:
# 1: Paulien; 2: Zarayda; 3: Carolien, Daniel, Kees;
# 14 - Als hoeveelste ging de Mol het veld in tijdens de Jacht-opdracht:
# 1: Kees; 2: Zarayda; 3: Paulien; 4: Carolien; 5: Daniel;
# 17 - Wat was het kamernummer van de Mol vannacht (Niet bruikbaar)
# 20 - Wie is de Mol:
# 1: Carolien; 2: Daniel; 3: Kees; 4: Paulien; 5: Zarayda;
# Antwoorden: Zarayda (8, 3), Carolien (20, 3), Daniel (20, 5), Kees (14, 3)
players7 = [Candidates.CAROLIEN_13, Candidates.DANIEL_13, Candidates.KEES_13, Candidates.PAULIEN_13,
            Candidates.ZARAYDA_13]
question7_8 = Question({1: [Candidates.PAULIEN_13],
                        2: [Candidates.ZARAYDA_13],
                        3: [Candidates.CAROLIEN_13, Candidates.DANIEL_13, Candidates.KEES_13]})
question7_14 = Question({1: [Candidates.KEES_13], 2: [Candidates.ZARAYDA_13], 3: [Candidates.PAULIEN_13],
                         4: [Candidates.CAROLIEN_13], 5: [Candidates.DANIEL_13]})
question7_20 = Question({1: [Candidates.CAROLIEN_13], 2: [Candidates.DANIEL_13], 3: [Candidates.KEES_13],
                         4: [Candidates.PAULIEN_13], 5: [Candidates.ZARAYDA_13]})
result7 = Result(True, [Candidates.DANIEL_13])
episode7 = Episode(players7, result7,
                    {Candidates.ZARAYDA_13: TestInput({8: 3}), Candidates.CAROLIEN_13: TestInput({20: 3}),
                     Candidates.DANIEL_13: TestInput({20: 5}), Candidates.KEES_13: TestInput({14: 3})},
                    {8: question7_8, 14: question7_14, 20: question7_20})

# Aflevering 8 (afvaller: Zarayda)
# Vragen:
# 1 - Vond de Mol porto's bij de postkantoor opdracht:
# 1: Paulien; 2: Carolien, Kees, Zarayda;
# 13 - Wie is de held van de Mol (Niet bruikbaar)
# 15 - Wat deed de Mol tijdens de school-opdracht:
# 1: Carolien, Kees; 2: Paulien, Zarayda;
# 16 - Wat is de geboortemaand van de Mol:
# 1: Kees, Paulien; 2: Carolien; 3: Zarayda;
# Antwoorden: Kees (1, 1), Zarayda (15, 1), Carolien (16, 1)
players8 = [Candidates.CAROLIEN_13, Candidates.KEES_13, Candidates.PAULIEN_13, Candidates.ZARAYDA_13]
question8_1 = Question({1: [Candidates.PAULIEN_13],
                        2: [Candidates.CAROLIEN_13, Candidates.KEES_13, Candidates.ZARAYDA_13]})
question8_15 = Question({1: [Candidates.CAROLIEN_13, Candidates.KEES_13],
                         2: [Candidates.PAULIEN_13, Candidates.ZARAYDA_13]})
question8_16 = Question({1: [Candidates.KEES_13, Candidates.PAULIEN_13],
                         2: [Candidates.CAROLIEN_13],
                         3: [Candidates.ZARAYDA_13]})
result8 = Result(True, [Candidates.ZARAYDA_13])
episode8 = Episode(players8, result8,
                   {Candidates.KEES_13: TestInput({1: 1}), Candidates.ZARAYDA_13: TestInput({15: 1}),
                    Candidates.CAROLIEN_13: TestInput({16: 1})},
                   {1: question8_1, 15: question8_15, 16: question8_16})

# Aflevering 9 (afvaller: Carolien) (40 vragen test)
# 24 - Wat was de Mol tijdens het kampvuurspel:
# 1: Paulien; 2: Kees, Carolien;
# 39 - Wat is de geheime aanwijzing van de Mol:
# 1: Carolien; 2: Paulien; 3: Kees;
# 40 - Wie is de Mol:
# 1: Carolien; 2: Kees; 3: Paulien;
# Antwoorden: Kees (24, 1) (40, 3), Paulien (40, 2), Carolien (39, 3) (40, 2)
players9 = [Candidates.CAROLIEN_13, Candidates.KEES_13, Candidates.PAULIEN_13]
question9_24 = Question({1: [Candidates.PAULIEN_13],
                         2: [Candidates.KEES_13, Candidates.CAROLIEN_13]})
question9_39 = Question({1: [Candidates.CAROLIEN_13], 2: [Candidates.PAULIEN_13], 3: [Candidates.KEES_13]})
question9_40 = Question({1: [Candidates.CAROLIEN_13], 2: [Candidates.KEES_13], 3: [Candidates.PAULIEN_13]})
result9 = Result(True, [Candidates.CAROLIEN_13])
episode9 = Episode(players9, result9,
                   {Candidates.KEES_13: TestInput({24: 1, 40: 3}), Candidates.PAULIEN_13: TestInput({40: 2}),
                    Candidates.CAROLIEN_13: TestInput({39: 3, 40: 2})},
                   {24: question9_24, 39: question9_39, 40: question9_40}, 40)

season13 = (players1, {1: episode1, 2: episode2, 2.5: episode3f, 3: episode3s, 4: episode4, 5: episode5, 6: episode6,
                       7: episode7, 8: episode8, 9: episode9})