from Candidates import *
from ExamDistribution.Structure import Question, TestInput, Result, Episode

# Aflevering 1 (afvaller: Vincent)
# Vragen:
# 1 - De Mol is een:
# 1: Diederik, Jeroen, Jochem, Thomas, Vincent; 2: Imanuelle, Roos, Sanne, Sigrid, Yvonne
# 4 - De Mol zat tijdens de eerste opdracht in:
# 1: Jeroen, Thomas, Vincent, Roos; 2: Diederik, Imanuelle, Jochem, Sanne, Sigrid, Yvonne
# 20 - Wie is de Mol:
# 1: Diederik; 2: Imanuelle; 3: Jeroen; 4: Jochem; 5: Roos; 6: Sanne; 7: Sigrid; 8: Thomas; 9: Vincent; 10: Yvonne;
# Vrijstellingen: Thomas, Jeroen, Roos
# Antwoorden: Yvonne (20, 9), Thomas (Vrijstelling), Sanne (1, 2), Jeroen (Vrijstelling), Roos (Vrijstelling),
# Jochem (4, 2)
players1 = [Candidates.DIEDERIK_17, Candidates.IMANUELLE_17, Candidates.JEROEN_17, Candidates.JOCHEM_17,
            Candidates.ROOS_17, Candidates.SANNE_17, Candidates.SIGRID_17, Candidates.THOMAS_17, Candidates.VINCENT_17,
            Candidates.YVONNE_17]
question1_1 = Question({1: [Candidates.DIEDERIK_17, Candidates.JEROEN_17, Candidates.JOCHEM_17, Candidates.THOMAS_17,
                            Candidates.VINCENT_17],
                        2: [Candidates.IMANUELLE_17, Candidates.ROOS_17, Candidates.SANNE_17, Candidates.SIGRID_17,
                            Candidates.YVONNE_17]})
question1_4 = Question({1: [Candidates.JEROEN_17, Candidates.THOMAS_17, Candidates.VINCENT_17, Candidates.ROOS_17],
                        2: [Candidates.DIEDERIK_17, Candidates.IMANUELLE_17, Candidates.JOCHEM_17, Candidates.SANNE_17,
                            Candidates.SIGRID_17, Candidates.YVONNE_17]})
question1_20 = Question({1: [Candidates.DIEDERIK_17], 2: [Candidates.IMANUELLE_17], 3: [Candidates.JEROEN_17],
                         4: [Candidates.JOCHEM_17], 5: [Candidates.ROOS_17], 6: [Candidates.SANNE_17],
                         7: [Candidates.SIGRID_17], 8: [Candidates.THOMAS_17], 9: [Candidates.VINCENT_17],
                         10: [Candidates.YVONNE_17]})
result1 = Result(True, [Candidates.VINCENT_17])
episode1 = Episode(players1, result1,
                   {Candidates.YVONNE_17: TestInput({20: 9}), Candidates.THOMAS_17: TestInput(jokers = 20),
                    Candidates.SANNE_17: TestInput({1: 2}), Candidates.JEROEN_17: TestInput(jokers = 20),
                    Candidates.ROOS_17: TestInput(jokers = 20), Candidates.JOCHEM_17: TestInput({4: 2})},
                   {1: question1_1, 4: question1_4, 20: question1_20})

# Aflevering 2 (afvaller: Yvonne)
# Vragen:
# 1 - De Mol is:
# 1: Diederik, Jeroen, Jochem, Thomas; 2: Imanuelle, Roos, Sanne, Sigrid, Yvonne
# 9 - Verdween de Mol tijdens de opdracht in de papierfabriek:
# 1: Jeroen, Diederik, Roos; 2: Imanuelle, Jochem, Sanne, Sigrid, Thomas, Yvonne
# 12 - Heeft de Mol geld verdiend voor de pot tijdens de opdracht in het pretpark?
# 1: Sanne, Imanuelle, Thomas; 2: Jochem, Sigrid, Yvonne 3: Jeroen, Diederik, Roos
# 14 - Zat de Mol op de voorste rij van de jury tijdens de opdracht bij de rechtbank:
# 1: Yvonne, Imanuelle, Sigrid; 2: Thomas, Sanne, Jochem; 3: Jeroen, Diederik, Roos
# 15 - Als hoeveelste werd de Mol verhoord?
# 1: Jeroen; 2: Roos; 3: Diederik; 4: Imanuelle, Jochem, Sanne, Sigrid, Thomas, Yvonne
# 20 - Wie is de Mol:
# 1: Diederik; 2: Imanuelle; 3: Jeroen; 4: Jochem; 5: Roos; 6: Sanne; 7: Sigrid; 8: Thomas; 9: Yvonne
# Antwoorden: Thomas (14, 1), Yvonne (20, 5), Roos (9, 2), Sanne (1, 2), Sigrid (15, 1), Jeroen (12, 2),
# Diederik (vrijstelling)
players2 = [Candidates.DIEDERIK_17, Candidates.IMANUELLE_17, Candidates.JEROEN_17, Candidates.JOCHEM_17,
            Candidates.ROOS_17, Candidates.SANNE_17, Candidates.SIGRID_17, Candidates.THOMAS_17, Candidates.YVONNE_17]
question2_1 = Question({1: [Candidates.DIEDERIK_17, Candidates.JEROEN_17, Candidates.JOCHEM_17, Candidates.THOMAS_17],
                        2: [Candidates.IMANUELLE_17, Candidates.ROOS_17, Candidates.SANNE_17, Candidates.SIGRID_17,
                            Candidates.YVONNE_17]})
question2_9 = Question({1: [Candidates.JEROEN_17, Candidates.DIEDERIK_17, Candidates.ROOS_17],
                        2: [Candidates.IMANUELLE_17, Candidates.JOCHEM_17, Candidates.SANNE_17, Candidates.SIGRID_17,
                            Candidates.THOMAS_17, Candidates.YVONNE_17]})
question2_12 = Question({1: [Candidates.SANNE_17, Candidates.IMANUELLE_17, Candidates.THOMAS_17],
                         2: [Candidates.JOCHEM_17, Candidates.SIGRID_17, Candidates.YVONNE_17],
                         3: [Candidates.JEROEN_17, Candidates.DIEDERIK_17, Candidates.ROOS_17]})
question2_14 = Question({1: [Candidates.YVONNE_17, Candidates.IMANUELLE_17, Candidates.SIGRID_17],
                         2: [Candidates.THOMAS_17, Candidates.SANNE_17, Candidates.JOCHEM_17],
                         3: [Candidates.JEROEN_17, Candidates.DIEDERIK_17, Candidates.ROOS_17]})
question2_15 = Question({1: [Candidates.JEROEN_17], 2: [Candidates.ROOS_17], 3: [Candidates.DIEDERIK_17],
                         4: [Candidates.IMANUELLE_17, Candidates.JOCHEM_17, Candidates.SANNE_17, Candidates.SIGRID_17,
                             Candidates.THOMAS_17, Candidates.YVONNE_17]})
question2_20 = Question({1: [Candidates.DIEDERIK_17], 2: [Candidates.IMANUELLE_17], 3: [Candidates.JEROEN_17],
                         4: [Candidates.JOCHEM_17], 5: [Candidates.ROOS_17], 6: [Candidates.SANNE_17],
                         7: [Candidates.SIGRID_17], 8: [Candidates.THOMAS_17], 9: [Candidates.YVONNE_17]})
result2 = Result(True, [Candidates.YVONNE_17])
episode2 = Episode(players2, result2,
                   {Candidates.THOMAS_17: TestInput({14: 1}), Candidates.YVONNE_17: TestInput({20: 5}),
                    Candidates.ROOS_17: TestInput({9: 2}), Candidates.SANNE_17: TestInput({1: 2}),
                    Candidates.SIGRID_17: TestInput({15: 1}), Candidates.JEROEN_17: TestInput({12: 2}),
                    Candidates.DIEDERIK_17: TestInput(jokers = 20)},
                   {1: question2_1, 9: question2_9, 12: question2_12, 14: question2_14, 15: question2_15,
                    20: question2_20})

# Aflevering 3 (afvaller: Roos)
# Vragen:
# 11 - Wat deed de Mol tijdens de vuurwerkopdracht:
# 1: Thomas, Jochem, Roos, Sanne, Jeroen, Diederik; 2: Imanuelle, Sigrid
# 17 - Welke aanwijzingen zaten op de auto waar de Mol in zat:
# 1: Sanne, Thomas; 2: Diederik, Roos; 3: Sigrid, Jeroen; 4: Jochem, Imanuelle
# 19 - Heeft de Mol achter het stuur gezeten?
# 1: Diederik, Thomas, Imanuelle, Jeroen 2: Roos, Sanne, Jochem, Sigrid
# 20 - Wie is de Mol:
# 1: Diederik; 2: Imanuelle; 3: Jeroen; 4: Jochem; 5: Roos; 6: Sanne; 7: Sigrid; 8: Thomas
# Antwoorden: Jochem (11, 1), Imanuelle (20, 3), Diederik (17, 3), Roos (19, 2)
players3 = [Candidates.DIEDERIK_17, Candidates.IMANUELLE_17, Candidates.JEROEN_17, Candidates.JOCHEM_17,
            Candidates.ROOS_17, Candidates.SANNE_17, Candidates.SIGRID_17, Candidates.THOMAS_17]
question3_11 = Question({1: [Candidates.THOMAS_17, Candidates.JOCHEM_17, Candidates.ROOS_17, Candidates.SANNE_17,
                             Candidates.JEROEN_17, Candidates.DIEDERIK_17],
                        2: [Candidates.IMANUELLE_17, Candidates.SIGRID_17]})
question3_17 = Question({1: [Candidates.SANNE_17, Candidates.THOMAS_17],
                         2: [Candidates.DIEDERIK_17, Candidates.ROOS_17],
                         3: [Candidates.SIGRID_17, Candidates.JEROEN_17],
                         4: [Candidates.JOCHEM_17, Candidates.IMANUELLE_17]})
question3_19 = Question({1: [Candidates.DIEDERIK_17, Candidates.THOMAS_17, Candidates.IMANUELLE_17,
                             Candidates.JEROEN_17],
                         2: [Candidates.ROOS_17, Candidates.SANNE_17, Candidates.JOCHEM_17, Candidates.SIGRID_17]})
question3_20 = Question({1: [Candidates.DIEDERIK_17], 2: [Candidates.IMANUELLE_17], 3: [Candidates.JEROEN_17],
                         4: [Candidates.JOCHEM_17], 5: [Candidates.ROOS_17], 6: [Candidates.SANNE_17],
                         7: [Candidates.SIGRID_17], 8: [Candidates.THOMAS_17]})
result3 = Result(True, [Candidates.ROOS_17])
episode3 = Episode(players3, result3,
                   {Candidates.JOCHEM_17: TestInput({11: 1}), Candidates.IMANUELLE_17: TestInput({20: 3}),
                    Candidates.DIEDERIK_17: TestInput({17: 3}), Candidates.ROOS_17: TestInput({19: 2})},
                   {11: question3_11, 17: question3_17, 19: question3_19, 20: question3_20})

# Aflevering 4 (afvaller: Sigrid)
# Vragen:
# 1 - De Mol is:
# 1: Diederik, Jeroen, Jochem, Thomas; 2: Imanuelle, Sanne, Sigrid
# 4 - Vond de Mol geld in de hooiberg?
# 1: Jochem, Sigrid; 2: Diederik, Imanuelle, Jeroen, Sanne, Thomas
# 6 - Door wie werd de Mol gevangen tijdens de Lasso-opdracht?
# 1: Jochem, Thomas 2: Sigrid; 3: Jeroen, Sanne, Diederik, Imanuelle
# 18 - Voor hoeveel euro kocht de Mol een joker bij de Koehandel-opdracht?
# 1: Sanne; 2: Diederik; 3: Jochem; 4: Imanuelle, Jeroen, Sigrid, Thomas;
# Antwoorden: Jochem (1 Joker), Imanuelle (4, 2), Diederik (1 Joker), Thomas (1, 1), Sanne (18, 3) (1 Joker),
# Sigrid (6, 3)
players4 = [Candidates.DIEDERIK_17, Candidates.IMANUELLE_17, Candidates.JEROEN_17, Candidates.JOCHEM_17,
            Candidates.SANNE_17, Candidates.SIGRID_17, Candidates.THOMAS_17]
question4_1 = Question({1: [Candidates.DIEDERIK_17, Candidates.JEROEN_17, Candidates.JOCHEM_17, Candidates.THOMAS_17],
                        2: [Candidates.IMANUELLE_17, Candidates.SANNE_17, Candidates.SIGRID_17]})
question4_4 = Question({1: [Candidates.JOCHEM_17, Candidates.SIGRID_17],
                        2: [Candidates.DIEDERIK_17, Candidates.IMANUELLE_17, Candidates.JEROEN_17, Candidates.SANNE_17,
                            Candidates.THOMAS_17]})
question4_6 = Question({1: [Candidates.JOCHEM_17, Candidates.THOMAS_17],
                        2: [Candidates.SIGRID_17],
                        3: [Candidates.JEROEN_17, Candidates.SANNE_17, Candidates.DIEDERIK_17,
                            Candidates.IMANUELLE_17]})
question4_18 = Question({1: [Candidates.SANNE_17],
                         2: [Candidates.DIEDERIK_17],
                         3: [Candidates.JOCHEM_17],
                         4: [Candidates.IMANUELLE_17, Candidates.JEROEN_17, Candidates.SIGRID_17,
                             Candidates.THOMAS_17]})
result4 = Result(True, [Candidates.SIGRID_17])
episode4 = Episode(players4, result4,
                   {Candidates.JOCHEM_17: TestInput(jokers = 1), Candidates.IMANUELLE_17: TestInput({4: 2}),
                    Candidates.DIEDERIK_17: TestInput(jokers = 1), Candidates.THOMAS_17: TestInput({1: 1}),
                    Candidates.SANNE_17: TestInput({18: 3}, 1), Candidates.SIGRID_17: TestInput({6: 3})},
                   {1: question4_1, 4: question4_4, 6: question4_6, 18: question4_18})

# Aflevering 5 (afvaller: Jeroen)
# Vragen:
# 1 - De Mol is:
# 1: Diederik, Jeroen, Jochem, Thomas; 2: Imanuelle, Sanne;
# 2 - Hoe hield de Mol de handen tijdens de groepsfoto van aflevering 5? (Diederik Inaccuraat)
# 1: Jochem; 2: Sanne, Diederik; 3: Imanuelle, Thomas; 4: Jeroen;
# 3 - Wat was de kleur van de huifkar van de Mol bij de aanvang van de Oregon Trail?
# 1: Diederik, Jochem; 2: Imanuelle, Sanne; 3: Thomas, Jeroen;
# 11 - Welk nummer stond op de enveloppe die de Mol pakte bij de Pony Express?
# 1: Diederik; 2: Thomas; 3: Sanne; 4: Jochem; 5: Jeroen; 6: Imanuelle
# 17: Als hoeveelste ging de Mol het speelveld in bij de opdracht met de rodeo posters?
# 1: Sanne; 2: Thomas; 3: Imanuelle; 4: Jeroen; 5: Jochem; 6: Diederik
# 20 - Wie is de Mol?
# 1: Diederik; 2: Imanuelle; 3: Jeroen; 4: Jochem; 5: Sanne; 6: Thomas
# Antwoorden: Jeroen (3, 1), Jochem (2, 3), Thomas (11, 5) (1 joker), Sanne (1, 1), Imanuelle (20, 1), Diederik (17, 5)
players5 = [Candidates.DIEDERIK_17, Candidates.IMANUELLE_17, Candidates.JEROEN_17, Candidates.JOCHEM_17,
            Candidates.SANNE_17, Candidates.THOMAS_17]
question5_1 = Question({1: [Candidates.DIEDERIK_17, Candidates.JEROEN_17, Candidates.JOCHEM_17, Candidates.THOMAS_17],
                        2: [Candidates.IMANUELLE_17, Candidates.SANNE_17]})
question5_2 = Question({1: [Candidates.JOCHEM_17],
                        2: [Candidates.SANNE_17, Candidates.DIEDERIK_17],
                        3: [Candidates.IMANUELLE_17, Candidates.THOMAS_17],
                        4: [Candidates.JEROEN_17]})
question5_3 = Question({1: [Candidates.DIEDERIK_17, Candidates.JOCHEM_17],
                        2: [Candidates.IMANUELLE_17, Candidates.SANNE_17],
                        3: [Candidates.THOMAS_17, Candidates.JEROEN_17]})
question5_11 = Question({1: [Candidates.DIEDERIK_17], 2: [Candidates.THOMAS_17], 3: [Candidates.SANNE_17],
                         4: [Candidates.JOCHEM_17], 5: [Candidates.JEROEN_17], 6: [Candidates.IMANUELLE_17]})
question5_17 = Question({1: [Candidates.SANNE_17], 2: [Candidates.THOMAS_17], 3: [Candidates.IMANUELLE_17],
                         4: [Candidates.JEROEN_17], 5: [Candidates.JOCHEM_17], 6: [Candidates.DIEDERIK_17]})
question5_20 = Question({1: [Candidates.DIEDERIK_17], 2: [Candidates.IMANUELLE_17], 3: [Candidates.JEROEN_17],
                         4: [Candidates.JOCHEM_17], 5: [Candidates.SANNE_17], 6: [Candidates.THOMAS_17]})
result5 = Result(True, [Candidates.JEROEN_17])
episode5 = Episode(players5, result5,
                   {Candidates.JEROEN_17: TestInput({3: 1}), Candidates.JOCHEM_17: TestInput({2: 3}),
                    Candidates.THOMAS_17: TestInput({11: 5}, 1), Candidates.SANNE_17: TestInput({1: 1}),
                    Candidates.IMANUELLE_17: TestInput({20: 1}), Candidates.DIEDERIK_17: TestInput({17: 5})},
                   {1: question5_1, 2: question5_2, 3: question5_3, 11: question5_11, 17: question5_17,
                    20: question5_20})

# Aflevering 6 (geen afvaller, maar Jochem, Diederik & Imanuelle geen scherm gezien)
# Vragen:
# 1 - De Mol is:
# 1: Diederik, Jochem, Thomas; 2: Imanuelle, Sanne;
# 9 - Welke letters maakte de Mol tijdens de maai-opdracht? (Inaccuraat)
# 1: Thomas; 2: Jochem; 3: Imanuelle; 4: Sanne, Diederik;
# 14 - Hoeveel geld heeft de Mol verdiend tijdens de opdracht bij de rodeo?
# 1: Thomas; 2: Imanuelle; 3: Diederik, Jochem, Sanne;
# Antwoorden: Imanuelle (9, 4), Sanne (1, 1), Thomas (14, 3)
players6 = [Candidates.DIEDERIK_17, Candidates.IMANUELLE_17, Candidates.JOCHEM_17, Candidates.SANNE_17,
            Candidates.THOMAS_17]
question6_1 = Question({1: [Candidates.DIEDERIK_17, Candidates.JOCHEM_17, Candidates.THOMAS_17],
                        2: [Candidates.IMANUELLE_17, Candidates.SANNE_17]})
question6_9 = Question({1: [Candidates.THOMAS_17], 2: [Candidates.JOCHEM_17], 3: [Candidates.IMANUELLE_17],
                        4: [Candidates.SANNE_17, Candidates.DIEDERIK_17]})
question6_14 = Question({1: [Candidates.THOMAS_17], 2: [Candidates.IMANUELLE_17],
                         3: [Candidates.DIEDERIK_17, Candidates.JOCHEM_17, Candidates.SANNE_17]})
result6 = Result(False, [Candidates.IMANUELLE_17, Candidates.DIEDERIK_17, Candidates.JOCHEM_17])
episode6 = Episode(players6, result6,
                   {Candidates.IMANUELLE_17: TestInput({9: 4}), Candidates.SANNE_17: TestInput({1: 1}),
                    Candidates.THOMAS_17: TestInput({14: 3})},
                   {1: question6_1, 9: question6_9, 14: question6_14})

# Aflevering 7 (afvaller: Imanuelle)
# 5 - Tegen wie kon de Mol tijdens de etherdiscipline opdracht spreken?
# 1: Imanuelle; 2: Thomas; 3: Sanne; 4: Diederik; 5: Jochem
# 7 - Hoeveel vragen beantwoordde de Mol goed tijdens de etherdiscipline opdracht? (Niet Bruikbaar)
# 1: Diederik; 2: Sanne, Imanuelle; 3: Thomas 4: Jochem;
# 10 - In welk voertuig zat de Mol tijdens de opdracht in de luchtballon?
# 1: Diederik, Imanuelle; 2: Jochem, Sanne, Thomas;
# 17 - Welke tijd behaalde de Mol tijdens de proefronde van het schieten te paard?
# 1: Thomas; 2: Diederik; 3: Jochem; 4: Imanuelle; 5: Sanne;
# 20 - Wie is de Mol?
# 1: Diederik; 2: Imanuelle; 3: Jochem; 4: Sanne; 5: Thomas
# Antwoorden: Imanuelle (17, 2), Diederik (10, 2), Jochem (20, 1) (1 Joker), Sanne (5, 5)
players7 = [Candidates.DIEDERIK_17, Candidates.IMANUELLE_17, Candidates.JOCHEM_17, Candidates.SANNE_17,
            Candidates.THOMAS_17]
question7_5 = Question({1: [Candidates.IMANUELLE_17], 2: [Candidates.THOMAS_17], 3: [Candidates.SANNE_17],
                        4: [Candidates.DIEDERIK_17], 5: [Candidates.JOCHEM_17]})
question7_10 = Question({1: [Candidates.DIEDERIK_17, Candidates.IMANUELLE_17],
                         2: [Candidates.JOCHEM_17, Candidates.SANNE_17, Candidates.THOMAS_17]})
question7_17 = Question({1: [Candidates.THOMAS_17], 2: [Candidates.DIEDERIK_17], 3: [Candidates.JOCHEM_17],
                         4: [Candidates.IMANUELLE_17], 5: [Candidates.SANNE_17]})
question7_20 = Question({1: [Candidates.DIEDERIK_17], 2: [Candidates.IMANUELLE_17], 3: [Candidates.JOCHEM_17],
                         4: [Candidates.SANNE_17], 5: [Candidates.THOMAS_17]})
result7 = Result(True, [Candidates.IMANUELLE_17])
episode7 = Episode(players7, result7,
                   {Candidates.IMANUELLE_17: TestInput({17: 2}), Candidates.DIEDERIK_17: TestInput({10: 2}),
                    Candidates.JOCHEM_17: TestInput({20: 1}, 1), Candidates.SANNE_17: TestInput({5: 5})},
                   {5: question7_5, 10: question7_10, 17: question7_17, 20: question7_20})

# Aflevering 8 (afvaller: Diederik)
# 1 - De Mol is:
# 1: Diederik, Jochem, Thomas; 2: Sanne;
# 20 - Wie is de Mol?
# 1: Diederik; 2: Jochem; 3: Sanne; 4: Thomas
# Antwoorden: Thomas (20, 2), Sanne (20, 2), Diederik (1, 2) (20, 2), Jochem (Vrijstelling)
players8 = [Candidates.DIEDERIK_17, Candidates.JOCHEM_17, Candidates.SANNE_17, Candidates.THOMAS_17]
question8_1 = Question({1: [Candidates.DIEDERIK_17, Candidates.JOCHEM_17, Candidates.THOMAS_17],
                        2: [Candidates.SANNE_17]})
question8_20 = Question({1: [Candidates.DIEDERIK_17], 2: [Candidates.JOCHEM_17], 3: [Candidates.SANNE_17],
                         4: [Candidates.THOMAS_17]})
result8 = Result(True, [Candidates.DIEDERIK_17])
episode8 = Episode(players8, result8,
                   {Candidates.THOMAS_17: TestInput({20: 2}), Candidates.SANNE_17: TestInput({20: 2}),
                    Candidates.DIEDERIK_17: TestInput({1: 2, 20: 2})},
                   {1: question8_1, 20: question8_20})

season17 = (players1, {1: episode1, 2: episode2, 3: episode3, 4: episode4, 5: episode5, 6: episode6, 7: episode7,
                       8: episode8})