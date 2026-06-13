---
entity_id: "reaction.ecocyc.GKI-RXN"
entity_type: "reaction"
name: "GKI-RXN"
source_database: "EcoCyc"
source_id: "GKI-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GKI-RXN

`reaction.ecocyc.GKI-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GKI-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + GLYCERATE -> PROTON + 2-PG + ADP; direction=LEFT-TO-RIGHT EcoCyc reaction equation: ATP + GLYCERATE -> PROTON + 2-PG + ADP; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by garK (protein.P23524), glxK (protein.P77364). Substrates: ATP (molecule.C00002), D-Glycerate (molecule.C00258). Products: ADP (molecule.C00008), H+ (molecule.C00080), 2-Phospho-D-glycerate (molecule.C00631).

## Enriched Pathways

- `ecocyc.GALACTARDEG-PWY` D-galactarate degradation I (EcoCyc)
- `ecocyc.GLUCARDEG-PWY` D-glucarate degradation I (EcoCyc)
- `ecocyc.GLYCOLATEMET-PWY` glycolate and glyoxylate degradation I (EcoCyc)
- `ecocyc.PWY0-1300` 2-O-α-mannosyl-D-glycerate degradation (EcoCyc)

## Annotation

ATP + GLYCERATE -> PROTON + 2-PG + ADP; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.GALACTARDEG-PWY` D-galactarate degradation I (EcoCyc)
- `ecocyc.GLUCARDEG-PWY` D-glucarate degradation I (EcoCyc)
- `ecocyc.GLYCOLATEMET-PWY` glycolate and glyoxylate degradation I (EcoCyc)
- `ecocyc.PWY0-1300` 2-O-α-mannosyl-D-glycerate degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P23524|protein.P23524]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P77364|protein.P77364]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00631|molecule.C00631]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00258|molecule.C00258]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:GKI-RXN`

## Notes

ATP + GLYCERATE -> PROTON + 2-PG + ADP; direction=LEFT-TO-RIGHT
