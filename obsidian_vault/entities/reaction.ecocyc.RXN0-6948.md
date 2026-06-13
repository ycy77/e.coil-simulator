---
entity_id: "reaction.ecocyc.RXN0-6948"
entity_type: "reaction"
name: "RXN0-6948"
source_database: "EcoCyc"
source_id: "RXN0-6948"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6948

`reaction.ecocyc.RXN0-6948`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6948`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

MET + ACETYL-COA -> CPD0-2015 + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: MET + ACETYL-COA -> CPD0-2015 + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by L-amino acid N-acyltransferase (complex.ecocyc.CPLX0-7962). Substrates: Acetyl-CoA (molecule.C00024), L-Methionine (molecule.C00073). Products: CoA (molecule.C00010), H+ (molecule.C00080), N-acetyl-L-methionine (molecule.ecocyc.CPD0-2015).

## Annotation

MET + ACETYL-COA -> CPD0-2015 + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7962|complex.ecocyc.CPLX0-7962]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-2015|molecule.ecocyc.CPD0-2015]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00073|molecule.C00073]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6948`

## Notes

MET + ACETYL-COA -> CPD0-2015 + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
