import csv
import random
import typing

##############################################
# Nom: Membre1 (github username)
# Nom: Membre2 (github username)
# Nom: Membre3 (github username)
##############################################

class EquipeLNH:
    pass



class DataUtils:

    # Charge le classement des équipes de la LNH à partir d'un fichier CSV
    # Retourne une liste de dictionnaires contenant les données pour chaque équipe
    @staticmethod
    def charger_données(nom_fichier: str) -> list[dict]:

        # Ouvre le fichier en
        with open(nom_fichier, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f, delimiter=';')
            equipes = [ligne for ligne in reader]
            # Permet de garder l'aléatoire constant
            random.seed(666)
            random.shuffle(equipes)
            return equipes

    # Calcul la moyenne des buts par match moyenne pour la liste d'équipes
    @staticmethod
    def moyenne_de_moyennes_buts_par_match(equipes: list[EquipeLNH]) -> float:
        pass

    # Sépare les équipes en deux listes, une pour les équipes ayant une moyenne de buts par match
    # inférieure à la moyenne et une autre pour les équipes ayant une moyenne de buts par match
    # supérieure ou égale à la moyenne
    @staticmethod
    def moyenne_haut_bas(equipes: list[EquipeLNH]) -> tuple[list[EquipeLNH], list[EquipeLNH]]:
        pass




if __name__ == '__main__':
    dict_equipes = DataUtils.charger_données('lnh2025.csv')
    print(dict_equipes)

