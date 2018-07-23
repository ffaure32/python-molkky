SCORE_IF_MAX_EXCEEDED = 25
SCORE_MAX = 50


class Molky:
    def __init__(self, joueurs):
        self.joueurs = [Joueur(j) for j in joueurs]
        self.index = 0

    def nom_prochain_joueur(self):
        return self.joueur_actuel().nom

    def score(self):
        test = [j.score_joueur() for j in self.joueurs]
        return ' ; '.join(test)

    def lance(self, quilles):
        self.verifier_etat_partie()
        self.joueur_actuel().update_score(Lancer(quilles))
        self.update_index()

    def verifier_etat_partie(self):
        if self.has_vainqueur():
            raise LancerImpossible('la partie est terminee')

    def joueur_actuel(self):
        return self.joueurs[self.index]

    def update_index(self):
        self.index += 1
        if self.index == len(self.joueurs):
            self.index = 0

    def has_vainqueur(self):
        return len(self.filtre_vainqueur()) == 1

    def vainqueur(self):
        vainqueur = self.filtre_vainqueur()
        if len(vainqueur) == 1:
            return vainqueur[0].nom

    def filtre_vainqueur(self):
        return [j for j in self.joueurs if j.is_winner()]


class Lancer:
    def __init__(self, quilles):
        self.quilles = quilles
        self.verifier_valeurs_quilles()
        self.verifier_doublons_quilles()

    def verifier_valeurs_quilles(self):
        if any([q for q in self.quilles if q <= 0 or q > 12]):
            raise LancerInvalide('quilles invalides')

    def verifier_doublons_quilles(self):
        if len(set(self.quilles)) < len(self.quilles):
            raise LancerInvalide('quilles en doublon')

    def score(self):
        if len(self.quilles) == 1:
            return self.quilles[0]
        else:
            return len(self.quilles)


class LancerInvalide(Exception):
    pass

class LancerImpossible(Exception):
    pass


class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.score = 0

    def score_joueur(self):
        return self.nom + ' : ' + str(self.score)

    def update_score(self, lancer):
        self.score += lancer.score()
        if self.score > SCORE_MAX:
            self.score = SCORE_IF_MAX_EXCEEDED

    def is_winner(self):
        return self.score == SCORE_MAX