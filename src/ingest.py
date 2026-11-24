import json, os
from pathlib import Path
from neo4j import GraphDatabase
G=json.loads((Path(__file__).resolve().parents[1]/'data/graph.json').read_text())
with GraphDatabase.driver(os.getenv('NEO4J_URI','bolt://localhost:7687'),auth=('neo4j',os.environ['NEO4J_PASSWORD'])) as d:
 d.verify_connectivity()
 d.execute_query('CREATE CONSTRAINT knowledge_id IF NOT EXISTS FOR (n:Knowledge) REQUIRE n.id IS UNIQUE')
 d.execute_query('UNWIND $rows AS row MERGE (n:Knowledge {id:row.id}) SET n += row',rows=G['nodes'])
 for t in sorted({r['type'] for r in G['edges']}):
  d.execute_query(f'UNWIND $rows AS row MATCH (a:Knowledge {{id:row.source}}),(b:Knowledge {{id:row.target}}) MERGE (a)-[r:{t}]->(b) SET r.status=row.status, r.classification=row.classification, r.source_url=row.source_url',rows=[r for r in G['edges'] if r['type']==t])
 print('Imported',len(G['nodes']),'nodes and',len(G['edges']),'relationships')
