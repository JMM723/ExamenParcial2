//
// Created by joeli on 11/10/2026.
//
// CONVERSION DE TIPOS (CASTING) EN C++: como transformar un dato en otro :D

#include <iostream>    // para cin y cout
#include <string>      // para string, stoi, stod y to_string xd
#include <vector>      // para el ejemplo real con vector
#include <cmath>       // para round
#include <stdexcept>   // para atrapar errores con try y catch
using namespace std;

int main() {

    // CONVERSION IMPLICITA
    // C++ la hace solo cuando mezclamos tipos compatibles, sin que se lo pidamos xd
    cout << "CONVERSION IMPLICITA" << endl;
    int entero = 10;
    double decimal = 2.5;

    double resultado = entero + decimal;   // int + double, C++ convierte el int a double solito
    cout << "10 + 2.5 = " << resultado << endl;

    // al reves tambien pasa, pero se pierden los decimales, como un chasquido de Thanos :-v
    double pi = 3.99;
    int cortado = pi;   // el double se mete en un int y se cortan los decimales sin avisar
    cout << "3.99 guardado en un int: " << cortado << endl;

    // el problema clasico de la division entre enteros
    cout << "\nDIVISION ENTERA" << endl;
    cout << "7 / 2 = " << 7 / 2 << endl;       // dos enteros dan un entero, sale 3 y no 3.5 :-v
    cout << "7 / 2.0 = " << 7 / 2.0 << endl;   // con un decimal ya sale 3.5 xd

    // CONVERSION EXPLICITA
    // aqui nosotros le decimos a C++ en que tipo queremos el dato
    // hay tres formas, la de estilo C, la funcional y la moderna static_cast :D
    cout << "\nCONVERSION EXPLICITA" << endl;
    double valor = 7.9;

    int a = (int)valor;              // estilo C, el mas corto pero el menos recomendado
    int b = int(valor);              // estilo funcional, parece una funcion
    int c = static_cast<int>(valor); // la forma moderna y la mas segura, usa esta :D

    cout << "Estilo C: " << a << endl;        // las tres cortan los decimales, no redondean
    cout << "Funcional: " << b << endl;
    cout << "static_cast: " << c << endl;

    // el casting arregla la division entera, como cuando Naruto activa el modo sabio :D
    int suma = 7;
    int cantidad = 2;
    double promedio1 = suma / cantidad;                         // sale 3, mal :-v
    double promedio2 = static_cast<double>(suma) / cantidad;    // sale 3.5, bien xd
    cout << "Sin casting: " << promedio1 << endl;
    cout << "Con casting: " << promedio2 << endl;

    // si quieres redondear de verdad usa round, static_cast solo corta
    cout << "Redondeado con round: " << round(valor) << endl;

    // CHAR Y ENTERO
    // en C++ cada letra es un numero de la tabla ASCII, asi que se pueden convertir :D
    cout << "\nCHAR Y ENTERO" << endl;
    char letra = 'A';
    int codigo = letra;                       // implicito, el char se vuelve su numero
    cout << "Codigo de A: " << codigo << endl;

    char otra = static_cast<char>(66);        // explicito, el numero se vuelve letra
    cout << "Letra del 66: " << otra << endl;

    cout << "A + 2 sin convertir: " << letra + 2 << endl;                      // da un numero, 67 xd
    cout << "A + 2 convertido a char: " << static_cast<char>(letra + 2) << endl;   // da la letra C

    // un truco muy usado, pasar un caracter digito a su valor numerico
    char digito = '7';
    int numero = digito - '0';   // restar el codigo del '0' nos da el numero real :D
    cout << "El caracter 7 como numero: " << numero << endl;

    // BOOL
    // la regla es sencilla, cero es false y todo lo demas es true :D
    cout << "\nBOOL" << endl;
    cout << boolalpha;   // boolalpha hace que se imprima true o false en vez de 1 o 0
    cout << "bool de 0: " << static_cast<bool>(0) << endl;
    cout << "bool de 1: " << static_cast<bool>(1) << endl;
    cout << "bool de -5: " << static_cast<bool>(-5) << endl;   // cualquier numero distinto de 0 es true
    cout << "bool de 0.1: " << static_cast<bool>(0.1) << endl;  // incluso un decimal chiquito xd

    // TEXTO A NUMERO
    // en C++ no se puede hacer int("25"), hay que usar funciones especiales :D
    cout << "\nTEXTO A NUMERO" << endl;
    string textoEntero = "25";
    string textoDecimal = "3.14";

    int n1 = stoi(textoEntero);      // stoi convierte un string a int
    double n2 = stod(textoDecimal);  // stod convierte un string a double
    cout << "stoi: " << n1 + 5 << endl;
    cout << "stod: " << n2 * 2 << endl;

    int binario = stoi("101", nullptr, 2);   // el 2 es la base, lee el texto como binario :D
    cout << "101 en binario es: " << binario << endl;

    // stoi lee hasta donde pueda y se detiene, como Gojo ignorando lo que no le importa xd
    cout << "stoi de 12abc: " << stoi("12abc") << endl;   // sale 12

    // NUMERO A TEXTO
    cout << "\nNUMERO A TEXTO" << endl;
    int edad = 20;
    string mensaje = "Tengo " + to_string(edad) + " anios";   // sin to_string truena al sumar texto con numero :-v
    cout << mensaje << endl;
    cout << "to_string de 3.5: " << to_string(3.5) << endl;   // sale 3.500000 con ceros extra xd

    // CASTING CON INPUT
    // leemos como texto con getline y despues convertimos, asi evitamos problemas :D
    cout << "\nCASTING CON INPUT" << endl;
    string num1, num2;
    cout << "Escribe un numero: ";
    getline(cin, num1);
    cout << "Escribe otro numero: ";
    getline(cin, num2);

    cout << "Sin convertir se pegan como texto: " << num1 + num2 << endl;   // 5 y 3 dan 53, no 8 xd
    cout << "Convertidos a int se suman bien: " << stoi(num1) + stoi(num2) << endl;

    // ERRORES COMUNES
    // si el texto no se puede convertir, stoi lanza un error llamado invalid_argument
    // con try y catch lo atrapamos para que el programa no truene :D
    cout << "\nERRORES COMUNES" << endl;
    string dato;
    cout << "Escribe un numero entero: ";
    getline(cin, dato);

    try {
        int numeroValido = stoi(dato);   // aqui intenta la conversion
        cout << "Conversion exitosa, el doble es " << numeroValido * 2 << endl;
    } catch (invalid_argument&) {
        // entra aqui si escribieron letras, como hola
        cout << "Eso no es un entero valido, ni Gojo lo convierte xd" << endl;
    } catch (out_of_range&) {
        // entra aqui si el numero es demasiado grande para un int
        cout << "Ese numero es demasiado grande, nivel de poder fuera de escala :-v" << endl;
    }

    // EJEMPLO REAL: PROMEDIO DE SENSORES
    // los datos llegan como texto, los convertimos y calculamos :D
    cout << "\nEJEMPLO REAL" << endl;
    vector<string> lecturasTexto = {"45", "72.5", "90", "60"};   // asi llegan de un archivo o un sensor

    double total = 0;
    for (int i = 0; i < lecturasTexto.size(); i++) {
        total = total + stod(lecturasTexto[i]);   // cada texto se convierte a double antes de sumar
    }

    double prom = total / lecturasTexto.size();
    cout << "Promedio de lecturas: " << prom << endl;

    // convertimos a texto para armar un mensaje, como cuando Jarvis reporta el estado de la armadura :D
    string reporte = "El promedio fue " + to_string(static_cast<int>(prom)) + " grados";
    cout << reporte << endl;

    // convertimos a entero para mostrar sin decimales
    cout << "Promedio sin decimales: " << static_cast<int>(prom) << endl;

    // resumen rapido
    // static_cast<tipo>(dato) es la forma moderna de convertir
    // stoi y stod pasan de texto a numero
    // to_string pasa de numero a texto
    // int entre int da int, hay que convertir uno a double para tener decimales
    // fin del programa, Avengers Assemble :D

    return 0;
}