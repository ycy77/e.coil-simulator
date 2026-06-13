---
entity_id: "protein.P42592"
entity_type: "protein"
name: "ygjK"
source_database: "UniProt"
source_id: "P42592"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ygjK b3080 JW3051"
---

# ygjK

`protein.P42592`

## Static

- Type: `protein`
- Source: `UniProt:P42592`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Glucoside hydrolase that cleaves the alpha-1,3-glucosidic linkage in nigerose. Has very low activity towards maltooligosaccharides, soluble starch, nigerotriose, kojibiose and trehalose. {ECO:0000269|PubMed:18586271}. YgjK belongs to the glycoside hydrolase family 63 and was shown to possess α-1,3-glucosyl hydrolase activity. Of the tested substrates, nigerose was the best; however, it is unlikely to be the natural substrate of the enzyme . YgjK is able to hydrolyze 2-O-α-D-glucopyranosyl-D-galactopyranose . The point mutations E727A and D324N convert the enzyme to a glycosynthase . Crystal structures of YgjK alone and in complex with various sugars have been solved .

## Biological Role

Catalyzes RXN0-5395 (reaction.ecocyc.RXN0-5395).

## Annotation

FUNCTION: Glucoside hydrolase that cleaves the alpha-1,3-glucosidic linkage in nigerose. Has very low activity towards maltooligosaccharides, soluble starch, nigerotriose, kojibiose and trehalose. {ECO:0000269|PubMed:18586271}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5395|reaction.ecocyc.RXN0-5395]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3080|gene.b3080]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P42592`
- `KEGG:ecj:JW3051;eco:b3080;ecoc:C3026_16820;`
- `GeneID:947596;`
- `GO:GO:0004555; GO:0005993; GO:0006974; GO:0009313; GO:0015926; GO:0046872; GO:1902687`
- `EC:3.2.1.-`

## Notes

Glucosidase YgjK (EC 3.2.1.-)
