from llama_index.core.llama_pack import BaseLlamaPack
from llama_index.packs.neo4j_query_engine import Neo4jQueryEnginePack


def test_class():
    names_of_base_classes = [b.__name__ for b in Neo4jQueryEnginePack.__mro__]
    assert BaseLlamaPack.__name__ in names_of_base_classes
