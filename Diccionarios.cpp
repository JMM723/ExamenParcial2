//
// Created by joeli on 11/10/2026.
//Joel Medina Martínez
// EJERCICIO 3 DICCIONARIOS (map): inventario de componentes de un robot :D

#include <iostream>
#include <map>      // aqui vive map, el diccionario de C++ xd
#include <string>
using namespace std;

int main() {

    // clave = nombre del componente, valor = cantidad, como el intercambio equivalente de Fullmetal Alchemist :D
    map<string, int> inventario;
    inventario["motor"] = 4;
    inventario["sensor"] = 10;
    inventario["led"] = 25;

    int opcion = 0;

    // el menu se repite hasta que el usuario elija la opcion 5
    do {
        cout << "\n===== INVENTARIO =====" << endl;
        cout << "1. Ver inventario" << endl;
        cout << "2. Agregar componente" << endl;
        cout << "3. Eliminar componente" << endl;
        cout << "4. Total de piezas" << endl;
        cout << "5. Salir" << endl;
        cout << "Elige una opcion: ";
        cin >> opcion;

        if (opcion == 1) {
            // auto deja que el compilador deduzca el tipo, como Jarvis que ya sabe que quieres antes de pedirlo xd
            // cada elemento es un par con first (clave) y second (valor)
            for (auto par : inventario) {
                cout << par.first << " -> " << par.second << endl;
            }

        } else if (opcion == 2) {
            string nombre;
            int cantidad;
            cout << "Nombre del componente: ";
            cin >> nombre;
            cout << "Cantidad a agregar: ";
            cin >> cantidad;

            // count nos dice si la clave existe, regresa 1 si esta y 0 si no :D
            if (inventario.count(nombre) > 0) {
                inventario[nombre] = inventario[nombre] + cantidad;   // si existe, sumamos
            } else {
                inventario[nombre] = cantidad;                        // si no existe, lo creamos
            }
            cout << "Listo, inventario actualizado xd" << endl;

        } else if (opcion == 3) {
            string nombre;
            cout << "Componente a eliminar: ";
            cin >> nombre;

            if (inventario.count(nombre) > 0) {
                inventario.erase(nombre);   // erase lo borra como si su nombre estuviera en el Death Note de Light :-v
                cout << "Componente eliminado" << endl;
            } else {
                cout << "Ese componente no existe" << endl;   // ni Ryuk lo encuentra xd
            }

        } else if (opcion == 4) {
            int total = 0;
            // sumamos solo los valores, como contar las Gemas del Infinito :D
            for (auto par : inventario) {
                total = total + par.second;
            }
            cout << "Total de piezas: " << total << endl;

        } else if (opcion == 5) {
            cout << "Hasta luego, Avengers Assemble otra vez cuando quieras :D" << endl;

        } else {
            cout << "Opcion no valida, intenta de nuevo xd" << endl;
        }

    } while (opcion != 5);

    return 0;
}