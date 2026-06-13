---
entity_id: "reaction.ecocyc.XYLULOKIN-RXN"
entity_type: "reaction"
name: "XYLULOKIN-RXN"
source_database: "EcoCyc"
source_id: "XYLULOKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# XYLULOKIN-RXN

`reaction.ecocyc.XYLULOKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:XYLULOKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Catabolism of xylose. EcoCyc reaction equation: D-XYLULOSE + ATP -> PROTON + XYLULOSE-5-PHOSPHATE + ADP; direction=LEFT-TO-RIGHT. Catabolism of xylose.

## Biological Role

Catalyzed by xylulokinase (complex.ecocyc.CPLX0-7466). Substrates: ATP (molecule.C00002), D-Xylulose (molecule.C00310). Products: ADP (molecule.C00008), H+ (molecule.C00080), D-Xylulose 5-phosphate (molecule.C00231).

## Enriched Pathways

- `ecocyc.DARABITOLUTIL-PWY` D-arabinitol degradation I (EcoCyc)
- `ecocyc.LARABITOLUTIL-PWY` xylitol degradation I (EcoCyc)
- `ecocyc.XYLCAT-PWY` D-xylose degradation I (EcoCyc)

## Annotation

Catabolism of xylose.

## Pathways

- `ecocyc.DARABITOLUTIL-PWY` D-arabinitol degradation I (EcoCyc)
- `ecocyc.LARABITOLUTIL-PWY` xylitol degradation I (EcoCyc)
- `ecocyc.XYLCAT-PWY` D-xylose degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7466|complex.ecocyc.CPLX0-7466]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00231|molecule.C00231]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00310|molecule.C00310]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-1054|molecule.ecocyc.CPD0-1054]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1316|molecule.ecocyc.CPD0-1316]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:XYLULOKIN-RXN`

## Notes

D-XYLULOSE + ATP -> PROTON + XYLULOSE-5-PHOSPHATE + ADP; direction=LEFT-TO-RIGHT
