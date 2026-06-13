---
entity_id: "reaction.ecocyc.RXN-15607"
entity_type: "reaction"
name: "RXN-15607"
source_database: "EcoCyc"
source_id: "RXN-15607"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-15607

`reaction.ecocyc.RXN-15607`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15607`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

11-DEOXYCORTICOSTERONE + NADH + PROTON -> CPD-16843 + NAD; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 11-DEOXYCORTICOSTERONE + NADH + PROTON -> CPD-16843 + NAD; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by kduD (protein.P37769). Substrates: NADH (molecule.C00004), H+ (molecule.C00080), 11-deoxycorticosterone (molecule.ecocyc.11-DEOXYCORTICOSTERONE). Products: NAD+ (molecule.C00003), 4-pregnen-20,21-diol-3-one (molecule.ecocyc.CPD-16843).

## Annotation

11-DEOXYCORTICOSTERONE + NADH + PROTON -> CPD-16843 + NAD; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P37769|protein.P37769]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-16843|molecule.ecocyc.CPD-16843]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.11-DEOXYCORTICOSTERONE|molecule.ecocyc.11-DEOXYCORTICOSTERONE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-15607`

## Notes

11-DEOXYCORTICOSTERONE + NADH + PROTON -> CPD-16843 + NAD; direction=PHYSIOL-LEFT-TO-RIGHT
