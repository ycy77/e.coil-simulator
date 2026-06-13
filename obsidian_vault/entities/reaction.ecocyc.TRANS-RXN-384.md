---
entity_id: "reaction.ecocyc.TRANS-RXN-384"
entity_type: "reaction"
name: "5-aminopentanaote:H+ symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-384"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 5-aminopentanaote:H+ symport

`reaction.ecocyc.TRANS-RXN-384`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-384`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

5-AMINOPENTANOATE + PROTON -> 5-AMINOPENTANOATE + PROTON; direction=REVERSIBLE EcoCyc reaction equation: 5-AMINOPENTANOATE + PROTON -> 5-AMINOPENTANOATE + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by gabP (protein.P25527). Substrates: H+ (molecule.C00080), 5-Aminopentanoate (molecule.C00431). Products: H+ (molecule.C00080), 5-Aminopentanoate (molecule.C00431).

## Annotation

5-AMINOPENTANOATE + PROTON -> 5-AMINOPENTANOATE + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P25527|protein.P25527]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00431|molecule.C00431]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00431|molecule.C00431]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-384`

## Notes

5-AMINOPENTANOATE + PROTON -> 5-AMINOPENTANOATE + PROTON; direction=REVERSIBLE
