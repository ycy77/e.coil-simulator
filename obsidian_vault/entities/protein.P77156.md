---
entity_id: "protein.P77156"
entity_type: "protein"
name: "ydcU"
source_database: "UniProt"
source_id: "P77156"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ydcU b1442 JW1437"
---

# ydcU

`protein.P77156`

## Static

- Type: `protein`
- Source: `UniProt:P77156`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Probably part of the ABC transporter complex YdcSTUV. Probably responsible for the translocation of the substrate across the membrane. {ECO:0000305}. YdcU is the predicted inner membrane component of an uncharacterized ABC transporter .

## Biological Role

Component of putative transport complex, ABC superfamily (complex.ecocyc.ABC-51-CPLX).

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)

## Annotation

FUNCTION: Probably part of the ABC transporter complex YdcSTUV. Probably responsible for the translocation of the substrate across the membrane. {ECO:0000305}.

## Pathways

- `eco02024` Quorum sensing (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-51-CPLX|complex.ecocyc.ABC-51-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1442|gene.b1442]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77156`
- `KEGG:ecj:JW1437;eco:b1442;ecoc:C3026_08390;`
- `GeneID:945976;`
- `GO:GO:0005886; GO:0015417; GO:0016020; GO:0055052; GO:0055085; GO:1903711`

## Notes

Inner membrane ABC transporter permease protein YdcU
