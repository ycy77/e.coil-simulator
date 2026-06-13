---
entity_id: "reaction.ecocyc.TRANS-RXN-261"
entity_type: "reaction"
name: "L-glutamate:4-aminobutanoate antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-261"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# L-glutamate:4-aminobutanoate antiport

`reaction.ecocyc.TRANS-RXN-261`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-261`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

4-AMINO-BUTYRATE + GLT -> GLT + 4-AMINO-BUTYRATE; direction=REVERSIBLE EcoCyc reaction equation: 4-AMINO-BUTYRATE + GLT -> GLT + 4-AMINO-BUTYRATE; direction=REVERSIBLE.

## Biological Role

Catalyzed by gadC (protein.P63235). Substrates: L-Glutamate (molecule.C00025), 4-Aminobutanoate (molecule.C00334). Products: L-Glutamate (molecule.C00025), 4-Aminobutanoate (molecule.C00334).

## Annotation

4-AMINO-BUTYRATE + GLT -> GLT + 4-AMINO-BUTYRATE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P63235|protein.P63235]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00334|molecule.C00334]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00334|molecule.C00334]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-261`

## Notes

4-AMINO-BUTYRATE + GLT -> GLT + 4-AMINO-BUTYRATE; direction=REVERSIBLE
