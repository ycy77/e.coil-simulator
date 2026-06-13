---
entity_id: "protein.P0AF01"
entity_type: "protein"
name: "modB"
source_database: "UniProt"
source_id: "P0AF01"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "modB chlJ b0764 JW0747"
---

# modB

`protein.P0AF01`

## Static

- Type: `protein`
- Source: `UniProt:P0AF01`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Part of the binding-protein-dependent transport system for molybdenum; probably responsible for the translocation of the substrate across the membrane. ModB is the predicted integral membrane subunit of an ABC transporter that mediates the high affinity uptake of molybdate. modB encodes a hydrophobic protein with 5 predicted transmembrane regions .

## Biological Role

Component of molybdate ABC transporter (complex.ecocyc.ABC-19-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the binding-protein-dependent transport system for molybdenum; probably responsible for the translocation of the substrate across the membrane.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-19-CPLX|complex.ecocyc.ABC-19-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0764|gene.b0764]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AF01`
- `KEGG:ecj:JW0747;eco:b0764;ecoc:C3026_03875;`
- `GeneID:86863274;93776717;945361;`
- `GO:GO:0005886; GO:0015098; GO:0015689; GO:0016020; GO:0055052; GO:0070614`

## Notes

Molybdenum transport system permease protein ModB
