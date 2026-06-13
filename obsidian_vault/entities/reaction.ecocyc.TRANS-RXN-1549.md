---
entity_id: "reaction.ecocyc.TRANS-RXN-1549"
entity_type: "reaction"
name: "L-glutamine:4-aminobutanoate antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-1549"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# L-glutamine:4-aminobutanoate antiport

`reaction.ecocyc.TRANS-RXN-1549`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-1549`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

GLN + 4-AMINO-BUTYRATE -> GLN + 4-AMINO-BUTYRATE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: GLN + 4-AMINO-BUTYRATE -> GLN + 4-AMINO-BUTYRATE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by gadC (protein.P63235). Substrates: L-Glutamine (molecule.C00064), 4-Aminobutanoate (molecule.C00334). Products: L-Glutamine (molecule.C00064), 4-Aminobutanoate (molecule.C00334).

## Annotation

GLN + 4-AMINO-BUTYRATE -> GLN + 4-AMINO-BUTYRATE; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P63235|protein.P63235]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00064|molecule.C00064]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00334|molecule.C00334]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00064|molecule.C00064]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00334|molecule.C00334]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-1549`

## Notes

GLN + 4-AMINO-BUTYRATE -> GLN + 4-AMINO-BUTYRATE; direction=LEFT-TO-RIGHT
