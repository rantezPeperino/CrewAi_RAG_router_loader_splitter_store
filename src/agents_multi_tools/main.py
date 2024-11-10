from crewai import Process
from crew import AgentsMultiToolsCrew
import os
from dotenv import load_dotenv



def main():
    load_dotenv()
        # Configurar la API key de OpenAI
    os.environ["OPENAI_API_KEY"] = ""
    
    # Solicitar al usuario el path del archivo PDF
    file_path = input("Por favor ingrese la ruta del archivo PDF a cargar: ")

    # Inicializar el Crew y ejecutar
    crew_instance = AgentsMultiToolsCrew()
    
    # Configurar las tareas con el file_path
    result = crew_instance.crew().kickoff(
        inputs={"file_path": file_path}
    )

    # Mostrar el resultado final
    print("\nProceso completado. Resultado:")
    print(result)

if __name__ == "__main__":
    main()