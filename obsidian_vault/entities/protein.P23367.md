---
entity_id: "protein.P23367"
entity_type: "protein"
name: "mutL"
source_database: "UniProt"
source_id: "P23367"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mutL b4170 JW4128"
---

# mutL

`protein.P23367`

## Static

- Type: `protein`
- Source: `UniProt:P23367`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: This protein is involved in the repair of mismatches in DNA. It is required for dam-dependent methyl-directed DNA mismatch repair. May act as a 'molecular matchmaker', a protein that promotes the formation of a stable complex between two or more DNA-binding proteins in an ATP-dependent manner without itself being part of the final effector complex. The ATPase activity of MutL is stimulated by DNA.

## Biological Role

Component of methyl-directed mismatch repair system (complex.ecocyc.MUTHLS-CPLX).

## Enriched Pathways

- `eco03430` Mismatch repair (KEGG)

## Annotation

FUNCTION: This protein is involved in the repair of mismatches in DNA. It is required for dam-dependent methyl-directed DNA mismatch repair. May act as a 'molecular matchmaker', a protein that promotes the formation of a stable complex between two or more DNA-binding proteins in an ATP-dependent manner without itself being part of the final effector complex. The ATPase activity of MutL is stimulated by DNA.

## Pathways

- `eco03430` Mismatch repair (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.MUTHLS-CPLX|complex.ecocyc.MUTHLS-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4170|gene.b4170]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P23367`
- `KEGG:ecj:JW4128;eco:b4170;ecoc:C3026_22535;`
- `GeneID:948691;`
- `GO:GO:0000018; GO:0003677; GO:0005524; GO:0006298; GO:0016887; GO:0017117; GO:0030983; GO:0032300; GO:0042802; GO:0070716; GO:0140664`

## Notes

DNA mismatch repair protein MutL
