# KnowledgeAxis — Blair Page

![KnowledgeAxis](assets/mark.svg)

Professional knowledge graph demonstration derived from selected professional sections of the supplied portfolio index.html. Source claims are self-reported. Proposed Neo4j/CloudFormation use cases are demonstrations, not claims of prior employment experience. Dataset is curated, not exhaustive; private personal details are excluded.

## GitHub Pages
Upload repository contents to main; Settings → Pages → Deploy from branch → main / root. The static explorer works without Neo4j. JSON and CSV are canonical data exports; graph.js is the browser snapshot. After editing JSON regenerate graph.js with `python -c "import pathlib; p=pathlib.Path('data'); (p/'graph.js').write_text('window.GRAPH='+ (p/'graph.json').read_text()+';')"` and regenerate CSVs if needed.

## Local Neo4j
Install Docker with Compose, Python 3.10+, and Git. Copy `.env.example` to `.env`, replace password with a unique long password (never commit it). Run:

```sh
docker compose up -d
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
set -a; source .env; set +a
python src/ingest.py
```
Wait for Neo4j to finish starting before ingestion. Open http://localhost:7474, connect using bolt://localhost:7687 and user neo4j. Run statements in cypher/explore.cypher individually. Ingestion is repeatable via MERGE; removed records are not automatically deleted. Stop with `docker compose down`; `docker compose down -v` destroys the data.

## AWS lab
Prerequisites: AWS CLI authenticated, Session Manager plugin, IAM permission to deploy EC2/IAM and start SSM sessions, existing VPC and subnet with outbound internet access (NAT or public IP routing) for Docker packages/image and SSM. No inbound rules. Choose a subnet in the supplied VPC. This is a single-instance lab, not production HA. EC2, EBS and networking may incur charges.

```sh
aws cloudformation deploy --template-file aws/neo4j.yaml --stack-name knowledgeaxis --capabilities CAPABILITY_IAM --parameter-overrides VpcId=vpc-REPLACE SubnetId=subnet-REPLACE
aws cloudformation describe-stacks --stack-name knowledgeaxis --query 'Stacks[0].Outputs'
aws ssm start-session --target i-REPLACE
```
Once connected, wait for cloud-init (`sudo cloud-init status --wait`), then run on instance:

```sh
read -rsp 'New Neo4j password: ' PW; echo
sudo docker run -d --name knowledgeaxis --restart unless-stopped -p 127.0.0.1:7474:7474 -p 127.0.0.1:7687:7687 -v knowledgeaxis-data:/data -e "NEO4J_AUTH=neo4j/$PW" neo4j:5.26-community
unset PW
exit
```
Open two local terminals for port forwarding:

```sh
aws ssm start-session --target i-REPLACE --document-name AWS-StartPortForwardingSession --parameters '{"portNumber":["7687"],"localPortNumber":["7687"]}'
```
```sh
aws ssm start-session --target i-REPLACE --document-name AWS-StartPortForwardingSession --parameters '{"portNumber":["7474"],"localPortNumber":["7474"]}'
```
Stop any local Neo4j using these ports first. In a third terminal activate the Python environment, export NEO4J_PASSWORD using a secure prompt, and run `python src/ingest.py`. Browser at localhost:7474. Do not publish credentials or open database ports. Back up data before deleting the stack; root disk is deleted on termination. Cleanup: `aws cloudformation delete-stack --stack-name knowledgeaxis`.

## Production considerations
Use private subnets, managed secrets, TLS, backups with restore drills, monitoring, least privilege, patching and access reviews. Enterprise clustering and managed graph hosting require separate architecture/licensing decisions. This repository has not been deployed to AWS or tested against a running Neo4j server in the authoring environment.

## Data model
All nodes have label Knowledge and a `label` category property. Unique id, name, detail, status and source. Relationship types represent documented experience, portfolio demonstrations or inferred applications. No inference should be treated as verified skill mastery. Source snapshot: supplied portfolio HTML, November 2026.
