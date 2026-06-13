---
entity_id: "reaction.ecocyc.RXN-14394"
entity_type: "reaction"
name: "RXN-14394"
source_database: "EcoCyc"
source_id: "RXN-14394"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14394

`reaction.ecocyc.RXN-14394`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14394`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-7221 + ACETYL-COA -> CPD-15244 + CO-A; direction=REVERSIBLE EcoCyc reaction equation: CPD-7221 + ACETYL-COA -> CPD-15244 + CO-A; direction=REVERSIBLE.

## Biological Role

Catalyzed by fadA (protein.P21151), fadI (protein.P76503). Substrates: Acetyl-CoA (molecule.C00024), (3Z)-dodec-3-enoyl-CoA (molecule.ecocyc.CPD-7221). Products: CoA (molecule.C00010), 3-oxo-(5Z)-tetradecenoyl-CoA (molecule.ecocyc.CPD-15244).

## Enriched Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Annotation

CPD-7221 + ACETYL-COA -> CPD-15244 + CO-A; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P21151|protein.P21151]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P76503|protein.P76503]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-15244|molecule.ecocyc.CPD-15244]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-7221|molecule.ecocyc.CPD-7221]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14394`

## Notes

CPD-7221 + ACETYL-COA -> CPD-15244 + CO-A; direction=REVERSIBLE
