---
entity_id: "reaction.ecocyc.GLUTKIN-RXN"
entity_type: "reaction"
name: "GLUTKIN-RXN"
source_database: "EcoCyc"
source_id: "GLUTKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLUTKIN-RXN

`reaction.ecocyc.GLUTKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLUTKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the first step in the proline biosynthesis pathway. EcoCyc reaction equation: GLT + ATP -> L-GLUTAMATE-5-P + ADP; direction=LEFT-TO-RIGHT. This is the first step in the proline biosynthesis pathway.

## Biological Role

Catalyzed by glutamate 5-kinase (complex.ecocyc.GLUTKIN-CPLX). Substrates: ATP (molecule.C00002), L-Glutamate (molecule.C00025). Products: ADP (molecule.C00008), L-Glutamyl 5-phosphate (molecule.C03287).

## Enriched Pathways

- `ecocyc.PROSYN-PWY` L-proline biosynthesis I (from L-glutamate) (EcoCyc)

## Annotation

This is the first step in the proline biosynthesis pathway.

## Pathways

- `ecocyc.PROSYN-PWY` L-proline biosynthesis I (from L-glutamate) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.GLUTKIN-CPLX|complex.ecocyc.GLUTKIN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03287|molecule.C03287]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00148|molecule.C00148]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GLUTKIN-RXN`

## Notes

GLT + ATP -> L-GLUTAMATE-5-P + ADP; direction=LEFT-TO-RIGHT
