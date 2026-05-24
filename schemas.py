# Node Labels
NODE_TEXT_CHUNK = "TextChunk"
NODE_CHEMICAL = "Chemical"
NODE_DISEASE = "Disease"

# Relationship Types
REL_CO_OCCURS_WITH = "CO_OCCURS_WITH"
REL_MENTIONED_IN = "MENTIONED_IN"

# Arrays for clean looping in your embedding script
ALLOWED_NODES = [NODE_TEXT_CHUNK, NODE_CHEMICAL, NODE_DISEASE]
ALLOWED_EDGES = [REL_CO_OCCURS_WITH, REL_MENTIONED_IN]

#LLM CONTEXT PROMPT
BIOMEDICAL_GRAPH_SCHEMA_CONTEXT = """
The graph database consists of the following structure:

Node Labels & Properties:
- `TextChunk`: A raw text passage extracted from the biomedical literature.
- `Chemical`: A specific chemical compound or drug entity. Property: {name: STRING}
- `Disease`: A specific medical condition or disease entity. Property: {name: STRING}

Relationship Types:
- (:Chemical)-[:CO_OCCURS_WITH]->(:Disease) : Indicates a chemical and a disease frequently appear together in the data.
- (:Chemical)-[:MENTIONED_IN]->(:TextChunk) : Connects a chemical entity to its originating text source.
- (:Disease)-[:MENTIONED_IN]->(:TextChunk) : Connects a disease entity to its originating text source.
"""