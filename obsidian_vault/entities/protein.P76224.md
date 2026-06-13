---
entity_id: "protein.P76224"
entity_type: "protein"
name: "ynjC"
source_database: "UniProt"
source_id: "P76224"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ynjC b1755 JW5285"
---

# ynjC

`protein.P76224`

## Static

- Type: `protein`
- Source: `UniProt:P76224`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Probably part of the binding-protein-dependent transport system YnjCD. Probably responsible for the translocation of the substrate across the membrane. YnjC is predicted to be the inner membrane subunit of a putative ATP-dependent transporter complex . YnjC is predicted to be an inner membrane protein with twelve transmembrane domains; topology analysis suggests the C-terminus is located in the cytoplasm . A ynjC nonsynonymous mutation (YnjC P213S) contributes to fitness in the presence of colistin .

## Biological Role

Component of putative transport complex, ABC superfamily (complex.ecocyc.ABC-48-CPLX).

## Annotation

FUNCTION: Probably part of the binding-protein-dependent transport system YnjCD. Probably responsible for the translocation of the substrate across the membrane.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-48-CPLX|complex.ecocyc.ABC-48-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1755|gene.b1755]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76224`
- `KEGG:ecj:JW5285;eco:b1755;ecoc:C3026_10020;`
- `GeneID:946273;`
- `GO:GO:0005886; GO:0016020; GO:0043190; GO:0055052; GO:0055085`

## Notes

Inner membrane ABC transporter permease protein YnjC
