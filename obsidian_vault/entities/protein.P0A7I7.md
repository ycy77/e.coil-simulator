---
entity_id: "protein.P0A7I7"
entity_type: "protein"
name: "ribA"
source_database: "UniProt"
source_id: "P0A7I7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ribA b1277 JW1269"
---

# ribA

`protein.P0A7I7`

## Static

- Type: `protein`
- Source: `UniProt:P0A7I7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the conversion of GTP to 2,5-diamino-6-ribosylamino-4(3H)-pyrimidinone 5'-phosphate (DARP), formate and pyrophosphate. {ECO:0000269|PubMed:235552}.

## Biological Role

Catalyzes GTP 7,8-8,9-dihydrolase (diphosphate-forming) (reaction.R00425). Component of GTP cyclohydrolase 2 (complex.ecocyc.GTP-CYCLOHYDRO-II-CPLX).

## Enriched Pathways

- `eco00740` Riboflavin metabolism (KEGG)
- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

FUNCTION: Catalyzes the conversion of GTP to 2,5-diamino-6-ribosylamino-4(3H)-pyrimidinone 5'-phosphate (DARP), formate and pyrophosphate. {ECO:0000269|PubMed:235552}.

## Pathways

- `eco00740` Riboflavin metabolism (KEGG)
- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00425|reaction.R00425]] `KEGG` `database` - via EC:3.5.4.25
- `is_component_of` --> [[complex.ecocyc.GTP-CYCLOHYDRO-II-CPLX|complex.ecocyc.GTP-CYCLOHYDRO-II-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1277|gene.b1277]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A7I7`
- `KEGG:ecj:JW1269;eco:b1277;ecoc:C3026_07500;`
- `GeneID:86859906;86946614;945763;`
- `GO:GO:0000287; GO:0003935; GO:0005525; GO:0005829; GO:0008270; GO:0009231; GO:0042803`
- `EC:3.5.4.25`

## Notes

GTP cyclohydrolase-2 (EC 3.5.4.25) (GTP cyclohydrolase II)
