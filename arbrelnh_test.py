import unittest
import csv

from arbrelnh import Noeud, DataUtils, EquipeLNH


class ArbreLnhTest(unittest.TestCase):

    def setUp(self):
        self.racine = None
        self.equipes_pts = {}
        self.liste_equipes: list[EquipeLNH] = self.load_data_test()

        for equipe in self.liste_equipes:
            if self.racine is None:
                self.racine = Noeud(equipe)
            else:
                self.racine.insertion(equipe)

    def test_total_points(self):
        for equipe in self.liste_equipes:
            self.assertEqual(equipe.total_points(), int(self.equipes_pts[equipe.nom][0]))

    def test_moyenne_but_par_match(self):
        for equipe in self.liste_equipes:
            self.assertAlmostEqual(equipe.moyenne_but_par_match(), self.equipes_pts[equipe.nom][1], places=4)

    def test_moyenne_de_moyennes_buts_par_match(self):
        moyenne = DataUtils.moyenne_de_moyennes_buts_par_match(self.liste_equipes)
        total_moyenne = 0
        for equipe in self.equipes_pts.values():
            total_moyenne += equipe[1]

        moyenne_attendue = total_moyenne / len(self.liste_equipes)
        self.assertAlmostEqual(moyenne, moyenne_attendue, places=4)

    def test_moyenne_bas_haut(self):
        bas, haut = DataUtils.moyenne_haut_bas(self.liste_equipes)
        total_moyenne = 0
        for equipe in self.equipes_pts.values():
            total_moyenne += equipe[1]

        moyenne = total_moyenne / len(self.liste_equipes)

        for equipe in self.liste_equipes:
            if equipe.moyenne_but_par_match() < moyenne:
                self.assertIn(equipe, bas)
            else:
                self.assertIn(equipe, haut)

    def test_arbre_binaire(self):
        liste_triee = []
        ArbreLnhTest.tri_arbre(self.racine, liste_triee)
        equipes_pts_triees = sorted(self.equipes_pts.items(), key=lambda x: x[1][0])
        for i in range(len(self.liste_equipes)):
            self.assertEqual(liste_triee[i].nom, equipes_pts_triees[i][0])

    def test_validation_parties_jouees(self):
        for equipe in self.liste_equipes:
            with self.assertRaises(ValueError):
                equipe.parties_jouees = -1

    def test_validation_victoires(self):
        for equipe in self.liste_equipes:
            with self.assertRaises(ValueError):
                equipe.victoires = -1

    def test_validation_defaites(self):
        for equipe in self.liste_equipes:
            with self.assertRaises(ValueError):
                equipe.defaites = -1

    def test_validation_defaites_prolongation(self):
        for equipe in self.liste_equipes:
            with self.assertRaises(ValueError):
                equipe.defaites_prolongation = -1

    def test_validation_buts_pour(self):
        for equipe in self.liste_equipes:
            with self.assertRaises(ValueError):
                equipe.buts_pour = -1

    def test_validation_buts_contre(self):
        for equipe in self.liste_equipes:
            with self.assertRaises(ValueError):
                equipe.buts_contre = -1

    @staticmethod
    def tri_arbre(racine, liste):
        if racine.gauche:
            ArbreLnhTest.tri_arbre(racine.gauche, liste)
        liste.append(racine.equipe)
        if racine.droite:
            ArbreLnhTest.tri_arbre(racine.droite, liste)


    def load_data_test(self):
        liste_equipes = []
        with open("lnh2025.csv", 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f, delimiter=";")

            for ligne in reader:
                equipe = EquipeLNH(ligne["Equipe"], int(ligne["PJ"]), int(ligne["V"]), int(ligne["D"]), int(ligne["DP"]), int(ligne["BP"]), int(ligne["BC"]))
                liste_equipes.append(equipe)
                self.equipes_pts[ligne["Equipe"]] = (int(ligne["PTS"]), float(int(ligne["BP"]) / int(ligne["PJ"])))

            return liste_equipes


