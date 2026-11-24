// Run individually
MATCH (n:Knowledge) WHERE n.classification IS NULL OR n.source IS NULL RETURN n;
MATCH (a:Knowledge)-[r]->(b:Knowledge) RETURN type(r),r.status,count(*) ORDER BY count(*) DESC;
MATCH (n:Knowledge) RETURN n.label,n.status,count(*) ORDER BY n.label;
