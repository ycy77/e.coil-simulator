---
entity_id: "reaction.ecocyc.D-ARABINITOL-4-DEHYDROGENASE-RXN"
entity_type: "reaction"
name: "D-ARABINITOL-4-DEHYDROGENASE-RXN"
source_database: "EcoCyc"
source_id: "D-ARABINITOL-4-DEHYDROGENASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# D-ARABINITOL-4-DEHYDROGENASE-RXN

`reaction.ecocyc.D-ARABINITOL-4-DEHYDROGENASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:D-ARABINITOL-4-DEHYDROGENASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-355 + NAD -> D-XYLULOSE + NADH + PROTON; direction=REVERSIBLE EcoCyc reaction equation: CPD-355 + NAD -> D-XYLULOSE + NADH + PROTON; direction=REVERSIBLE.

## Biological Role

Substrates: NAD+ (molecule.C00003), D-Arabitol (molecule.C01904). Products: NADH (molecule.C00004), H+ (molecule.C00080), D-Xylulose (molecule.C00310).

## Enriched Pathways

- `ecocyc.DARABITOLUTIL-PWY` D-arabinitol degradation I (EcoCyc)

## Annotation

CPD-355 + NAD -> D-XYLULOSE + NADH + PROTON; direction=REVERSIBLE

## Pathways

- `ecocyc.DARABITOLUTIL-PWY` D-arabinitol degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00310|molecule.C00310]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01904|molecule.C01904]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:D-ARABINITOL-4-DEHYDROGENASE-RXN`

## Notes

CPD-355 + NAD -> D-XYLULOSE + NADH + PROTON; direction=REVERSIBLE
