---
entity_id: "reaction.ecocyc.RXN0-705"
entity_type: "reaction"
name: "RXN0-705"
source_database: "EcoCyc"
source_id: "RXN0-705"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-705

`reaction.ecocyc.RXN0-705`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-705`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PROTON + CPD-2343 -> L-XYLULOSE-5-P + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + CPD-2343 -> L-XYLULOSE-5-P + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 3-keto-L-gulonate-6-phosphate decarboxylase UlaD (complex.ecocyc.CPLX0-7744), sgbH (protein.P37678). Substrates: H+ (molecule.C00080), 3-Dehydro-L-gulonate 6-phosphate (molecule.C14899). Products: CO2 (molecule.C00011), L-Xylulose 5-phosphate (molecule.C03291).

## Enriched Pathways

- `ecocyc.PWY-6961` L-ascorbate degradation II (bacterial, aerobic) (EcoCyc)
- `ecocyc.PWY0-301` L-ascorbate degradation I (bacterial, anaerobic) (EcoCyc)

## Annotation

PROTON + CPD-2343 -> L-XYLULOSE-5-P + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6961` L-ascorbate degradation II (bacterial, aerobic) (EcoCyc)
- `ecocyc.PWY0-301` L-ascorbate degradation I (bacterial, anaerobic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7744|complex.ecocyc.CPLX0-7744]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P37678|protein.P37678]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03291|molecule.C03291]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C14899|molecule.C14899]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-705`

## Notes

PROTON + CPD-2343 -> L-XYLULOSE-5-P + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT
