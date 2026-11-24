// Run each statement separately in Neo4j Browser.
MATCH (p:Knowledge {id:'blair'})-[r]->(n) RETURN p,r,n;
MATCH (p:Knowledge {id:'blair'})-[:HAS_EXPERIENCE]->(r)-[:USES_TECHNOLOGY]->(t) RETURN t.name AS technology, collect(r.name) AS experience ORDER BY size(experience) DESC;
MATCH (u:Knowledge {label:'UseCase'})-[:COULD_USE]->(t)<-[:USES_TECHNOLOGY]-(r) RETURN u.name, t.name, collect(DISTINCT r.name);
MATCH (n:Knowledge) RETURN n.label, n.status, count(*) ORDER BY count(*) DESC;
MATCH (p:Knowledge {id:'blair'})-[:HAS_PROJECT]->(j)-[:DEMONSTRATES]->(s) RETURN j,s;
