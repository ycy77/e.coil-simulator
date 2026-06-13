---
entity_id: "protein.P0A6E4"
entity_type: "protein"
name: "argG"
source_database: "UniProt"
source_id: "P0A6E4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "argG b3172 JW3140"
---

# argG

`protein.P0A6E4`

## Static

- Type: `protein`
- Source: `UniProt:P0A6E4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

Argininosuccinate synthase (EC 6.3.4.5) (Citrulline--aspartate ligase)

## Biological Role

Component of argininosuccinate synthetase (complex.ecocyc.CPLX0-238).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

Argininosuccinate synthase (EC 6.3.4.5) (Citrulline--aspartate ligase)

## Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-238|complex.ecocyc.CPLX0-238]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b3172|gene.b3172]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6E4`
- `KEGG:ecj:JW3140;eco:b3172;ecoc:C3026_17275;`
- `GeneID:947590;`
- `GO:GO:0000050; GO:0000053; GO:0004055; GO:0005524; GO:0005737; GO:0005829; GO:0006526; GO:0042802; GO:0042803`
- `EC:6.3.4.5`

## Notes

Argininosuccinate synthase (EC 6.3.4.5) (Citrulline--aspartate ligase)
