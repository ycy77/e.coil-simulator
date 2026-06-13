---
entity_id: "reaction.ecocyc.RXN-21523"
entity_type: "reaction"
name: "RXN-21523"
source_database: "EcoCyc"
source_id: "RXN-21523"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21523

`reaction.ecocyc.RXN-21523`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21523`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Hydroxymethylbilane-Synthase-ES2 + PORPHOBILINOGEN -> Hydroxymethylbilane-Synthase-ES3 + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Hydroxymethylbilane-Synthase-ES2 + PORPHOBILINOGEN -> Hydroxymethylbilane-Synthase-ES3 + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Porphobilinogen (molecule.C00931), a [hydroxymethylbilane synthase] ES2 intermediate (molecule.ecocyc.Hydroxymethylbilane-Synthase-ES2). Products: ammonium (molecule.ecocyc.AMMONIUM), a [hydroxymethylbilane synthase] ES3 intermediate (molecule.ecocyc.Hydroxymethylbilane-Synthase-ES3).

## Annotation

Hydroxymethylbilane-Synthase-ES2 + PORPHOBILINOGEN -> Hydroxymethylbilane-Synthase-ES3 + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Hydroxymethylbilane-Synthase-ES3|molecule.ecocyc.Hydroxymethylbilane-Synthase-ES3]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00931|molecule.C00931]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Hydroxymethylbilane-Synthase-ES2|molecule.ecocyc.Hydroxymethylbilane-Synthase-ES2]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-21523`

## Notes

Hydroxymethylbilane-Synthase-ES2 + PORPHOBILINOGEN -> Hydroxymethylbilane-Synthase-ES3 + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT
