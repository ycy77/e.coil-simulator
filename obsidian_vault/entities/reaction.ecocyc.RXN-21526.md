---
entity_id: "reaction.ecocyc.RXN-21526"
entity_type: "reaction"
name: "RXN-21526"
source_database: "EcoCyc"
source_id: "RXN-21526"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21526

`reaction.ecocyc.RXN-21526`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21526`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Holo-Hydroxymethylbilane-Synthase + PORPHOBILINOGEN -> Hydroxymethylbilane-Synthase-ES + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Holo-Hydroxymethylbilane-Synthase + PORPHOBILINOGEN -> Hydroxymethylbilane-Synthase-ES + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Porphobilinogen (molecule.C00931), a holo-[hydroxymethylbilane synthase] (molecule.ecocyc.Holo-Hydroxymethylbilane-Synthase). Products: ammonium (molecule.ecocyc.AMMONIUM), a holo [hydroxymethylbilane synthase] ES intermediate (molecule.ecocyc.Hydroxymethylbilane-Synthase-ES).

## Annotation

Holo-Hydroxymethylbilane-Synthase + PORPHOBILINOGEN -> Hydroxymethylbilane-Synthase-ES + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Hydroxymethylbilane-Synthase-ES|molecule.ecocyc.Hydroxymethylbilane-Synthase-ES]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00931|molecule.C00931]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Holo-Hydroxymethylbilane-Synthase|molecule.ecocyc.Holo-Hydroxymethylbilane-Synthase]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-21526`

## Notes

Holo-Hydroxymethylbilane-Synthase + PORPHOBILINOGEN -> Hydroxymethylbilane-Synthase-ES + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT
