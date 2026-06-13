---
entity_id: "protein.P0AED0"
entity_type: "protein"
name: "uspA"
source_database: "UniProt"
source_id: "P0AED0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "uspA b3495 JW3462"
---

# uspA

`protein.P0AED0`

## Static

- Type: `protein`
- Source: `UniProt:P0AED0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Required for resistance to DNA-damaging agents.

## Biological Role

Component of universal stress protein A (complex.ecocyc.CPLX0-8585).

## Annotation

FUNCTION: Required for resistance to DNA-damaging agents.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8585|complex.ecocyc.CPLX0-8585]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3495|gene.b3495]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AED0`
- `KEGG:ecj:JW3462;eco:b3495;ecoc:C3026_18930;`
- `GeneID:86862112;93778498;948007;`
- `GO:GO:0005737; GO:0006950; GO:0016020; GO:0042802; GO:0042803`

## Notes

Universal stress protein A
