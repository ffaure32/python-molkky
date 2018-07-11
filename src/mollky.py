SCORE_IF_MAX_EXCEEDED = 25
SCORE_MAX = 50


class Molky:
    def __init__(self, joueurs):
        self.joueurs = list(map(lambda j: Joueur(j), joueurs))
        self.index = 0

    def nom_prochain_joueur(self):
        return self.joueur_actuel().nom

    def score(self):
        return ' ; '.join(list(map(lambda j: j.score_joueur(), self.joueurs)))

    def lance(self, quilles):
        self.verifier_etat_partie()
        self.joueur_actuel().update_score(Lancer(quilles))
        self.update_index()

    def verifier_etat_partie(self):
        if self.has_vainqueur():
            raise ValueError('la partie est terminee')

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
        return list(filter(lambda j: j.is_winner(), self.joueurs))


class Lancer:
    def __init__(self, quilles):
        self.quilles = quilles
        self.verifier_valeurs_quilles()
        self.verifier_doublons_quilles()

    def verifier_valeurs_quilles(self):
        if any(list(map(lambda q: q <= 0 or q > 12, self.quilles))):
            raise ValueError('quilles invalides')

    def verifier_doublons_quilles(self):
        if len(set(self.quilles)) < len(self.quilles):
            raise ValueError('quilles en doublon')

    def score(self):
        if len(self.quilles) == 1:
            return self.quilles[0]
        else:
            return len(self.quilles)


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
