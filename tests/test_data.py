import json, unittest
from pathlib import Path
class Dataset(unittest.TestCase):
 def test_integrity(self):
  g=json.loads((Path(__file__).resolve().parents[1]/'data/graph.json').read_text()); ids={n['id'] for n in g['nodes']}; self.assertEqual(len(ids),len(g['nodes'])); self.assertTrue(all(e['source'] in ids and e['target'] in ids for e in g['edges'])); self.assertEqual(len(g['edges']),len({(e['source'],e['target'],e['type']) for e in g['edges']}))
if __name__=='__main__': unittest.main()
