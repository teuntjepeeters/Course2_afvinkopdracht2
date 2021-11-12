import random


def main():
    ### OPDRACHT 1 ###
    # Gebruik de lijsten x y en z voor de grafieken van opdracht 1
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [3, 6, 8, 10, 12, 12, 4, 14, 7, 10]
    z = []
    for i in range(0,11):
        n = random.randint(1,100)
        z.append(n)

    ### OPDRACHT 2 ###
    # Bestand voor opdracht 2
    patienten = "patienten.csv"

    ### OPDRACHT 3 ###
    # Bestand voor opdracht 3
    gist = "yeast_genes.csv"

    ### OPDRACHT 4 ###
    # Bestand voor opdracht 4
    test = "test.csv"


main()
