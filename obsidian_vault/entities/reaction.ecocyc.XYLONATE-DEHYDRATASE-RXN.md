---
entity_id: "reaction.ecocyc.XYLONATE-DEHYDRATASE-RXN"
entity_type: "reaction"
name: "XYLONATE-DEHYDRATASE-RXN"
source_database: "EcoCyc"
source_id: "XYLONATE-DEHYDRATASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# XYLONATE-DEHYDRATASE-RXN

`reaction.ecocyc.XYLONATE-DEHYDRATASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:XYLONATE-DEHYDRATASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-XYLONATE -> WATER + 2-DH-3-DO-D-ARABINONATE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: D-XYLONATE -> WATER + 2-DH-3-DO-D-ARABINONATE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by yjhG (protein.P39358), yagF (protein.P77596). Substrates: D-Xylonate (molecule.C00502). Products: H2O (molecule.C00001), 2-Dehydro-3-deoxy-D-xylonate (molecule.C03826).

## Enriched Pathways

- `ecocyc.PWY-6760` D-xylose degradation III (EcoCyc)
- `ecocyc.PWY-7294` D-xylose degradation IV (EcoCyc)

## Annotation

D-XYLONATE -> WATER + 2-DH-3-DO-D-ARABINONATE; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6760` D-xylose degradation III (EcoCyc)
- `ecocyc.PWY-7294` D-xylose degradation IV (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `activates` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P39358|protein.P39358]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P77596|protein.P77596]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03826|molecule.C03826]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00502|molecule.C00502]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:XYLONATE-DEHYDRATASE-RXN`

## Notes

D-XYLONATE -> WATER + 2-DH-3-DO-D-ARABINONATE; direction=LEFT-TO-RIGHT
