---
entity_id: "reaction.ecocyc.RXN-21524"
entity_type: "reaction"
name: "RXN-21524"
source_database: "EcoCyc"
source_id: "RXN-21524"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21524

`reaction.ecocyc.RXN-21524`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21524`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Hydroxymethylbilane-Synthase-ES3 + PORPHOBILINOGEN -> Hydroxymethylbilane-Synthase-ES4 + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Hydroxymethylbilane-Synthase-ES3 + PORPHOBILINOGEN -> Hydroxymethylbilane-Synthase-ES4 + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Porphobilinogen (molecule.C00931), a [hydroxymethylbilane synthase] ES3 intermediate (molecule.ecocyc.Hydroxymethylbilane-Synthase-ES3). Products: ammonium (molecule.ecocyc.AMMONIUM), a [hydroxymethylbilane synthase] ES4 intermediate (molecule.ecocyc.Hydroxymethylbilane-Synthase-ES4).

## Annotation

Hydroxymethylbilane-Synthase-ES3 + PORPHOBILINOGEN -> Hydroxymethylbilane-Synthase-ES4 + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Hydroxymethylbilane-Synthase-ES4|molecule.ecocyc.Hydroxymethylbilane-Synthase-ES4]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00931|molecule.C00931]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Hydroxymethylbilane-Synthase-ES3|molecule.ecocyc.Hydroxymethylbilane-Synthase-ES3]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-21524`

## Notes

Hydroxymethylbilane-Synthase-ES3 + PORPHOBILINOGEN -> Hydroxymethylbilane-Synthase-ES4 + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT
