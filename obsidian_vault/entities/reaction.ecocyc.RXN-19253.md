---
entity_id: "reaction.ecocyc.RXN-19253"
entity_type: "reaction"
name: "RXN-19253"
source_database: "EcoCyc"
source_id: "RXN-19253"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19253

`reaction.ecocyc.RXN-19253`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19253`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

CPD-15384 + WATER -> CPD-20750 + D-ALANINE; direction=REVERSIBLE EcoCyc reaction equation: CPD-15384 + WATER -> CPD-20750 + D-ALANINE; direction=REVERSIBLE.

## Biological Role

Catalyzed by D-alanyl-D-alanine carboxypeptidase DacA (complex.ecocyc.CPLX0-8252), dacD (protein.P33013). Substrates: H2O (molecule.C00001), L-alanyl-γ-D-glutamyl-L-lysyl-D-alanyl-D-alanine (molecule.ecocyc.CPD-15384). Products: D-Alanine (molecule.C00133), L-alanyl-γ-D-glutamyl-L-lysyl-D-alanine (molecule.ecocyc.CPD-20750).

## Annotation

CPD-15384 + WATER -> CPD-20750 + D-ALANINE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8252|complex.ecocyc.CPLX0-8252]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P33013|protein.P33013]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00133|molecule.C00133]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-20750|molecule.ecocyc.CPD-20750]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-15384|molecule.ecocyc.CPD-15384]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19253`

## Notes

CPD-15384 + WATER -> CPD-20750 + D-ALANINE; direction=REVERSIBLE
