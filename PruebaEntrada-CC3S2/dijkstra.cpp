#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

struct arista {
    int datoDestino;
    int peso;
    arista *sgteArista;
};

typedef arista* parista;

struct vertice {
    int datoOrigen;
    vertice *sgteVertice;
    parista adyacente;
};

typedef vertice* pvertice;

class grafo {
private:
    pvertice pGrafo;

public:
    grafo();
    ~grafo();
    void insertarVertice(int);
    void insertarArista(int, int, int);
    void imprimirGrafo();

};

grafo::grafo() {
    pGrafo = NULL;
}

grafo::~grafo() {
    pvertice p = pGrafo, rp;
    while (p != NULL) {
        parista r = p->adyacente, ra;
        while (r != NULL) {
            ra = r;
            r = r->sgteArista;
            delete ra;
        }
        rp = p;
        p = p->sgteVertice;
        delete rp;
    }
}

void grafo::insertarVertice(int x) {
    pvertice nuevo = new vertice;
    nuevo->datoOrigen = x;
    nuevo->adyacente = NULL;
    nuevo->sgteVertice = pGrafo;
    pGrafo = nuevo;
}

void grafo::insertarArista(int origen, int destino, int peso) {
    pvertice p = pGrafo;
    while (p != NULL && p->datoOrigen != origen) {
        p = p->sgteVertice;
    }
    if (p != NULL) {
        parista nueva = new arista;
        nueva->datoDestino = destino;
        nueva->peso = peso;
        nueva->sgteArista = p->adyacente;
        p->adyacente = nueva;
    }
}


void grafo::imprimirGrafo() {
    pvertice p = pGrafo;
    if (p == NULL) cout << "Grafo vacio" << endl;
    else {
        while (p != NULL) {
            parista a = p->adyacente;
            cout << p->datoOrigen;
            if(a != NULL) {
                cout << "->";
            }
            while (a != NULL) {
                cout << a->datoDestino << "(Peso: " << a->peso << ") ";
                a = a->sgteArista;
                if(a != NULL) {
                    cout << "->";
                }
            }
            cout << endl;
            p = p->sgteVertice;
        }
    }
}






int main() {
    grafo g;
    
    // Insertar vértices
    for (int i = 0; i <= 5; ++i) {
        g.insertarVertice(i);
    }

    // Insertar aristas con sus pesos
    g.insertarArista(0, 1, 41);
    g.insertarArista(1, 2, 51);
    g.insertarArista(2, 3, 50);
    g.insertarArista(4, 3, 36);
    g.insertarArista(3, 5, 38);
    g.insertarArista(3, 0, 45);
    g.insertarArista(0, 5, 29);
    g.insertarArista(5, 4, 21);
    g.insertarArista(1, 4, 32);
    g.insertarArista(4, 2, 32);
    g.insertarArista(5, 1, 24);

    // Imprimir el grafo
    g.imprimirGrafo();


    return 0;
}
