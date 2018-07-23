NB_LANCERS_RATES_TERMINANT_PARTIE = 3
SCORE_RETOUR = 25
SCORE_PARTIE_GAGNEE = 50


class MolkkyScore(object):
    def __init__(self):
        self.partie_terminee = False
        self.nb_lancers_rates = 0
        self.score_total = 0

    def score(self):
        return self.score_total

    def lancer(self, *quilles):
        self._verifier_partie_en_cours()
        self._calcul_score_brut(quilles)
        if self._score_max_depasse():
            self.score_total = SCORE_RETOUR
        self._maj_etat_partie(quilles)

    def _maj_etat_partie(self, quilles):
        self._maj_partie_perdue(quilles)
        self._maj_partie_gagnee()

    def _maj_partie_perdue(self, quilles):
        self._maj_decompte_lancers_rates(quilles)

        if self.nb_lancers_rates == NB_LANCERS_RATES_TERMINANT_PARTIE:
            self.partie_terminee = True

    def _maj_decompte_lancers_rates(self, quilles):
        lancer_rate = len(quilles) == 0
        if lancer_rate:
            self.nb_lancers_rates += 1
        else:
            self.nb_lancers_rates = 0

    def _score_max_depasse(self):
        return self.score_total > SCORE_PARTIE_GAGNEE

    def _calcul_score_brut(self, quilles):
        nombre_de_quilles = len(quilles)
        if nombre_de_quilles == 1:
            self.score_total += quilles[0]
        else:
            self.score_total += nombre_de_quilles

    def partie_gagnee(self):
        return self._verifier_partie_gagnee()

    def _verifier_partie_gagnee(self):
        return self.score_total == SCORE_PARTIE_GAGNEE

    def plusieurs_lancers_consecutifs(self, *lancers):
        for lancer in lancers:
            self.lancer(lancer)

    def partie_perdue(self):
        return self.partie_terminee

    def _verifier_partie_en_cours(self):
        if self.partie_terminee:
            raise Exception("Partie Terminee")

    def _maj_partie_gagnee(self):
        if self._verifier_partie_gagnee():
            self.partie_terminee = True
