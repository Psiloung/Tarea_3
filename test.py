from busqueda import laberinto

if __name__=="__main__":
    inicio=[0,0]
    final=[9,10]
    lab=laberinto(inicio,final)
    #Parte 1
    #lab.algoritmo_anchura()
    #lab.algoritmo_profundidad()
    #lab.algoritmo_anchura_evalua_hijos()
    #lab.algoritmo_profundidad_evalua_hijos()

    #Parte 2
    lab.algoritmo_better_first()
    #lab.algoritmo_hill_climbing()
    #lab.algoritmo_beam(2,None)