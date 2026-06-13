---
entity_id: "reaction.ecocyc.RXN0-2161"
entity_type: "reaction"
name: "RXN0-2161"
source_database: "EcoCyc"
source_id: "RXN0-2161"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-2161

`reaction.ecocyc.RXN0-2161`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-2161`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

tRNA-Sec + SER + ATP -> L-seryl-SEC-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: tRNA-Sec + SER + ATP -> L-seryl-SEC-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by serine—tRNA ligase (complex.ecocyc.SERS-CPLX). Substrates: ATP (molecule.C00002), L-Serine (molecule.C00065). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020).

## Enriched Pathways

- `ecocyc.PWY0-901` L-selenocysteine biosynthesis I (bacteria) (EcoCyc)

## Annotation

tRNA-Sec + SER + ATP -> L-seryl-SEC-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-901` L-selenocysteine biosynthesis I (bacteria) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.SERS-CPLX|complex.ecocyc.SERS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00065|molecule.C00065]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-2161`

## Notes

tRNA-Sec + SER + ATP -> L-seryl-SEC-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
