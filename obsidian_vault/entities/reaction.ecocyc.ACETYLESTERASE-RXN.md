---
entity_id: "reaction.ecocyc.ACETYLESTERASE-RXN"
entity_type: "reaction"
name: "ACETYLESTERASE-RXN"
source_database: "EcoCyc"
source_id: "ACETYLESTERASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ACETYLESTERASE-RXN

`reaction.ecocyc.ACETYLESTERASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ACETYLESTERASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

WATER + Acetate-esters -> Alcohols + ACET + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: WATER + Acetate-esters -> Alcohols + ACET + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by acetylesterase (complex.ecocyc.CPLX0-8033). Substrates: H2O (molecule.C00001), an acetyl ester (molecule.ecocyc.Acetate-esters). Products: Acetate (molecule.C00033), H+ (molecule.C00080), an alcohol (molecule.ecocyc.Alcohols).

## Annotation

WATER + Acetate-esters -> Alcohols + ACET + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8033|complex.ecocyc.CPLX0-8033]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00033|molecule.C00033]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Alcohols|molecule.ecocyc.Alcohols]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Acetate-esters|molecule.ecocyc.Acetate-esters]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ACETYLESTERASE-RXN`

## Notes

WATER + Acetate-esters -> Alcohols + ACET + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
