---
entity_id: "reaction.ecocyc.TRANS-RXN-286"
entity_type: "reaction"
name: "homocystine:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-286"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# homocystine:proton symport

`reaction.ecocyc.TRANS-RXN-286`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-286`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

HOMOCYSTINE + PROTON -> HOMOCYSTINE + PROTON; direction=REVERSIBLE EcoCyc reaction equation: HOMOCYSTINE + PROTON -> HOMOCYSTINE + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by tcyP (protein.P77529). Substrates: H+ (molecule.C00080), L-Homocystine (molecule.C01817). Products: H+ (molecule.C00080), L-Homocystine (molecule.C01817).

## Annotation

HOMOCYSTINE + PROTON -> HOMOCYSTINE + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P77529|protein.P77529]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01817|molecule.C01817]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01817|molecule.C01817]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-286`

## Notes

HOMOCYSTINE + PROTON -> HOMOCYSTINE + PROTON; direction=REVERSIBLE
