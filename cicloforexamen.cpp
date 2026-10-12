//
// Created by joeli on 11/10/2026.
//
#include <iostream>
#include <string>

//Miguel Ángel Hernández Mandujano
//Inge, sé que deberían tener comentarios. Pero me lo enviaron el último día y no tengo ánimos de ponerle los comentarios que debíeron de haber puesto :-(

using namespace std;

int main() {
        string categorias[4] = {"Lácteos", "Panadería", "Lácteos", "Enlatados"};
        for (int i = 0; i < 4; i++) {
            cout << categorias[i] << " ";
        }

        for (int i = 0; i < 10; i++) {
            if (i == 5) break;
            cout << i << endl;
        }

        for (int i = 0; i < 6; i++) {
            if (i == 3) continue;
            cout << i << endl;
        }

        string productos[10] = {"Pan", "Leche", "Huevos"};
        double precios[3] = {2.5, 1.8, 3.0};
        int len = 3;

        cout << productos[0] << endl;
        cout << productos[len - 1] << endl;

        productos[len++] = "Cereal";

        for (int i = 0; i < len; i++) {
            if (productos[i] == "Leche") {
                for (int j = i; j < len - 1; j++) {
                    productos[j] = productos[j + 1];
                }
                len--;
                break;
            }
        }
        for (int i = 0; i < len; i++) {
            cout << productos[i] << endl;
        }

    return 0;
    // Conjunto.cpp
    string frutas[4] = {"manzanas", "naranja", "naranja", "pera"};
    for (int i = 0; i < 4; i++) {
        cout << frutas[i] << " ";
    }


    // For.cpp
    for (int i = 0; i < 10; i++) {
        if (i == 5) break;
        cout << i << endl;
    }

    for (int i = 0; i < 6; i++) {
        if (i == 3) continue;
        cout << i << endl;
    }

    // colecciones.cpp
    string alumnos[] = {"Ana", "Luis", "Paty"};
    double calif[3] = {9.0, 7.5, 8.2};

    cout << alumnos[0] << endl;
    cout << alumnos[len - 1] << endl;

    alumnos[len++] = "Carlos";

    for (int i = 0; i < len; i++) {
        if (alumnos[i] == "Luis") {
            for (int j = i; j < len - 1; j++) {
                alumnos[j] = alumnos[j + 1];
            }
            len--;
            break;
        }
    }

    for (int i = 0; i < len; i++) {
        cout << alumnos[i] << endl;
    }

    return 0;
}