---
entity_id: "reaction.ecocyc.RXN0-262"
entity_type: "reaction"
name: "RXN0-262"
source_database: "EcoCyc"
source_id: "RXN0-262"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-262

`reaction.ecocyc.RXN0-262`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-262`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-15870 + GTP + PROTON -> CPD-582 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-15870 + GTP + PROTON -> CPD-582 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by mobA (protein.P32173). Substrates: GTP (molecule.C00044), H+ (molecule.C00080), Molybdoenzyme molybdenum cofactor (molecule.C18237). Products: Diphosphate (molecule.C00013), Guanylyl molybdenum cofactor (molecule.C19871).

## Enriched Pathways

- `ecocyc.PWY-5964` guanylyl molybdenum cofactor biosynthesis (EcoCyc)

## Annotation

CPD-15870 + GTP + PROTON -> CPD-582 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-5964` guanylyl molybdenum cofactor biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P32173|protein.P32173]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C19871|molecule.C19871]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C18237|molecule.C18237]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-262`

## Notes

CPD-15870 + GTP + PROTON -> CPD-582 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
