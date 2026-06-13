---
entity_id: "protein.P0AB58"
entity_type: "protein"
name: "lapB"
source_database: "UniProt"
source_id: "P0AB58"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00994, ECO:0000269|PubMed:24187084, ECO:0000269|PubMed:24722986}; Single-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00994, ECO:0000269|PubMed:24187084}; Cytoplasmic side {ECO:0000255|HAMAP-Rule:MF_00994, ECO:0000269|PubMed:24187084}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lapB yciM b1280 JW1272"
---

# lapB

`protein.P0AB58`

## Static

- Type: `protein`
- Source: `UniProt:P0AB58`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00994, ECO:0000269|PubMed:24187084, ECO:0000269|PubMed:24722986}; Single-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00994, ECO:0000269|PubMed:24187084}; Cytoplasmic side {ECO:0000255|HAMAP-Rule:MF_00994, ECO:0000269|PubMed:24187084}.

## Enriched Summary

FUNCTION: Modulates cellular lipopolysaccharide (LPS) levels by regulating LpxC, which is involved in lipid A biosynthesis. Regulates the proteolytic activity of FtsH towards LpxC by acting as an adapter protein which interacts with FtsH via its transmembrane helices while its cytoplasmic domain recruits LpxC for degradation by FtsH. May also coordinate assembly of proteins involved in LPS synthesis at the plasma membrane. {ECO:0000255|HAMAP-Rule:MF_00994, ECO:0000269|PubMed:24266962, ECO:0000269|PubMed:24722986, ECO:0000269|PubMed:33260377, ECO:0000269|PubMed:35931690}.

## Biological Role

Component of lipopolysaccharide assembly protein B (complex.ecocyc.CPLX0-13399).

## Annotation

FUNCTION: Modulates cellular lipopolysaccharide (LPS) levels by regulating LpxC, which is involved in lipid A biosynthesis. Regulates the proteolytic activity of FtsH towards LpxC by acting as an adapter protein which interacts with FtsH via its transmembrane helices while its cytoplasmic domain recruits LpxC for degradation by FtsH. May also coordinate assembly of proteins involved in LPS synthesis at the plasma membrane. {ECO:0000255|HAMAP-Rule:MF_00994, ECO:0000269|PubMed:24266962, ECO:0000269|PubMed:24722986, ECO:0000269|PubMed:33260377, ECO:0000269|PubMed:35931690}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-13399|complex.ecocyc.CPLX0-13399]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1280|gene.b1280]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AB58`
- `KEGG:ecj:JW1272;eco:b1280;ecoc:C3026_07515;`
- `GeneID:93775403;944858;`
- `GO:GO:0005506; GO:0005829; GO:0005886; GO:0008653; GO:0009898; GO:0046872; GO:0046890`

## Notes

Lipopolysaccharide assembly protein B (Lipopolysaccharide regulatory protein) (LpxC degradation adapter protein B)
