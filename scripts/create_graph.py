from indexify import IndexifyClient, ExtractionGraph

client = IndexifyClient()


def create_extraction_graph():
    with open("scripts/graph.yaml", "r") as file:
        extraction_graph_spec = file.read()
        extraction_graph = ExtractionGraph.from_yaml(extraction_graph_spec)
        client.create_extraction_graph(extraction_graph)


if __name__ == "__main__":
    create_extraction_graph()
