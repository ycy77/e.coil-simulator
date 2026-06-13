---
entity_id: "reaction.ecocyc.FERREDOXIN--NAD_-REDUCTASE-RXN"
entity_type: "reaction"
name: "FERREDOXIN--NAD+-REDUCTASE-RXN"
source_database: "EcoCyc"
source_id: "FERREDOXIN--NAD+-REDUCTASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# FERREDOXIN--NAD+-REDUCTASE-RXN

`reaction.ecocyc.FERREDOXIN--NAD_-REDUCTASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:FERREDOXIN--NAD+-REDUCTASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Reduced-2Fe-2S-Ferredoxins + NAD + PROTON -> Oxidized-2Fe-2S-Ferredoxins + NADH; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: Reduced-2Fe-2S-Ferredoxins + NAD + PROTON -> Oxidized-2Fe-2S-Ferredoxins + NADH; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Substrates: NAD+ (molecule.C00003), H+ (molecule.C00080). Products: NADH (molecule.C00004).

## Annotation

Reduced-2Fe-2S-Ferredoxins + NAD + PROTON -> Oxidized-2Fe-2S-Ferredoxins + NADH; direction=PHYSIOL-RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:FERREDOXIN--NAD+-REDUCTASE-RXN`

## Notes

Reduced-2Fe-2S-Ferredoxins + NAD + PROTON -> Oxidized-2Fe-2S-Ferredoxins + NADH; direction=PHYSIOL-RIGHT-TO-LEFT
