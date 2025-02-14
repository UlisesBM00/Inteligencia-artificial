import random

class AgenteCarrera:
    def __init__(self, distancia_meta=100):
        self.posicion = 0
        self.distancia_meta = distancia_meta

    def percibir_entorno(self):
        if self.posicion >= self.distancia_meta:
            return "meta"
        return random.choice(["despejado", "obstáculo"])

    def decidir_accion(self, entorno):
        if entorno == "meta":
            return "parar"
        elif entorno == "obstáculo":
            return "saltar"
        else:
            return "avanzar"

    def actuar(self, accion):
        if accion == "avanzar":
            self.posicion += 10
            print("🏃 Avanzando... Posición:", self.posicion)
        elif accion == "saltar":
            print("🤸 Saltando obstáculo...")
        elif accion == "parar":
            print("🎉 ¡Meta alcanzada! Carrera finalizada.")
    
    def correr(self):
        while True:
            entorno = self.percibir_entorno()
            accion = self.decidir_accion(entorno)
            self.actuar(accion)
            if accion == "parar":
                break

# Simulación
carrera = AgenteCarrera()
carrera.correr()
