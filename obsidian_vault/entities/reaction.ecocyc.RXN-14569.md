---
entity_id: "reaction.ecocyc.RXN-14569"
entity_type: "reaction"
name: "RXN-14569"
source_database: "EcoCyc"
source_id: "RXN-14569"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14569

`reaction.ecocyc.RXN-14569`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14569`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

THR + HCO3 + ATP -> CPD-15435 + PPI + WATER; direction=REVERSIBLE EcoCyc reaction equation: THR + HCO3 + ATP -> CPD-15435 + PPI + WATER; direction=REVERSIBLE.

## Biological Role

Catalyzed by tsaC (protein.P45748). Substrates: ATP (molecule.C00002), L-Threonine (molecule.C00188), HCO3- (molecule.C00288). Products: H2O (molecule.C00001), Diphosphate (molecule.C00013), (L-threonylcarbamoyl)adenylate (molecule.ecocyc.CPD-15435).

## Enriched Pathways

- `ecocyc.PWY0-1587` N6-L-threonylcarbamoyladenosine37-modified tRNA biosynthesis (EcoCyc)

## Annotation

THR + HCO3 + ATP -> CPD-15435 + PPI + WATER; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-1587` N6-L-threonylcarbamoyladenosine37-modified tRNA biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `activates` <-- [[molecule.C00288|molecule.C00288]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P45748|protein.P45748]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-15435|molecule.ecocyc.CPD-15435]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00188|molecule.C00188]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00288|molecule.C00288]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14569`

## Notes

THR + HCO3 + ATP -> CPD-15435 + PPI + WATER; direction=REVERSIBLE
