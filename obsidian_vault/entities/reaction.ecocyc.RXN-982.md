---
entity_id: "reaction.ecocyc.RXN-982"
entity_type: "reaction"
name: "RXN-982"
source_database: "EcoCyc"
source_id: "RXN-982"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-982

`reaction.ecocyc.RXN-982`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-982`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ARSENATE + GLUTATHIONE + Red-Glutaredoxins + PROTON -> CPD0-2040 + Grx-GSH-dithiol + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ARSENATE + GLUTATHIONE + Red-Glutaredoxins + PROTON -> CPD0-2040 + Grx-GSH-dithiol + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by arsC (protein.P0AB96). Substrates: Glutathione (molecule.C00051), H+ (molecule.C00080), arsenate (molecule.ecocyc.ARSENATE). Products: H2O (molecule.C00001), arsenous acid (molecule.ecocyc.CPD0-2040).

## Enriched Pathways

- `ecocyc.PWY-4621-1` arsenic detoxification VI (E. coli) (EcoCyc)

## Annotation

ARSENATE + GLUTATHIONE + Red-Glutaredoxins + PROTON -> CPD0-2040 + Grx-GSH-dithiol + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-4621-1` arsenic detoxification VI (E. coli) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AB96|protein.P0AB96]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-2040|molecule.ecocyc.CPD0-2040]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00051|molecule.C00051]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.ARSENATE|molecule.ecocyc.ARSENATE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-982`

## Notes

ARSENATE + GLUTATHIONE + Red-Glutaredoxins + PROTON -> CPD0-2040 + Grx-GSH-dithiol + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
