---
entity_id: "protein.P0A9H9"
entity_type: "protein"
name: "cheZ"
source_database: "UniProt"
source_id: "P0A9H9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:12644507}. Note=Colocalizes with CheA chemoreceptor patches near the cell poles, which requires CheA(short)."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cheZ b1881 JW1870"
---

# cheZ

`protein.P0A9H9`

## Static

- Type: `protein`
- Source: `UniProt:P0A9H9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:12644507}. Note=Colocalizes with CheA chemoreceptor patches near the cell poles, which requires CheA(short).

## Enriched Summary

FUNCTION: Plays an important role in bacterial chemotaxis signal transduction pathway by accelerating the dephosphorylation of phosphorylated CheY (CheY-P). {ECO:0000269|PubMed:10852888, ECO:0000269|PubMed:8820640}.

## Biological Role

Component of chemotaxis protein CheZ (complex.ecocyc.CHEZ-CPLX).

## Enriched Pathways

- `eco02030` Bacterial chemotaxis (KEGG)

## Annotation

FUNCTION: Plays an important role in bacterial chemotaxis signal transduction pathway by accelerating the dephosphorylation of phosphorylated CheY (CheY-P). {ECO:0000269|PubMed:10852888, ECO:0000269|PubMed:8820640}.

## Pathways

- `eco02030` Bacterial chemotaxis (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CHEZ-CPLX|complex.ecocyc.CHEZ-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1881|gene.b1881]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9H9`
- `KEGG:ecj:JW1870;eco:b1881;ecoc:C3026_10700;`
- `GeneID:75171954;946392;`
- `GO:GO:0004721; GO:0005829; GO:0005886; GO:0006935; GO:0009288; GO:0042802; GO:0050920; GO:0051219; GO:0071978; GO:0098561; GO:1902021`
- `EC:3.1.3.-`

## Notes

Protein phosphatase CheZ (EC 3.1.3.-) (Chemotaxis protein CheZ)
