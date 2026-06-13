---
entity_id: "reaction.ecocyc.RXN0-6726"
entity_type: "reaction"
name: "RXN0-6726"
source_database: "EcoCyc"
source_id: "RXN0-6726"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6726

`reaction.ecocyc.RXN0-6726`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6726`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

alpha-N-Peptidyl-LGlutamate + GLT + ATP -> CPD0-2471 + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: alpha-N-Peptidyl-LGlutamate + GLT + ATP -> CPD0-2471 + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ribosomal protein S6 modification protein (complex.ecocyc.CPLX0-7946). Substrates: ATP (molecule.C00002), L-Glutamate (molecule.C00025), a [protein] C-terminal L-glutamate (molecule.ecocyc.alpha-N-Peptidyl-LGlutamate). Products: ADP (molecule.C00008), H+ (molecule.C00080), a [protein] C-terminal α-L-glutamate-α-L-glutamate (molecule.ecocyc.CPD0-2471), phosphate (molecule.ecocyc.Pi).

## Annotation

alpha-N-Peptidyl-LGlutamate + GLT + ATP -> CPD0-2471 + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7946|complex.ecocyc.CPLX0-7946]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-2471|molecule.ecocyc.CPD0-2471]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.alpha-N-Peptidyl-LGlutamate|molecule.ecocyc.alpha-N-Peptidyl-LGlutamate]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6726`

## Notes

alpha-N-Peptidyl-LGlutamate + GLT + ATP -> CPD0-2471 + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
