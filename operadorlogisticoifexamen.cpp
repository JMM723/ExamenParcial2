//
// Created by joeli on 11/10/2026.
//
//JESUS EMILIO NAVARRO CASTRO
#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

class OperadorLogistico {
private:
    string nombre;
    string tipoTransporte;
    double costoPorKg;
    int tiempoEntregaDias;

public:
    OperadorLogistico() : nombre("Sin Nombre"), tipoTransporte("N/A"), costoPorKg(0.0), tiempoEntregaDias(0) {}

    OperadorLogistico(string _nombre, string _tipoTransporte, double _costoPorKg, int _tiempoEntregaDias)
        : nombre(_nombre), tipoTransporte(_tipoTransporte), costoPorKg(_costoPorKg), tiempoEntregaDias(_tiempoEntregaDias) {}

    OperadorLogistico& operator=(const OperadorLogistico& otro) {
        if (this != &otro) {
            this->nombre = otro.nombre;
            this->tipoTransporte = otro.tipoTransporte;
            this->costoPorKg = otro.costoPorKg;
            this->tiempoEntregaDias = otro.tiempoEntregaDias;
        }
        return *this;
    }

    OperadorLogistico operator+(const OperadorLogistico& otro) const {
        string nuevoNombre = this->nombre + " & " + otro.nombre;
        string nuevoTipo = this->tipoTransporte + "/" + otro.tipoTransporte;
        double costoCombinado = (this->costoPorKg + otro.costoPorKg) / 2.0;
        int tiempoTotal = this->tiempoEntregaDias + otro.tiempoEntregaDias;
        return OperadorLogistico(nuevoNombre, nuevoTipo, costoCombinado, tiempoTotal);
    }

    bool operator==(const OperadorLogistico& otro) const {
        return (this->costoPorKg == otro.costoPorKg && this->tiempoEntregaDias == otro.tiempoEntregaDias);
    }

    bool operator<(const OperadorLogistico& otro) const {
        return this->costoPorKg < otro.costoPorKg;
    }

    void mostrarInformacion() const {
        cout << "Nombre: " << nombre << endl;
        cout << "Transporte: " << tipoTransporte << endl;
        cout << "Costo/Kg: $" << fixed << setprecision(2) << costoPorKg << endl;
        cout << "Tiempo estimado: " << tiempoEntregaDias << " dias" << endl;
        cout << "-----------------------------------" << endl;
    }
};

int main() {
    OperadorLogistico op1("Express Cargo", "Aereo", 12.50, 2);
    OperadorLogistico op2("Rutas del Norte", "Terrestre", 5.80, 5);
    OperadorLogistico op3("Express Cargo Duplicado", "Aereo", 12.50, 2);

    cout << "=== OPERADORES ORIGINALES ===" << endl;
    op1.mostrarInformacion();
    op2.mostrarInformacion();

    OperadorLogistico opCopia;
    opCopia = op1;

    cout << "=== PRUEBA OPERADOR DE ASIGNACIÓN (=) ===" << endl;
    cout << "Resultado de (opCopia = op1):" << endl;
    opCopia.mostrarInformacion();

    OperadorLogistico opCombinado = op1 + op2;

    cout << "=== PRUEBA OPERADOR ARITMÉTICO (+) ===" << endl;
    cout << "Resultado de (op1 + op2):" << endl;
    opCombinado.mostrarInformacion();

    cout << "=== PRUEBA OPERADORES RELACIONALES (== y <) ===" << endl;
    if (op1 == op3) {
        cout << "op1 y op3 tienen las mismas tarifas y tiempos." << endl;
    } else {
        cout << "op1 y op3 son diferentes en tarifas o tiempos." << endl;
    }

    if (op2 < op1) {
        cout << "op2 ('Rutas del Norte') es más económico por kg que op1 ('Express Cargo')." << endl;
    }

    return 0;
}