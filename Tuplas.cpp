//
// Created by joeli on 11/10/2026.
// Joelito Medina Martínez
// EJERCICIO 2 TUPLAS (pair): clasificacion de sensores con limites fijos :D

#include <iostream>
#include <vector>
#include <string>
#include <utility>   // aqui vive pair, que guarda dos datos juntos como Gojo y Geto, siempre en pareja :D
using namespace std;

// funcion que regresa DOS valores dentro de un pair (mayor y menor) xd
pair<double, double> mayorYMenor(vector< pair<string, double> > datos) {

    double mayor = datos[0].second;   // second es el segundo dato del pair, o sea el valor
    double menor = datos[0].second;

    for (int i = 0; i < datos.size(); i++) {
        if (datos[i].second > mayor) {
            mayor = datos[i].second;
        }
        if (datos[i].second < menor) {
            menor = datos[i].second;
        }
    }

    return make_pair(mayor, menor);   // make_pair arma el par para regresarlo :D
}

int main() {

    // const significa que no se puede modificar, como el Domain Expansion de Gojo una vez activado xd
    const int LIMITE_BAJO = 50;
    const int LIMITE_ALTO = 80;

    // vector donde cada elemento es un pair (nombre, valor) :D
    vector< pair<string, double> > sensores;

    int cantidad;
    cout << "Cuantos sensores vas a registrar: ";
    cin >> cantidad;

    // llenamos el vector con pares, como armar el equipo de los Vengadores uno por uno :D
    for (int i = 0; i < cantidad; i++) {
        string nombre;
        double valor;

        cout << "Nombre del sensor " << (i + 1) << ": ";
        cin >> nombre;
        cout << "Valor de " << nombre << ": ";
        cin >> valor;

        sensores.push_back(make_pair(nombre, valor));   // guardamos nombre y valor juntos
    }

    // recorremos mostrando el estado de cada sensor
    cout << "\n===== RESULTADOS =====" << endl;
    for (int i = 0; i < sensores.size(); i++) {

        string nombre = sensores[i].first;   // first es el primer dato del pair, el nombre
        double valor = sensores[i].second;   // second es el segundo dato, el valor
        string estado;

        if (valor < LIMITE_BAJO) {
            estado = "Estado normal";          // todo tranquilo, dia normal en Konoha :D
        } else if (valor <= LIMITE_ALTO) {
            estado = "Requiere supervision";   // hay que vigilarlo, como a Loki xd
        } else {
            estado = "Estado critico";         // Sukuna suelto, a correr :-v
        }

        cout << nombre << " -> " << valor << " : " << estado << endl;
    }

    // llamamos la funcion y recibimos el pair con los dos resultados :D
    pair<double, double> resultado = mayorYMenor(sensores);
    cout << "\nValor mas alto: " << resultado.first << endl;
    cout << "Valor mas bajo: " << resultado.second << endl;

    // si intentamos esto da error porque la constante no se puede cambiar, ni con el Sexto Sentido :-v
    // LIMITE_BAJO = 60;

    return 0;
}