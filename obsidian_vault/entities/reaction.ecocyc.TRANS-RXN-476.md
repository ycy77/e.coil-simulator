---
entity_id: "reaction.ecocyc.TRANS-RXN-476"
entity_type: "reaction"
name: "ADP-glucose:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-476"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ADP-glucose:proton symport

`reaction.ecocyc.TRANS-RXN-476`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-476`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

ADP-D-GLUCOSE + PROTON -> ADP-D-GLUCOSE + PROTON; direction=REVERSIBLE EcoCyc reaction equation: ADP-D-GLUCOSE + PROTON -> ADP-D-GLUCOSE + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by nupC (protein.P0AFF2), nupG (protein.P0AFF4). Substrates: H+ (molecule.C00080), ADP-glucose (molecule.C00498). Products: H+ (molecule.C00080), ADP-glucose (molecule.C00498).

## Annotation

ADP-D-GLUCOSE + PROTON -> ADP-D-GLUCOSE + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AFF2|protein.P0AFF2]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AFF4|protein.P0AFF4]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00498|molecule.C00498]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00498|molecule.C00498]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-476`

## Notes

ADP-D-GLUCOSE + PROTON -> ADP-D-GLUCOSE + PROTON; direction=REVERSIBLE
