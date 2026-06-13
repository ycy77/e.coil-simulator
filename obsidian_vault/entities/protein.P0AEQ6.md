---
entity_id: "protein.P0AEQ6"
entity_type: "protein"
name: "glnP"
source_database: "UniProt"
source_id: "P0AEQ6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glnP b0810 JW0795"
---

# glnP

`protein.P0AEQ6`

## Static

- Type: `protein`
- Source: `UniProt:P0AEQ6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Part of the binding-protein-dependent transport system for glutamine; probably responsible for the translocation of the substrate across the membrane. GlnP is the predicted integral membrane subunit of an L-glutamine ABC transport sytem

## Biological Role

Component of L-glutamine ABC transporter (complex.ecocyc.ABC-12-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the binding-protein-dependent transport system for glutamine; probably responsible for the translocation of the substrate across the membrane.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-12-CPLX|complex.ecocyc.ABC-12-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0810|gene.b0810]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEQ6`
- `KEGG:ecj:JW0795;eco:b0810;ecoc:C3026_05100;`
- `GeneID:93776618;945621;`
- `GO:GO:0005886; GO:0006865; GO:0006868; GO:0015186; GO:0016020; GO:0055052; GO:1903803`

## Notes

Glutamine transport system permease protein GlnP
