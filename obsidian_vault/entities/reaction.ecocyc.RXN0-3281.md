---
entity_id: "reaction.ecocyc.RXN0-3281"
entity_type: "reaction"
name: "RXN0-3281"
source_database: "EcoCyc"
source_id: "RXN0-3281"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-3281

`reaction.ecocyc.RXN0-3281`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-3281`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

FORMATE + Oxidized-ferredoxins -> CARBON-DIOXIDE + PROTON + Reduced-ferredoxins; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: FORMATE + Oxidized-ferredoxins -> CARBON-DIOXIDE + PROTON + Reduced-ferredoxins; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by fdhF (protein.P07658). Substrates: Formate (molecule.C00058). Products: CO2 (molecule.C00011), H+ (molecule.C00080).

## Annotation

FORMATE + Oxidized-ferredoxins -> CARBON-DIOXIDE + PROTON + Reduced-ferredoxins; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `catalyzes` <-- [[protein.P07658|protein.P07658]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00058|molecule.C00058]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00088|molecule.C00088]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00244|molecule.C00244]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01417|molecule.C01417]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CL-|molecule.ecocyc.CL-]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-2841|molecule.ecocyc.CPD-2841]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.HSCN|molecule.ecocyc.HSCN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-3281`

## Notes

FORMATE + Oxidized-ferredoxins -> CARBON-DIOXIDE + PROTON + Reduced-ferredoxins; direction=PHYSIOL-LEFT-TO-RIGHT
