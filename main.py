import xml.etree.ElementTree as ET #para lectura de los xml
import os #manipulacion de archivos.

###############################################
#COMENZANDO CON CLASE VUELO. 
class Vuelo:
    def __init__(self, codigo, origen, destino, duracion, aerolinea): #iniciando lso valores que tendra.
        
        self.codigo = codigo
        self.origen = origen
        self.destino = destino
        self.duracion = int(duracion) #convertirlos a enteros para gestiones posteriores...!
        self.aerolinea = aerolinea

    def __str__(self):
        return (f"Código: {self.codigo}\n"
                f"Origen: {self.origen}\n"
                f"Destino: {self.destino}\n"
                f"Duración: {self.duracion} horas\n"
                f"Aerolínea: {self.aerolinea}\n")


###############################################
#CLASE QUE SE UTILIZARA PARA HACER L
class GestorVuelos:
    def __init__(self):
        self.vuelos = {}

    def cargar_archivo(self, path=None): # se intento probar una comparacion de valores para quitar repetidos.
        if not path:
            path = os.path.join(os.path.dirname(__file__), 'entrada.xml') #SI NO SE AGREGA ALGO SE TOMA DE PREDETERMINADO.
        try:
            tree = ET.parse(path)
            root = tree.getroot()
            for vuelo_element in root.findall('vuelo'):
                codigo = vuelo_element.find('codigo').text
                if codigo in self.vuelos:
                    print(f"✘ Código duplicado: {codigo}. No se agrega este vuelo.")
                    continue
                origen = vuelo_element.find('origen').text
                destino = vuelo_element.find('destino').text
                duracion = vuelo_element.find('duracion').text
                aerolinea = vuelo_element.find('aerolinea').text
                vuelo = Vuelo(codigo, origen, destino, duracion, aerolinea)
                self.vuelos[codigo] = vuelo
            print(f"✔ ARCHIVO CARGADO CORRECTAMENTE {len(self.vuelos)} VUELOS.")
        except Exception as e:
            print(f"ERROR AL LEER EL ARCHIVO, EL ERROR ES: {e}")

    def detalle_vuelo(self, codigo):
        vuelo = self.vuelos.get(codigo)
        if vuelo:
            print(vuelo)
        else:
            print("VUELO NO ENCONTRADO")





###############################################
#inicializando la agrupacion....
    def agrupar_por_aerolinea(self):
        agrupado = {}
        for vuelo in self.vuelos.values():
            if vuelo.aerolinea not in agrupado:
                agrupado[vuelo.aerolinea] = []
            agrupado[vuelo.aerolinea].append(vuelo.codigo)
        for aerolinea, codigos in agrupado.items():
            print(f"Aerolínea: {aerolinea}")
            for codigo in codigos:
                print(f"  - {codigo}")
            print()



###############################################
#ordenando...
    def ordenar_por_duracion(self):
        ordenados = sorted(self.vuelos.values(), key=lambda v: v.duracion, reverse=True)
        print("VUELOS ORDENADOS DE MAYOR DURACION A MENOR DURACION:")
        for vuelo in ordenados:
            print(f"{vuelo.codigo} - {vuelo.duracion} horas")






###############################################
def mostrar_menu():
    print("\nMENÚ PRINCIPAL")
    print("1. Cargar Archivo")
    print("2. Detalle de vuelo específico")
    print("3. Agrupar vuelos por aerolínea")
    print("4. Ordenar más duración a menor duración")
    print("5. Salir")



###############################################
def main():
    gestor = GestorVuelos()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            ruta = input("Ingrese la ruta del archivo XML (Enter para usar 'entrada.xml'): ")
            gestor.cargar_archivo(ruta.strip() if ruta else None)
        elif opcion == '2':
            codigo = input("Ingrese el código del vuelo: ")
            gestor.detalle_vuelo(codigo)
        elif opcion == '3':
            gestor.agrupar_por_aerolinea()
        elif opcion == '4':
            gestor.ordenar_por_duracion()
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")






if __name__ == "__main__":
    main()
