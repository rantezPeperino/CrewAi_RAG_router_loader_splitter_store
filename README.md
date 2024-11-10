# CrewAi_RAG_router_loader_splitter_store
Proyecto multiagente con CrewAi con decorator (@crew,@task,@agent,@CrewBase), para realizar Rag con documentos pdf, html, csv.

Las tareas son las que ordenan el proyecto, los agentes las realizan, en este caso es   Process.sequential.
                route_document : definir que tipo de documento
                load_document  : cargar el documento            
                split_document : dividir el documento
                store_vectors  : almacenar los chunk del documento
        

-Se crearon 4 agentes
  -Route determina el tipo de archivo pdf, html, csv.
  -document_loader encargado de cargar el documento. Usando custom tool correspondiente PDFLoaderTool CSVLoaderTool HTMLLoaderTool
  -document_splitter encargado de dividir en chunk el documento
  -vector_store encargado de guardar en la base vectorial despues del llm.

  













