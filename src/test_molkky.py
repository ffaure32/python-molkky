from src.molkky import MolkkyScore, SCORE_RETOUR


def test_score_initial_a_zero():
    score_molkky = MolkkyScore()

    score = score_molkky.score()

    assert score == 0

def test_score_premier_lancer():
    # Arrange
    score_molkky = MolkkyScore()

    # Act
    score_molkky.lancer(9)

    # Assert
    score = score_molkky.score()
    assert score == 9

def test_score_premier_lancer_autre_resultat():
    # Arrange
    score_molkky = MolkkyScore()

    # Act
    score_molkky.lancer(4)

    # Assert
    score = score_molkky.score()
    assert score == 4

def test_score_2_lancer_somme_resultats():
    # Arrange
    score_molkky = MolkkyScore()

    # Act
    score_molkky.plusieurs_lancers_consecutifs(4, 3)

                                   # Assert
    score = score_molkky.score()
    assert score == 7

def test_score_1_lancer_plusieurs_quilles():
    # Arrange
    score_molkky = MolkkyScore()

    # Act
    score_molkky.lancer(4, 12)

    # Assert
    score = score_molkky.score()
    assert score == 2

def test_score_1_lancer_zero_quille():
    # Arrange
    score_molkky = MolkkyScore()

    # Act
    score_molkky.lancer()

    # Assert
    score = score_molkky.score()
    assert score == 0


def test_partie_gagnante():
    # Arrange
    score_molkky = MolkkyScore()

    # Act
    score_molkky.plusieurs_lancers_consecutifs(12, 12, 12, 12, 2)

                                   # Assert
    partie_gagnee = score_molkky.partie_gagnee()
    assert partie_gagnee


def test_partie_non_gagnante():
    # Arrange
    score_molkky = MolkkyScore()

    # Act
    score_molkky.plusieurs_lancers_consecutifs(12, 12, 12, 12)

   # Assert
    partie_gagnee = score_molkky.partie_gagnee()
    assert partie_gagnee == False


def test_score_a_25_car_depassement_limite():
    # Arrange
    score_molkky = MolkkyScore()

    # Act
    score_molkky.plusieurs_lancers_consecutifs(12, 12, 12, 12, 12)

    # Assert
    score = score_molkky.score()
    assert score == SCORE_RETOUR


def test_trois_fois_0_partie_perdue():
    # Arrange
    score_molkky = MolkkyScore()

    # Act
    score_molkky.lancer()
    score_molkky.lancer()
    score_molkky.lancer()

    # Assert
    partie_perdue = score_molkky.partie_perdue()
    assert partie_perdue

def test_deux_fois_0_partie_pas_perdue():
    # Arrange
    score_molkky = MolkkyScore()

    # Act
    score_molkky.lancer()
    score_molkky.lancer()

    # Assert
    partie_perdue = score_molkky.partie_perdue()
    assert partie_perdue == False

def test_lancers_rates_non_consecutifs_ne_terminent_pas_la_partie():
    # Arrange
    score_molkky = MolkkyScore()

    # Act
    score_molkky.lancer()
    score_molkky.lancer(3)
    score_molkky.lancer()
    score_molkky.lancer()

    # Assert
    partie_perdue = score_molkky.partie_perdue()
    assert partie_perdue == False

def test_lancer_apres_partie_perdue():
    # Arrange
    score_molkky = MolkkyScore()

    # Act
    score_molkky.lancer()
    score_molkky.lancer()
    score_molkky.lancer()

    try:
        score_molkky.lancer(3)
        assert False
    except Exception as e:
        assert str(e) == "Partie Terminee"

def test_lancer_apres_partie_gagnee():
    # Arrange
    score_molkky = MolkkyScore()

    # Act
    score_molkky.plusieurs_lancers_consecutifs(12, 12, 12, 12, 2)

    try:
        score_molkky.lancer(3)
        assert False
    except Exception as e:
        assert str(e) == "Partie Terminee"
