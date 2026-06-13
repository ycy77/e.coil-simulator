---
entity_id: "reaction.ecocyc.RXN0-5413"
entity_type: "reaction"
name: "RXN0-5413"
source_database: "EcoCyc"
source_id: "RXN0-5413"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5413

`reaction.ecocyc.RXN0-5413`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5413`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

UDP-N-ACETYL-D-GLUCOSAMINE + N-acetyl-D-glucosamine -> CPD0-1192 + UDP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: UDP-N-ACETYL-D-GLUCOSAMINE + N-acetyl-D-glucosamine -> CPD0-1192 + UDP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by poly-N-acetyl-D-glucosamine synthase (complex.ecocyc.CPLX0-7994). Substrates: UDP-N-acetyl-alpha-D-glucosamine (molecule.C00043), N-Acetyl-D-glucosamine (molecule.C00140). Products: UDP (molecule.C00015), poly-β-1,6-N-acetyl-D-glucosamine (molecule.ecocyc.CPD0-1192).

## Enriched Pathways

- `ecocyc.PWY0-1609` poly-β-1,6-N-acetyl-D-glucosamine biosynthesis (EcoCyc)

## Annotation

UDP-N-ACETYL-D-GLUCOSAMINE + N-acetyl-D-glucosamine -> CPD0-1192 + UDP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1609` poly-β-1,6-N-acetyl-D-glucosamine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `activates` <-- [[molecule.C16463|molecule.C16463]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7994|complex.ecocyc.CPLX0-7994]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00015|molecule.C00015]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-1192|molecule.ecocyc.CPD0-1192]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00043|molecule.C00043]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00140|molecule.C00140]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5413`

## Notes

UDP-N-ACETYL-D-GLUCOSAMINE + N-acetyl-D-glucosamine -> CPD0-1192 + UDP; direction=PHYSIOL-LEFT-TO-RIGHT
