---
entity_id: "reaction.ecocyc.ADCLY-RXN"
entity_type: "reaction"
name: "ADCLY-RXN"
source_database: "EcoCyc"
source_id: "ADCLY-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ADCLY-RXN

`reaction.ecocyc.ADCLY-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ADCLY-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second step in para-aminobenzoate biosynthesis. EcoCyc reaction equation: 4-AMINO-4-DEOXYCHORISMATE -> PROTON + P-AMINO-BENZOATE + PYRUVATE; direction=LEFT-TO-RIGHT. This is the second step in para-aminobenzoate biosynthesis.

## Biological Role

Catalyzed by aminodeoxychorismate lyase (complex.ecocyc.ADCLY-CPLX). Substrates: 4-Amino-4-deoxychorismate (molecule.C11355). Products: Pyruvate (molecule.C00022), H+ (molecule.C00080), 4-Aminobenzoate (molecule.C00568).

## Enriched Pathways

- `ecocyc.PWY-6543` 4-aminobenzoate biosynthesis I (EcoCyc)

## Annotation

This is the second step in para-aminobenzoate biosynthesis.

## Pathways

- `ecocyc.PWY-6543` 4-aminobenzoate biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.ADCLY-CPLX|complex.ecocyc.ADCLY-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00568|molecule.C00568]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C11355|molecule.C11355]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ADCLY-RXN`

## Notes

4-AMINO-4-DEOXYCHORISMATE -> PROTON + P-AMINO-BENZOATE + PYRUVATE; direction=LEFT-TO-RIGHT
