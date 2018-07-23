from src.mollky import Molky, LancerInvalide, LancerImpossible


def test_init_partie():
    mollky = Molky(['Alice', 'Bob'])

    prochain_joueur = mollky.nom_joueur_actuel()

    assert prochain_joueur == 'Alice'


def test_premier_lancer_avec_une_quille():
    # arrange
    mollky = Molky(['Alice', 'Bob'])

    # act
    mollky.lance([5])

    # assert
    assert mollky.score() == "Alice : 5 ; Bob : 0"
    assert mollky.nom_joueur_actuel() == 'Bob'


def test_deuxieme_joueur_avec_une_quille():
    # arrange
    mollky = Molky(['Alice', 'Bob'])

    # act
    lancers_unitaires(mollky, [5, 5])

    # assert
    assert mollky.score() == "Alice : 5 ; Bob : 5"
    assert mollky.nom_joueur_actuel() == 'Alice'


def test_lanceravec_deux_quilles():
    # arrange
    mollky = Molky(['Alice', 'Bob'])

    # act
    mollky.lance([5, 7])

    # assert
    assert mollky.score() == "Alice : 2 ; Bob : 0"


def test_rate_quilles():
    # arrange
    mollky = Molky(['Alice', 'Bob'])

    # act
    mollky.lance([])

    # assert
    assert mollky.score() == "Alice : 0 ; Bob : 0"


def test_depasse_score_max():
    # arrange
    mollky = Molky(['Alice'])

    # act
    lancers_unitaires(mollky, [12, 12, 12, 12, 12])

    # assert
    assert mollky.score() == "Alice : 25"


def test_lancement_partie_terminee():
    # arrange
    mollky = Molky(['Alice'])

    # act
    lancers_unitaires(mollky, [12, 12, 12, 12, 2])

    try:
        mollky.lance([5])
        assert False
    except LancerImpossible:
        assert True


def test_lancement_quille_invalide():
    # arrange
    mollky = Molky(['Alice'])

    # act
    try:
        mollky.lance([13])
        assert False
    except LancerInvalide:
        assert True


def test_lancement_quille_negative():
    # arrange
    mollky = Molky(['Alice'])

    # act
    try:
        mollky.lance([-1])
        assert False
    except LancerInvalide:
        assert True


def test_lancement_memes_quilles():
    # arrange
    mollky = Molky(['Alice'])

    # act
    try:
        mollky.lance([5, 5])
        assert False
    except LancerInvalide:
        assert True


def test_recupere_vainqueur():
    # arrange
    mollky = Molky(['Alice', 'Bob'])

    # act
    lancers_unitaires(mollky, [12, 1, 12, 1, 12, 1, 12, 1, 2])

    # assert
    assert mollky.score() == "Alice : 50 ; Bob : 4"
    assert mollky.vainqueur() == "Alice"


def lancers_unitaires(mollky, lancers):
    for lancer in lancers:
        mollky.lance([lancer])
