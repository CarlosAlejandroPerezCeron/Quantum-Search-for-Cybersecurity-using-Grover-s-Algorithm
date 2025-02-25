from execute_grover import grover_search
from ai_model import train_ai_model

def main():
    """
    Ejecuta el Algoritmo de Grover y el modelo de IA.
    """
    print("🔍 Ejecutando el Algoritmo de Grover...")
    grover_results = grover_search(3, 2)

    print("\n🤖 Entrenando el modelo de Machine Learning...")
    model = train_ai_model()

    print("\n✅ Proyecto completado.")

if __name__ == "__main__":
    main()
