---
entity_id: "reaction.ecocyc.TRANS-RXN-415"
entity_type: "reaction"
name: "2,7-anhydro-N-acetylneuraminate:H+ symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-415"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 2,7-anhydro-N-acetylneuraminate:H+ symport

`reaction.ecocyc.TRANS-RXN-415`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-415`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD-6182 + PROTON -> CPD-6182 + PROTON; direction=REVERSIBLE EcoCyc reaction equation: CPD-6182 + PROTON -> CPD-6182 + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by nanX (protein.P39352). Substrates: H+ (molecule.C00080), 2,7-anhydro-α-N-acetylneuraminate (molecule.ecocyc.CPD-6182). Products: H+ (molecule.C00080), 2,7-anhydro-α-N-acetylneuraminate (molecule.ecocyc.CPD-6182).

## Annotation

CPD-6182 + PROTON -> CPD-6182 + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P39352|protein.P39352]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-6182|molecule.ecocyc.CPD-6182]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-6182|molecule.ecocyc.CPD-6182]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-415`

## Notes

CPD-6182 + PROTON -> CPD-6182 + PROTON; direction=REVERSIBLE
