---
entity_id: "protein.P69330"
entity_type: "protein"
name: "citD"
source_database: "UniProt"
source_id: "P69330"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "citD ybdX b0617 JW0609"
---

# citD

`protein.P69330`

## Static

- Type: `protein`
- Source: `UniProt:P69330`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Covalent carrier of the coenzyme of citrate lyase.

## Biological Role

Component of citrate lyase (complex.ecocyc.ACECITLY-CPLX), citrate lyase [acyl carrier protein] component (complex.ecocyc.ACPSUB-CPLX), citrate lyase, inactive (complex.ecocyc.CITLY-CPLX).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Covalent carrier of the coenzyme of citrate lyase.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (3)

- `is_component_of` --> [[complex.ecocyc.ACECITLY-CPLX|complex.ecocyc.ACECITLY-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6
- `is_component_of` --> [[complex.ecocyc.ACPSUB-CPLX|complex.ecocyc.ACPSUB-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6
- `is_component_of` --> [[complex.ecocyc.CITLY-CPLX|complex.ecocyc.CITLY-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b0617|gene.b0617]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69330`
- `KEGG:ecj:JW0609;eco:b0617;ecoc:C3026_03085;`
- `GeneID:86863137;93776868;945415;`
- `GO:GO:0005737; GO:0006084; GO:0006101; GO:0009346; GO:0051192`

## Notes

Citrate lyase acyl carrier protein (Citrate lyase gamma chain)
