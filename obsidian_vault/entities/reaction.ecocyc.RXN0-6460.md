---
entity_id: "reaction.ecocyc.RXN0-6460"
entity_type: "reaction"
name: "peroxyureidoacrylate/ureidoacrylate amidohydrolase"
source_database: "EcoCyc"
source_id: "RXN0-6460"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# peroxyureidoacrylate/ureidoacrylate amidohydrolase

`reaction.ecocyc.RXN0-6460`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6460`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2331 + WATER -> PROTON + CARBAMATE + CPD0-2339; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-2331 + WATER -> PROTON + CARBAMATE + CPD0-2339; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rutB (protein.P75897). Substrates: H2O (molecule.C00001), Ureidoacrylate (molecule.C20254). Products: H+ (molecule.C00080), Carbamate (molecule.C01563), Aminoacrylate (molecule.C20253).

## Enriched Pathways

- `ecocyc.PWY0-1471` uracil degradation III (EcoCyc)

## Annotation

CPD0-2331 + WATER -> PROTON + CARBAMATE + CPD0-2339; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1471` uracil degradation III (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P75897|protein.P75897]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01563|molecule.C01563]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C20253|molecule.C20253]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C20254|molecule.C20254]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6460`

## Notes

CPD0-2331 + WATER -> PROTON + CARBAMATE + CPD0-2339; direction=PHYSIOL-LEFT-TO-RIGHT
