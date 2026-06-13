---
entity_id: "reaction.ecocyc.DEPHOSPHOCOAKIN-RXN"
entity_type: "reaction"
name: "DEPHOSPHOCOAKIN-RXN"
source_database: "EcoCyc"
source_id: "DEPHOSPHOCOAKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DEPHOSPHOCOAKIN-RXN

`reaction.ecocyc.DEPHOSPHOCOAKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DEPHOSPHOCOAKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the fifth and final reaction in coenzyme A (CoA) biosynthesis. EcoCyc reaction equation: DEPHOSPHO-COA + ATP -> PROTON + CO-A + ADP; direction=PHYSIOL-LEFT-TO-RIGHT. This is the fifth and final reaction in coenzyme A (CoA) biosynthesis.

## Biological Role

Catalyzed by coaE (protein.P0A6I9). Substrates: ATP (molecule.C00002), Dephospho-CoA (molecule.C00882). Products: ADP (molecule.C00008), CoA (molecule.C00010), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.COA-PWY` coenzyme A biosynthesis I (bacteria) (EcoCyc)

## Annotation

This is the fifth and final reaction in coenzyme A (CoA) biosynthesis.

## Pathways

- `ecocyc.COA-PWY` coenzyme A biosynthesis I (bacteria) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0A6I9|protein.P0A6I9]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00882|molecule.C00882]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:DEPHOSPHOCOAKIN-RXN`

## Notes

DEPHOSPHO-COA + ATP -> PROTON + CO-A + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
