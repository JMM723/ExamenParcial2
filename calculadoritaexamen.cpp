//
// Created by joeli on 11/10/2026.
//
//ELLIOTH EMMANUEL HERNANDEZ RAMIREZ
#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

struct Estudiante {
    string nombre;
    double notas[3];
    double promedio;
};

int main() {
    Estudiante alumno;

    cout << "Registro de Calificaciones" << endl;

    cout << "Introduce el nombre del alumno/a: ";
    getline(cin, alumno.nombre);

    cout << "Introduce la primera calificacion: ";
    cin >> alumno.notas[0];

    cout << "Introduce la segunda calificacion: ";
    cin >> alumno.notas[1];

    cout << "Introduce la tercera calificacion: ";
    cin >> alumno.notas[2];

    alumno.promedio = (alumno.notas[0] + alumno.notas[1] + alumno.notas[2]) / 3.0;

    cout << "\n" << string(35, '=') << endl;
    cout << "       BOLETIN DE CALIFICACIONES" << endl;
    cout << string(35, '=') << endl;

    cout << "Estudiante: " << alumno.nombre << endl;
    cout << string(35, '-') << endl;

    cout << "Calificaciones: [" << alumno.notas[0] << ", "
         << alumno.notas[1] << ", "
         << alumno.notas[2] << "]" << endl;

    cout << "Promedio Final: " << fixed << setprecision(2)
         << alumno.promedio << endl;

    cout << string(35, '-') << endl;

    if (alumno.promedio >= 6.0) {
        cout << "ESTADO FINAL: APROBADO" << endl;
    } else {
        cout << "ESTADO FINAL: REPROBADO" << endl;
    }

    cout << string(35, '=') << endl;

    return 0;
}