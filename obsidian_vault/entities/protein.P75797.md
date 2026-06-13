---
entity_id: "protein.P75797"
entity_type: "protein"
name: "gsiB"
source_database: "UniProt"
source_id: "P75797"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gsiB yliB b0830 JW5111"
---

# gsiB

`protein.P75797`

## Static

- Type: `protein`
- Source: `UniProt:P75797`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex GsiABCD involved in glutathione import (PubMed:16109926). Binds glutathione (PubMed:30515393). {ECO:0000269|PubMed:16109926, ECO:0000269|PubMed:30515393}. gsiB encodes the periplasmic binding protein of a glutathione ABC importer . GsiB has been used to develop a biosensor specific for the detection of reduced glutathione

## Biological Role

Component of glutathione ABC transporter (complex.ecocyc.ABC-49-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex GsiABCD involved in glutathione import (PubMed:16109926). Binds glutathione (PubMed:30515393). {ECO:0000269|PubMed:16109926, ECO:0000269|PubMed:30515393}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-49-CPLX|complex.ecocyc.ABC-49-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0830|gene.b0830]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75797`
- `KEGG:ecj:JW5111;eco:b0830;`
- `GeneID:945459;`
- `GO:GO:0006974; GO:0016020; GO:0030288; GO:0034635; GO:0042938; GO:0055052; GO:1904680`

## Notes

Glutathione-binding protein GsiB
