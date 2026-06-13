---
entity_id: "reaction.ecocyc.RXN0-5214"
entity_type: "reaction"
name: "RXN0-5214"
source_database: "EcoCyc"
source_id: "RXN0-5214"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5214

`reaction.ecocyc.RXN0-5214`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5214`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-ASCORBATE-6-PHOSPHATE + WATER -> CPD-2343; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: L-ASCORBATE-6-PHOSPHATE + WATER -> CPD-2343; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by L-ascorbate-6-phosphate lactonase (complex.ecocyc.CPLX0-7848). Substrates: H2O (molecule.C00001), L-Ascorbate 6-phosphate (molecule.C16186). Products: 3-Dehydro-L-gulonate 6-phosphate (molecule.C14899).

## Enriched Pathways

- `ecocyc.PWY0-301` L-ascorbate degradation I (bacterial, anaerobic) (EcoCyc)

## Annotation

L-ASCORBATE-6-PHOSPHATE + WATER -> CPD-2343; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-301` L-ascorbate degradation I (bacterial, anaerobic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7848|complex.ecocyc.CPLX0-7848]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C14899|molecule.C14899]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C16186|molecule.C16186]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5214`

## Notes

L-ASCORBATE-6-PHOSPHATE + WATER -> CPD-2343; direction=PHYSIOL-LEFT-TO-RIGHT
