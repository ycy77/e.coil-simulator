---
entity_id: "protein.P75799"
entity_type: "protein"
name: "gsiD"
source_database: "UniProt"
source_id: "P75799"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gsiD yliD b0832 JW0816"
---

# gsiD

`protein.P75799`

## Static

- Type: `protein`
- Source: `UniProt:P75799`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex GsiABCD involved in glutathione import. Probably responsible for the translocation of the substrate across the membrane. {ECO:0000305|PubMed:16109926}. gsiD encodes one of two predicted integral membrane subunits of a glutathione ABC importer

## Biological Role

Component of glutathione ABC transporter (complex.ecocyc.ABC-49-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex GsiABCD involved in glutathione import. Probably responsible for the translocation of the substrate across the membrane. {ECO:0000305|PubMed:16109926}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-49-CPLX|complex.ecocyc.ABC-49-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0832|gene.b0832]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75799`
- `KEGG:ecj:JW0816;eco:b0832;ecoc:C3026_05215;`
- `GeneID:945461;`
- `GO:GO:0005886; GO:0016020; GO:0034634; GO:0034775; GO:0055052; GO:0071916`

## Notes

Glutathione transport system permease protein GsiD
