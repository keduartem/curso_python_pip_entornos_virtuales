import  matplotlib.pyplot as plt #importo la librería

def generate_pie_chart(): #Defino una función
    labels = ["A", "B", "C"]
    values = [200, 34, 120]

    fig, ax = plt.subplots () #Generar la grafica desde matlib
    ax.pie(values, labels=labels)
    plt.savefig("pie.png") # guardar archivo
    plt.close()