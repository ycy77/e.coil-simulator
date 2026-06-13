---
entity_id: "protein.P23909"
entity_type: "protein"
name: "mutS"
source_database: "UniProt"
source_id: "P23909"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mutS fdv b2733 JW2703"
---

# mutS

`protein.P23909`

## Static

- Type: `protein`
- Source: `UniProt:P23909`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: This protein is involved in the repair of mismatches in DNA. It is possible that it carries out the mismatch recognition step. This protein has a weak ATPase activity. Purified MutS binds to DNA regions containing a mismatched base pair .

## Biological Role

Component of methyl-directed mismatch repair system (complex.ecocyc.MUTHLS-CPLX).

## Enriched Pathways

- `eco03430` Mismatch repair (KEGG)

## Annotation

FUNCTION: This protein is involved in the repair of mismatches in DNA. It is possible that it carries out the mismatch recognition step. This protein has a weak ATPase activity.

## Pathways

- `eco03430` Mismatch repair (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.MUTHLS-CPLX|complex.ecocyc.MUTHLS-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2733|gene.b2733]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P23909`
- `KEGG:ecj:JW2703;eco:b2733;ecoc:C3026_15035;`
- `GeneID:947206;`
- `GO:GO:0000018; GO:0003684; GO:0005524; GO:0005829; GO:0006298; GO:0006974; GO:0008301; GO:0016887; GO:0030983; GO:0032136; GO:0032300; GO:0042802; GO:0043531; GO:0140664; GO:1990710`

## Notes

DNA mismatch repair protein MutS
