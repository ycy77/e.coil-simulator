---
entity_id: "reaction.ecocyc.RXN-21601"
entity_type: "reaction"
name: "RXN-21601"
source_database: "EcoCyc"
source_id: "RXN-21601"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21601

`reaction.ecocyc.RXN-21601`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21601`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-15870 + CPD-4 + GTP + PROTON -> CPD-15873 + PPI + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-15870 + CPD-4 + GTP + PROTON -> CPD-15873 + PPI + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by mobA (protein.P32173). Substrates: GTP (molecule.C00044), H+ (molecule.C00080), Molybdopterin (molecule.C05924), Molybdoenzyme molybdenum cofactor (molecule.C18237). Products: H2O (molecule.C00001), Diphosphate (molecule.C00013), bis(guanylyl molybdopterin) cofactor (molecule.ecocyc.CPD-15873).

## Annotation

CPD-15870 + CPD-4 + GTP + PROTON -> CPD-15873 + PPI + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P32173|protein.P32173]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-15873|molecule.ecocyc.CPD-15873]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05924|molecule.C05924]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C18237|molecule.C18237]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-21601`

## Notes

CPD-15870 + CPD-4 + GTP + PROTON -> CPD-15873 + PPI + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
