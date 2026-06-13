---
entity_id: "reaction.ecocyc.RXN0-704"
entity_type: "reaction"
name: "RXN0-704"
source_database: "EcoCyc"
source_id: "RXN0-704"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-704

`reaction.ecocyc.RXN0-704`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-704`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

3-KETO-L-GULONATE + ATP -> PROTON + CPD-2343 + ADP; direction=LEFT-TO-RIGHT EcoCyc reaction equation: 3-KETO-L-GULONATE + ATP -> PROTON + CPD-2343 + ADP; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by L-xylulose kinase (complex.ecocyc.LYXK-CPLX). Substrates: ATP (molecule.C00002), 3-Dehydro-L-gulonate (molecule.C00618). Products: ADP (molecule.C00008), H+ (molecule.C00080), 3-Dehydro-L-gulonate 6-phosphate (molecule.C14899).

## Enriched Pathways

- `ecocyc.PWY-6961` L-ascorbate degradation II (bacterial, aerobic) (EcoCyc)

## Annotation

3-KETO-L-GULONATE + ATP -> PROTON + CPD-2343 + ADP; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6961` L-ascorbate degradation II (bacterial, aerobic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.LYXK-CPLX|complex.ecocyc.LYXK-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C14899|molecule.C14899]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00618|molecule.C00618]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-704`

## Notes

3-KETO-L-GULONATE + ATP -> PROTON + CPD-2343 + ADP; direction=LEFT-TO-RIGHT
