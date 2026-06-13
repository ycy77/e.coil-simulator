---
entity_id: "protein.P0AC73"
entity_type: "protein"
name: "ebgC"
source_database: "UniProt"
source_id: "P0AC73"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ebgC b3077 JW3048"
---

# ebgC

`protein.P0AC73`

## Static

- Type: `protein`
- Source: `UniProt:P0AC73`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Required for full activity of the EbgA enzyme. Exact function not known.

## Biological Role

Component of evolved β-D-galactosidase (complex.ecocyc.CPLX0-3937).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco00511` Other glycan degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Required for full activity of the EbgA enzyme. Exact function not known.

## Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco00511` Other glycan degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3937|complex.ecocyc.CPLX0-3937]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b3077|gene.b3077]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AC73`
- `KEGG:ecj:JW3048;eco:b3077;ecoc:C3026_16805;`
- `GeneID:93778914;947581;`
- `GO:GO:0005829; GO:0044010`

## Notes

Evolved beta-galactosidase subunit beta
