---
entity_id: "reaction.ecocyc.R15-RXN"
entity_type: "reaction"
name: "R15-RXN"
source_database: "EcoCyc"
source_id: "R15-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# R15-RXN

`reaction.ecocyc.R15-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:R15-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

MET + 2-Oxo-carboxylates -> CPD-479 + Amino-Acids-20; direction=REVERSIBLE EcoCyc reaction equation: MET + 2-Oxo-carboxylates -> CPD-479 + Amino-Acids-20; direction=REVERSIBLE.

## Biological Role

Catalyzed by methionine transaminase (complex.ecocyc.CPLX0-8561). Substrates: L-Methionine (molecule.C00073), a 2-oxo carboxylate (molecule.ecocyc.2-Oxo-carboxylates). Products: 4-Methylthio-2-oxobutanoic acid (molecule.C01180), a proteinogenic amino acid (molecule.ecocyc.Amino-Acids-20).

## Annotation

MET + 2-Oxo-carboxylates -> CPD-479 + Amino-Acids-20; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8561|complex.ecocyc.CPLX0-8561]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C01180|molecule.C01180]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Amino-Acids-20|molecule.ecocyc.Amino-Acids-20]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00073|molecule.C00073]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.2-Oxo-carboxylates|molecule.ecocyc.2-Oxo-carboxylates]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:R15-RXN`

## Notes

MET + 2-Oxo-carboxylates -> CPD-479 + Amino-Acids-20; direction=REVERSIBLE
