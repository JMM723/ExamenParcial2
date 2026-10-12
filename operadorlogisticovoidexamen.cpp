//
// Created by joeli on 11/10/2026.
//
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
    OperadorLogistico()
        : nombre("Sin Nombre"), tipoTransporte("N/A"), costoPorKg(0.0), tiempoEntregaDias(0) {}

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

    friend ostream& operator<<(ostream& os, const OperadorLogistico& op) {
        os << "Nombre: " << op.nombre << "\n"
           << "Transporte: " << op.tipoTransporte << "\n"
           << "Costo/Kg: $" << fixed << setprecision(2) << op.costoPorKg << "\n"
           << "Tiempo estimado: " << op.tiempoEntregaDias << " dias\n"
           << "-----------------------------------";
        return os;
    }

    void mostrarInformacion() const {
        cout << *this << endl;
    }
};

int main() {
    OperadorLogistico op1("Express Cargo", "Aereo", 12.50, 2);
    OperadorLogistico op2("Rutas del Norte", "Terrestre", 5.80, 5);

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
    cout << opCombinado << endl;

    return 0;
}
