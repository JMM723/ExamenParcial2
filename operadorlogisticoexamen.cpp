//
// Created by joeli on 11/10/2026.
//
//JESUS EMILIO NAVARRO CASTRO

#include <iostream>
#include <string>
#include <vector>
#include <iomanip>

using namespace std;

class OperadorLogistico {
    string nombre;
    string tipoTransporte;
    double costoPorKg;
    int tiempoEntregaDias;

public:
    OperadorLogistico(string _nombre, string _tipoTransporte, double _costoPorKg, int _tiempoEntregaDias)
        : nombre(_nombre), tipoTransporte(_tipoTransporte), costoPorKg(_costoPorKg), tiempoEntregaDias(_tiempoEntregaDias) {}

    string getNombre() const { return nombre; }
    string getTipoTransporte() const { return tipoTransporte; }
    double getCostoPorKg() const { return costoPorKg; }
    int getTiempoEntregaDias() const { return tiempoEntregaDias; }

    double calcularCostoEnvio(double pesoKg) const {
        return pesoKg * costoPorKg;
    }

    void mostrarInformacion() const {
        cout << left << setw(20) << nombre
             << setw(15) << tipoTransporte
             << "$" << setw(11) << fixed << setprecision(2) << costoPorKg
             << tiempoEntregaDias << " días" << endl;
    }
};

int main() {
    vector<OperadorLogistico> operadores = {
        OperadorLogistico("Express Cargo", "Aéreo", 12.50, 2),
        OperadorLogistico("Logística Global", "Marítimo", 3.20, 15),
        OperadorLogistico("Rutas del Norte", "Terrestre", 5.80, 5)
    };

    cout << "=== SISTEMA DE GESTIÓN DE OPERADORES LOGÍSTICOS ===" << endl << endl;

    cout << left << setw(20) << "Operador"
         << setw(15) << "Transporte"
         << setw(12) << "Costo/Kg"
         << "Tiempo Estimado" << endl;
    cout << string(60, '-') << endl;

    for (const auto& op : operadores) {
        op.mostrarInformacion();
    }

    double pesoPaquete;
    cout << "\n---------------------------------------------------" << endl;
    cout << "Ingrese el peso del paquete a enviar (en kg): ";
    cin >> pesoPaquete;

    if (pesoPaquete <= 0) {
        cout << "El peso ingresado no es válido." << endl;
        return 1;
    }

    cout << "\n--- COTIZACIÓN PARA UN PAQUETE DE " << pesoPaquete << " KG ---" << endl;
    for (const auto& op : operadores) {
        double costoTotal = op.calcularCostoEnvio(pesoPaquete);
        cout << "- " << op.getNombre() << " (" << op.getTipoTransporte() << "): $"
             << fixed << setprecision(2) << costoTotal
             << " (Llega en " << op.getTiempoEntregaDias() << " días)" << endl;
    }

    return 0;
}