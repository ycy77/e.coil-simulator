---
entity_id: "reaction.ecocyc.RXN0-5040"
entity_type: "reaction"
name: "RXN0-5040"
source_database: "EcoCyc"
source_id: "RXN0-5040"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5040

`reaction.ecocyc.RXN0-5040`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5040`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

WATER + CPD0-889 -> P-AMINO-BENZOATE + GLT; direction=LEFT-TO-RIGHT EcoCyc reaction equation: WATER + CPD0-889 -> P-AMINO-BENZOATE + GLT; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by p-aminobenzoyl-glutamate hydrolase (complex.ecocyc.CPLX0-7844). Substrates: H2O (molecule.C00001), N-(4-aminobenzoyl)-L-glutamate (molecule.ecocyc.CPD0-889). Products: L-Glutamate (molecule.C00025), 4-Aminobenzoate (molecule.C00568).

## Annotation

WATER + CPD0-889 -> P-AMINO-BENZOATE + GLT; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7844|complex.ecocyc.CPLX0-7844]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00568|molecule.C00568]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-889|molecule.ecocyc.CPD0-889]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5040`

## Notes

WATER + CPD0-889 -> P-AMINO-BENZOATE + GLT; direction=LEFT-TO-RIGHT
