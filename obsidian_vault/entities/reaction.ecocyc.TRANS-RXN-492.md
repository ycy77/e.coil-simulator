---
entity_id: "reaction.ecocyc.TRANS-RXN-492"
entity_type: "reaction"
name: "TRANS-RXN-492"
source_database: "EcoCyc"
source_id: "TRANS-RXN-492"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-492

`reaction.ecocyc.TRANS-RXN-492`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-492`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

S-2-AMINOETHYL-L-CYSTEINE + PROTON -> S-2-AMINOETHYL-L-CYSTEINE + PROTON; direction=REVERSIBLE EcoCyc reaction equation: S-2-AMINOETHYL-L-CYSTEINE + PROTON -> S-2-AMINOETHYL-L-CYSTEINE + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by lysO (protein.P75826). Substrates: H+ (molecule.C00080), S-(2-aminoethyl)-L-cysteine (molecule.ecocyc.S-2-AMINOETHYL-L-CYSTEINE). Products: H+ (molecule.C00080), S-(2-aminoethyl)-L-cysteine (molecule.ecocyc.S-2-AMINOETHYL-L-CYSTEINE).

## Annotation

S-2-AMINOETHYL-L-CYSTEINE + PROTON -> S-2-AMINOETHYL-L-CYSTEINE + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P75826|protein.P75826]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.S-2-AMINOETHYL-L-CYSTEINE|molecule.ecocyc.S-2-AMINOETHYL-L-CYSTEINE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.S-2-AMINOETHYL-L-CYSTEINE|molecule.ecocyc.S-2-AMINOETHYL-L-CYSTEINE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-492`

## Notes

S-2-AMINOETHYL-L-CYSTEINE + PROTON -> S-2-AMINOETHYL-L-CYSTEINE + PROTON; direction=REVERSIBLE
