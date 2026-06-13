---
entity_id: "reaction.ecocyc.RXN0-5295"
entity_type: "reaction"
name: "RXN0-5295"
source_database: "EcoCyc"
source_id: "RXN0-5295"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5295

`reaction.ecocyc.RXN0-5295`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5295`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-1162 + WATER -> GLC-6-P + HYDROQUINONE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-1162 + WATER -> GLC-6-P + HYDROQUINONE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by bglB (protein.P11988), ascB (protein.P24240), bglA (protein.Q46829). Substrates: H2O (molecule.C00001), Arbutin 6-phosphate (molecule.C06187). Products: Hydroquinone (molecule.C00530), beta-D-Glucose 6-phosphate (molecule.C01172).

## Annotation

CPD-1162 + WATER -> GLC-6-P + HYDROQUINONE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P11988|protein.P11988]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P24240|protein.P24240]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.Q46829|protein.Q46829]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00530|molecule.C00530]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01172|molecule.C01172]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C06187|molecule.C06187]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5295`

## Notes

CPD-1162 + WATER -> GLC-6-P + HYDROQUINONE; direction=PHYSIOL-LEFT-TO-RIGHT
