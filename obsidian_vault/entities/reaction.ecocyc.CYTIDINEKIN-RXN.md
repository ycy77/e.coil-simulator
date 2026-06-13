---
entity_id: "reaction.ecocyc.CYTIDINEKIN-RXN"
entity_type: "reaction"
name: "CYTIDINEKIN-RXN"
source_database: "EcoCyc"
source_id: "CYTIDINEKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# CYTIDINEKIN-RXN

`reaction.ecocyc.CYTIDINEKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:CYTIDINEKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Part of pyrimidine nucleotide metabolism, a salvage reaction. EcoCyc reaction equation: CYTIDINE + GTP -> PROTON + CMP + GDP; direction=PHYSIOL-LEFT-TO-RIGHT. Part of pyrimidine nucleotide metabolism, a salvage reaction.

## Biological Role

Catalyzed by udk (protein.P0A8F4). Substrates: GTP (molecule.C00044), Cytidine (molecule.C00475). Products: GDP (molecule.C00035), CMP (molecule.C00055), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.PWY0-163` salvage pathways of pyrimidine ribonucleotides (EcoCyc)

## Annotation

Part of pyrimidine nucleotide metabolism, a salvage reaction.

## Pathways

- `ecocyc.PWY0-163` salvage pathways of pyrimidine ribonucleotides (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (12)

- `catalyzes` <-- [[protein.P0A8F4|protein.P0A8F4]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00035|molecule.C00035]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00055|molecule.C00055]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00475|molecule.C00475]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00063|molecule.C00063]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00075|molecule.C00075]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1319|molecule.ecocyc.CPD0-1319]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1320|molecule.ecocyc.CPD0-1320]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1321|molecule.ecocyc.CPD0-1321]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1322|molecule.ecocyc.CPD0-1322]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:CYTIDINEKIN-RXN`

## Notes

CYTIDINE + GTP -> PROTON + CMP + GDP; direction=PHYSIOL-LEFT-TO-RIGHT
