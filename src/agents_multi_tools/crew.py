from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from tools.custom_tool import PDFLoaderTool, HTMLLoaderTool, CSVLoaderTool, DocumentSplitterTool, VectorDBTool

@CrewBase
class AgentsMultiToolsCrew():
    """Crew para procesamiento de documentos"""

    @agent
    def document_loader(self) -> Agent:
        return Agent(
            config=self.agents_config['document_loader'],
            tools=[PDFLoaderTool(),CSVLoaderTool(),HTMLLoaderTool()],
            verbose=True
        )

    # @agent
    # def html_loader(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['html_loader'],
    #         tools=[HTMLLoaderTool()],
    #         verbose=True
    #     )


    # @agent
    # def csv_loader(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['csv_loader'],
    #         tools=[CVSLoaderTool()],
    #         verbose=True
    #     )


    @agent
    def router(self) -> Agent:
        return Agent(
            config=self.agents_config['router'],
            verbose=True
        )

    @agent
    def document_splitter(self) -> Agent:
        return Agent(
            config=self.agents_config['document_splitter'],
            tools=[DocumentSplitterTool()],
            verbose=True
        )

    @agent
    def vector_store(self) -> Agent:
        return Agent(
            config=self.agents_config['vector_store'],
            tools=[VectorDBTool()],
            verbose=True
        )

    @task
    def route_document(self, file_path: str = None) -> Task:
        return Task(
			config=self.tasks_config['route_document'],
        	verbose=True
        )

    @task
    def load_document(self, file_path: str = None) -> Task:
        return Task(
            config = self.tasks_config['load_document'],
            context=[self.route_document()],
        	verbose=True
        )            

    @task
    def split_document(self) -> Task:
        return Task(
            config = self.tasks_config['split_document'],
        	verbose=True
        )

    @task
    def store_vectors(self) -> Task:
        return Task(
            config = self.tasks_config['store_vectors'],
        	verbose=True
        )

    @crew
    def crew(self) -> Crew:
        """Crear y configurar el crew"""
        return Crew(
            agents=[
                self.router(),
                self.document_loader(),
                self.document_splitter(),
                self.vector_store()
            ],
            tasks=[
                # Llamar a las funciones para obtener las instancias de Task
                self.route_document(),
                self.load_document(),
                self.split_document(),
                self.store_vectors()
            ],
            process=Process.sequential,
            verbose=True
        )