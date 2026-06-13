---
entity_id: "reaction.ecocyc.RXN-19256"
entity_type: "reaction"
name: "RXN-19256"
source_database: "EcoCyc"
source_id: "RXN-19256"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19256

`reaction.ecocyc.RXN-19256`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19256`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

CPD-20756 + WATER -> CPD-20757 + D-ALANINE; direction=REVERSIBLE EcoCyc reaction equation: CPD-20756 + WATER -> CPD-20757 + D-ALANINE; direction=REVERSIBLE.

## Biological Role

Catalyzed by D-alanyl-D-alanine carboxypeptidase DacC (complex.ecocyc.CPLX0-8254). Substrates: H2O (molecule.C00001), N-acetyl-muramoyl-(L-alanyl-γ-D-glutamyl-L-lysyl-D-alanyl-D-alanine) (molecule.ecocyc.CPD-20756). Products: D-Alanine (molecule.C00133), N-acetyl-muramoyl-(L-alanyl-γ-D-glutamyl-L-lysyl-D-alanine) (molecule.ecocyc.CPD-20757).

## Annotation

CPD-20756 + WATER -> CPD-20757 + D-ALANINE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8254|complex.ecocyc.CPLX0-8254]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00133|molecule.C00133]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-20757|molecule.ecocyc.CPD-20757]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-20756|molecule.ecocyc.CPD-20756]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19256`

## Notes

CPD-20756 + WATER -> CPD-20757 + D-ALANINE; direction=REVERSIBLE
