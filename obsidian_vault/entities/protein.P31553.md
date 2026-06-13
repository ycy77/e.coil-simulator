---
entity_id: "protein.P31553"
entity_type: "protein"
name: "caiT"
source_database: "UniProt"
source_id: "P31553"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01049, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:20357772, ECO:0000269|PubMed:20829798}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01049, ECO:0000269|PubMed:20357772, ECO:0000269|PubMed:20829798}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "caiT yaaP b0040 JW0039"
---

# caiT

`protein.P31553`

## Static

- Type: `protein`
- Source: `UniProt:P31553`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01049, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:20357772, ECO:0000269|PubMed:20829798}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01049, ECO:0000269|PubMed:20357772, ECO:0000269|PubMed:20829798}.

## Enriched Summary

FUNCTION: Catalyzes the exchange of L-carnitine for gamma-butyrobetaine (PubMed:12163501, PubMed:20829798, PubMed:30846799). Can also transport D-carnitine and, with lower efficiency, acetyl-L-carnitine and glycine betaine (PubMed:12163501). {ECO:0000269|PubMed:12163501, ECO:0000269|PubMed:20829798, ECO:0000269|PubMed:30846799}.

## Biological Role

Component of L-carnitine:γ-butyrobetaine antiporter (complex.ecocyc.CPLX0-7906).

## Annotation

FUNCTION: Catalyzes the exchange of L-carnitine for gamma-butyrobetaine (PubMed:12163501, PubMed:20829798, PubMed:30846799). Can also transport D-carnitine and, with lower efficiency, acetyl-L-carnitine and glycine betaine (PubMed:12163501). {ECO:0000269|PubMed:12163501, ECO:0000269|PubMed:20829798, ECO:0000269|PubMed:30846799}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7906|complex.ecocyc.CPLX0-7906]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3 | EcoCyc transporter component coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b0040|gene.b0040]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31553`
- `KEGG:ecj:JW0039;eco:b0040;ecoc:C3026_00210;`
- `GeneID:93777395;944765;`
- `GO:GO:0005886; GO:0009437; GO:0015226; GO:0015879; GO:0022857; GO:0044667; GO:1900751`

## Notes

L-carnitine/gamma-butyrobetaine antiporter
