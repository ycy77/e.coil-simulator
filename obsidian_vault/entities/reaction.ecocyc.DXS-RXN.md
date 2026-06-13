---
entity_id: "reaction.ecocyc.DXS-RXN"
entity_type: "reaction"
name: "DXS-RXN"
source_database: "EcoCyc"
source_id: "DXS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DXS-RXN

`reaction.ecocyc.DXS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DXS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the first reaction in the mevalonate-independent pathway for isopentenyl diphosphate biosynthesis. The reaction product deoxyxylulose-5-phosphate is also an intermediate in pyridoxal 5'-phosphate biosynthesis. EcoCyc reaction equation: PYRUVATE + GAP + PROTON -> CARBON-DIOXIDE + DEOXYXYLULOSE-5P; direction=LEFT-TO-RIGHT. This is the first reaction in the mevalonate-independent pathway for isopentenyl diphosphate biosynthesis. The reaction product deoxyxylulose-5-phosphate is also an intermediate in pyridoxal 5'-phosphate biosynthesis.

## Biological Role

Catalyzed by 1-deoxy-D-xylulose-5-phosphate synthase (complex.ecocyc.CPLX0-743). Substrates: Pyruvate (molecule.C00022), H+ (molecule.C00080), D-Glyceraldehyde 3-phosphate (molecule.C00118). Products: CO2 (molecule.C00011), 1-Deoxy-D-xylulose 5-phosphate (molecule.C11437).

## Enriched Pathways

- `ecocyc.NONMEVIPP-PWY` methylerythritol phosphate pathway I (EcoCyc)
- `ecocyc.PWY-6892` thiazole component of thiamine diphosphate biosynthesis I (EcoCyc)
- `ecocyc.PYRIDOXSYN-PWY` pyridoxal 5'-phosphate biosynthesis I (EcoCyc)

## Annotation

This is the first reaction in the mevalonate-independent pathway for isopentenyl diphosphate biosynthesis. The reaction product deoxyxylulose-5-phosphate is also an intermediate in pyridoxal 5'-phosphate biosynthesis.

## Pathways

- `ecocyc.NONMEVIPP-PWY` methylerythritol phosphate pathway I (EcoCyc)
- `ecocyc.PWY-6892` thiazole component of thiamine diphosphate biosynthesis I (EcoCyc)
- `ecocyc.PYRIDOXSYN-PWY` pyridoxal 5'-phosphate biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-743|complex.ecocyc.CPLX0-743]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C11437|molecule.C11437]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00118|molecule.C00118]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-1353|molecule.ecocyc.CPD0-1353]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.METHYL-ACETYLPHOSPHONATE|molecule.ecocyc.METHYL-ACETYLPHOSPHONATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:DXS-RXN`

## Notes

PYRUVATE + GAP + PROTON -> CARBON-DIOXIDE + DEOXYXYLULOSE-5P; direction=LEFT-TO-RIGHT
