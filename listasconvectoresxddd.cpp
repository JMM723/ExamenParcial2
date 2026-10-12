//
// Created by joeli on 11/10/2026.
// Joelito Medina Martínez
// EJERCICIO 1 LISTAS : registro de temperaturas de un motor :D

#include <iostream>    // para cin y cout
#include <vector>      // para usar vector, la lista de C++ xd
#include <algorithm>   // para sort, que ordena la lista
using namespace std;

int main() {

    // vector vacio, crece solo como los clones del Kage Bunshin de Naruto :D
    vector<double> temperaturas;

    // pedimos cuantas lecturas y repetimos hasta que sea mayor a 0
    int cantidad = 0;
    while (cantidad < 1) {
        cout << "Cuantas lecturas quieres registrar: ";
        cin >> cantidad;
        if (cantidad < 1) {
            cout << "Tiene que ser al menos 1 xd" << endl;
        }
    }

    // ciclo for para llenar el vector, como juntar las Esferas del Dragon una por una :D
    for (int i = 0; i < cantidad; i++) {
        double temp;
        cout << "Temperatura " << (i + 1) << " (C): ";
        cin >> temp;
        temperaturas.push_back(temp);   // push_back agrega al final, como cuando llega Spider-Man a ultima hora xd
    }

    // mostramos todas las lecturas
    cout << "\nLecturas: ";
    for (int i = 0; i < temperaturas.size(); i++) {   // size nos dice cuantos elementos hay
        cout << temperaturas[i] << " ";
    }
    cout << endl;

    // calculamos suma, maximo y minimo con un solo ciclo :D
    double suma = 0;
    double maxima = temperaturas[0];   // suponemos que la primera es la mayor
    double minima = temperaturas[0];   // y tambien la menor

    for (int i = 0; i < temperaturas.size(); i++) {
        suma = suma + temperaturas[i];

        if (temperaturas[i] > maxima) {
            maxima = temperaturas[i];   // encontramos una con mas poder que la anterior xd
        }
        if (temperaturas[i] < minima) {
            minima = temperaturas[i];   // encontramos una mas baja
        }
    }

    double promedio = suma / temperaturas.size();

    cout << "Promedio: " << promedio << endl;
    cout << "Maxima: " << maxima << endl;
    cout << "Minima: " << minima << endl;

    // contamos cuantas lecturas pasan el limite de seguridad, como detectar maldiciones de grado especial en JJK :-v
    double limite = 80;
    int peligrosas = 0;   // contador que empieza en 0
    for (int i = 0; i < temperaturas.size(); i++) {
        if (temperaturas[i] > limite) {
            peligrosas = peligrosas + 1;   // sumamos 1 cada vez que una lectura se pasa
        }
    }
    cout << "Lecturas arriba de " << limite << " grados: " << peligrosas << endl;

    // sort ordena de menor a mayor, como el ranking de los Hashira de Demon Slayer :D
    // begin y end son el inicio y el final del vector
    sort(temperaturas.begin(), temperaturas.end());

    // back nos da el ultimo, que despues de ordenar es el mas alto
    double mayor = temperaturas.back();
    temperaturas.pop_back();   // pop_back quita el ultimo, un chasquido de Thanos pero solo a uno :-v
    cout << "Quitamos la lectura mas alta: " << mayor << endl;

    cout << "Lista final: ";
    for (int i = 0; i < temperaturas.size(); i++) {
        cout << temperaturas[i] << " ";
    }
    cout << endl;

    return 0;   // fin del programa, mision cumplida :D
}