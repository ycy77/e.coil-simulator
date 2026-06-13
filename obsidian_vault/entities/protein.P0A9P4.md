---
entity_id: "protein.P0A9P4"
entity_type: "protein"
name: "trxB"
source_database: "UniProt"
source_id: "P0A9P4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "placeholder"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "trxB b0888 JW0871"
---

# trxB

`protein.P0A9P4`

## Static

- Type: `protein`
- Source: `UniProt:P0A9P4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

Thioredoxin reductase (TRXR) (EC 1.8.1.9)

## Biological Role

Component of thioredoxin reductase (complex.ecocyc.THIOREDOXIN-REDUCT-NADPH-CPLX).

## Enriched Pathways

- `eco00450` Selenocompound metabolism (KEGG)

## Annotation

Thioredoxin reductase (TRXR) (EC 1.8.1.9)

## Pathways

- `eco00450` Selenocompound metabolism (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.THIOREDOXIN-REDUCT-NADPH-CPLX|complex.ecocyc.THIOREDOXIN-REDUCT-NADPH-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0888|gene.b0888]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9P4`
- `KEGG:ecj:JW0871;eco:b0888;`
- `GeneID:93776532;949054;`
- `GO:GO:0004791; GO:0005829; GO:0019430; GO:0045454; GO:0050660; GO:1902515`
- `EC:1.8.1.9`

## Notes

Thioredoxin reductase (TRXR) (EC 1.8.1.9)
