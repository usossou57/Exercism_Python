"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(TIME_COMPLETED):
    """Calcul du temps de cuisson restant
        Cette fonction prend en paramètre le temps de cuisson écoulé et retourne le temps de cuisson restant en faisant: temps de cuisson total - temps de cuisson écoulé
    """
    return (EXPECTED_BAKE_TIME - TIME_COMPLETED)
    


#TODO: Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.
def preparation_time_in_minutes(number_of_layers):
    """ Calcul de la durée de préparation:
        Etant donnée que chaque couche nécessite 2 minutes de préparation, la durée de préparation est obtenue en faisant 2 * nombre de couches
    """
    return number_of_layers*2


#TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):
    """Calcul du temps total à faire en cuisine:
    Il correspond au temps de cuisson écoulé + durée de préparation de chaque couche
    """
    return elapsed_bake_time+(number_of_layers*2)


# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
