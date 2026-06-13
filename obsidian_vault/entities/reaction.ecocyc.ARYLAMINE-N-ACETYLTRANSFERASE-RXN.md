---
entity_id: "reaction.ecocyc.ARYLAMINE-N-ACETYLTRANSFERASE-RXN"
entity_type: "reaction"
name: "ARYLAMINE-N-ACETYLTRANSFERASE-RXN"
source_database: "EcoCyc"
source_id: "ARYLAMINE-N-ACETYLTRANSFERASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ARYLAMINE-N-ACETYLTRANSFERASE-RXN

`reaction.ecocyc.ARYLAMINE-N-ACETYLTRANSFERASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ARYLAMINE-N-ACETYLTRANSFERASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Aryl-Amines + ACETYL-COA -> N-acetylarylamines + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Aryl-Amines + ACETYL-COA -> N-acetylarylamines + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by arylamine N-acetyltransferase (complex.ecocyc.CPLX0-236). Substrates: Acetyl-CoA (molecule.C00024), an arylamine (molecule.ecocyc.Aryl-Amines). Products: CoA (molecule.C00010), an N-acetylarylamine (molecule.ecocyc.N-acetylarylamines).

## Annotation

Aryl-Amines + ACETYL-COA -> N-acetylarylamines + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-236|complex.ecocyc.CPLX0-236]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.N-acetylarylamines|molecule.ecocyc.N-acetylarylamines]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Aryl-Amines|molecule.ecocyc.Aryl-Amines]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00805|molecule.C00805]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.N-ETHYLMALEIMIDE|molecule.ecocyc.N-ETHYLMALEIMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ARYLAMINE-N-ACETYLTRANSFERASE-RXN`

## Notes

Aryl-Amines + ACETYL-COA -> N-acetylarylamines + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT
