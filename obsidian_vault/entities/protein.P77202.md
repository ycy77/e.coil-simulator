---
entity_id: "protein.P77202"
entity_type: "protein"
name: "dsbG"
source_database: "UniProt"
source_id: "P77202"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dsbG ybdP b0604 JW0597"
---

# dsbG

`protein.P77202`

## Static

- Type: `protein`
- Source: `UniProt:P77202`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm.

## Enriched Summary

FUNCTION: Involved in disulfide bond formation. DsbG and DsbC are part of a periplasmic reducing system that controls the level of cysteine sulfenylation, and provides reducing equivalents to rescue oxidatively damaged secreted proteins such as ErfK, YbiS and YnhG. Probably also functions as a disulfide isomerase with a narrower substrate specificity than DsbC. DsbG is maintained in a reduced state by DsbD. Displays chaperone activity in both redox states in vitro. {ECO:0000269|PubMed:19965429}.

## Biological Role

Component of protein sulfenic acid reductase and chaperone DsbGoxidized (complex.ecocyc.CPLX0-10624), protein sulfenic acid reductase and chaperone DsbG (complex.ecocyc.DSBG-CPLX).

## Annotation

FUNCTION: Involved in disulfide bond formation. DsbG and DsbC are part of a periplasmic reducing system that controls the level of cysteine sulfenylation, and provides reducing equivalents to rescue oxidatively damaged secreted proteins such as ErfK, YbiS and YnhG. Probably also functions as a disulfide isomerase with a narrower substrate specificity than DsbC. DsbG is maintained in a reduced state by DsbD. Displays chaperone activity in both redox states in vitro. {ECO:0000269|PubMed:19965429}.

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-10624|complex.ecocyc.CPLX0-10624]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.DSBG-CPLX|complex.ecocyc.DSBG-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0604|gene.b0604]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77202`
- `KEGG:ecj:JW0597;eco:b0604;ecoc:C3026_03020;`
- `GeneID:945224;`
- `GO:GO:0003756; GO:0006457; GO:0030288; GO:0042803`

## Notes

Thiol:disulfide interchange protein DsbG
