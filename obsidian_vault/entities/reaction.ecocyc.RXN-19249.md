---
entity_id: "reaction.ecocyc.RXN-19249"
entity_type: "reaction"
name: "RXN-19249"
source_database: "EcoCyc"
source_id: "RXN-19249"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19249

`reaction.ecocyc.RXN-19249`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19249`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

CPD0-1965 + WATER -> CPD-20746 + D-ALANINE; direction=REVERSIBLE EcoCyc reaction equation: CPD0-1965 + WATER -> CPD-20746 + D-ALANINE; direction=REVERSIBLE.

## Biological Role

Catalyzed by D-alanyl-D-alanine carboxypeptidase DacA (complex.ecocyc.CPLX0-8252), D-alanyl-D-alanine carboxypeptidase DacC (complex.ecocyc.CPLX0-8254), dacD (protein.P33013). Substrates: H2O (molecule.C00001), Nα,Nε-diacetyl-lysyl-D-alanyl-D-alanine (molecule.ecocyc.CPD0-1965). Products: D-Alanine (molecule.C00133), Nα,Nε-diacetyl-lysyl-D-alanine (molecule.ecocyc.CPD-20746).

## Annotation

CPD0-1965 + WATER -> CPD-20746 + D-ALANINE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8252|complex.ecocyc.CPLX0-8252]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8254|complex.ecocyc.CPLX0-8254]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P33013|protein.P33013]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00133|molecule.C00133]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-20746|molecule.ecocyc.CPD-20746]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1965|molecule.ecocyc.CPD0-1965]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00067|molecule.C00067]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-29|molecule.ecocyc.CPD-29]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.N-ETHYLMALEIMIDE|molecule.ecocyc.N-ETHYLMALEIMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.PHMB|molecule.ecocyc.PHMB]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-19249`

## Notes

CPD0-1965 + WATER -> CPD-20746 + D-ALANINE; direction=REVERSIBLE
