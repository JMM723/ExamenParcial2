//ELLIOTH EMMANUEL HERNANDEZ RAMIREZ

#include <iostream>
#include <iomanip>
using namespace std;

// Definimos una estructura (struct) para agrupar los datos del estudiante
// (Funciona de manera similar a un diccionario {clave: valor})
struct Estudiante {
    string nombre;
    double notas[3];
    double promedio;
};

int main() {
    // Configurar consola para aceptar acentos (en Windows)
    // system("chcp 65001 > nul");

    // 1. Entrada de datos
    cout << "--- Registro de Calificaciones ---" << endl;

    Estudiante alumno; // Creamos una variable de tipo Estudiante

    cout << "Introduce el nombre del alumno/a: ";
    getline(cin, alumno.nombre);

    cout << "Introduce la primera calificación: ";
    cin >> alumno.notas[0];

    cout << "Introduce la segunda calificación: ";
    cin >> alumno.notas[1];

    cout << "Introduce la tercera calificación: ";
    cin >> alumno.notas[2];

    //  2. y 3. Conversión y cálculo del promedio
    // Como las notas ya son numéricas (double), podemos sumarlas directamente
    alumno.promedio = (alumno.notas[0] + alumno.notas[1] + alumno.notas[2]) / 3.0;

    // --- 4. y 5. Mostrar resultados y boletín ---
    cout << "\n" << string(35, '=') << endl;
    cout << "       BOLETÍN DE CALIFICACIONES" << endl;
    cout << string(35, '=') << endl;

    cout << "Estudiante: " << alumno.nombre << endl;
    cout << string(35, '-') << endl;

    // Imprimimos las calificaciones guardadas en el arreglo
    cout << "Calificaciones: [" << alumno.notas[0] << ", "
                                << alumno.notas[1] << ", "
                                << alumno.notas[2] << "]" << endl;

    // Mostramos el promedio con solo 2 decimales usando fixed y setprecision
    cout << "Promedio Final: " << fixed << setprecision(2) << alumno.promedio << endl;

    // 6. Indicador de aprobación/reprobación
    // Evaluamos el promedio con una condición (if/else)
    // Si el promedio es mayor o igual a 6.0, el alumno aprueba.
    cout << string(35, '-') << endl;
    if (alumno.promedio >= 6.0) {
        cout << "ESTADO FINAL: APROBADO" << endl;
    } else {
        cout << "ESTADO FINAL: REPROBADO" << endl;
    }
    cout << string(35, '=') << "\n" << endl;

    return 0;
}