import json, yaml

def transformar_json2yaml(fi_json):
  with open(fi_json) as fi:
    j = fi.read()
  d = json.loads(j)
  return yaml.dump(d)

def escribir(string, destino):
  with open(destino) as fo:
    fo.write(string)

# /tmp/ejemplo/[in,out]
escribir(
  transformar_json2yaml("/tmp/ejemplo/in/input.json"),
  "/tmp/ejemplo/out/output.yaml"
)
