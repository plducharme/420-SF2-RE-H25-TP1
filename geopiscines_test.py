import unittest
from geopiscines import *

class GeoPiscinesTest(unittest.TestCase):

    def setUp(self):
        self.piscine_rectangulaire = PiscineRectangulaire("PiscineRectangulaire", "RECT", 2, 5, 6)
        self.piscine_cylindrique = PiscineCylindrique("PiscineCylindrique", "CYL", 2, 5)
        self.piscine_hexagonale = PiscineHexagonale("PiscineHexagonale", "HEX", 2, 5)

    def test_piscine_validation_profondeur(self):
        with self.assertRaises(ValueError):
            PiscineRectangulaire("PiscineRectangulaire", "RECT", -1, 5, 6)
            PiscineCylindrique("PiscineCylindrique", "CYL", -1, 5)

        with self.assertRaises(ValueError):
            self.piscine_rectangulaire.profondeur = -1

    def test_piscine_recangulaire_validation_longueur(self):
        with self.assertRaises(ValueError):
            PiscineRectangulaire("PiscineRectangulaire", "RECT", 1, -5, 6)

        with self.assertRaises(ValueError):
            self.piscine_rectangulaire.longueur = -1

    def test_piscine_recangulaire_validation_largeur(self):
        with self.assertRaises(ValueError):
            PiscineRectangulaire("PiscineRectangulaire", "RECT", 1, 5, -6)

        with self.assertRaises(ValueError):
            self.piscine_rectangulaire.largeur = -1


    def test_piscine_recangulaire_volume(self):
        self.assertEqual(self.piscine_rectangulaire.volume(), 60)


    def test_piscine_recangulaire_dessiner(self):
        self.piscine_rectangulaire.dessiner()


    def test_piscine_cylindrique_validation_rayon(self):
        with self.assertRaises(ValueError):
            PiscineCylindrique("PiscineCylindrique", "CYL", 2, -1)

        with self.assertRaises(ValueError):
            self.piscine_cylindrique.rayon = -1

    def test_piscine_cylindrique_volume(self):
        self.assertAlmostEqual(self.piscine_cylindrique.volume(), 157.0796, places=4)

    def test_piscine_cylindrique_dessiner(self):
        self.piscine_cylindrique.dessiner()


    def test_piscine_hexagonale_validation_rayon(self):
        with self.assertRaises(ValueError):
            PiscineHexagonale("PiscineHexagonale", "HEX", 2, -1)

        with self.assertRaises(ValueError):
            self.piscine_hexagonale.rayon = -1


    def test_piscine_hexagonale_validation_longueur_cote(self):
        with self.assertRaises(ValueError):
            PiscineHexagonale("PiscineHexagonale", "HEX", 2, 5)

        with self.assertRaises(ValueError):
            self.piscine_hexagonale.longueur_cote = -1

    def test_piscine_hexagonale_volume(self):
        self.assertAlmostEqual(self.piscine_hexagonale.volume(), 129.9038, places=4)

    def test_piscine_hexagonale_dessiner(self):
        self.piscine_hexagonale.dessiner()

