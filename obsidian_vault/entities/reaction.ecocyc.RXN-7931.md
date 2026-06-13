---
entity_id: "reaction.ecocyc.RXN-7931"
entity_type: "reaction"
name: "RXN-7931"
source_database: "EcoCyc"
source_id: "RXN-7931"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-7931

`reaction.ecocyc.RXN-7931`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-7931`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-7221 -> CPD-7222; direction=REVERSIBLE EcoCyc reaction equation: CPD-7221 -> CPD-7222; direction=REVERSIBLE.

## Biological Role

Substrates: (3Z)-dodec-3-enoyl-CoA (molecule.ecocyc.CPD-7221). Products: 2-trans-Dodecenoyl-CoA (molecule.C03221).

## Enriched Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Annotation

CPD-7221 -> CPD-7222; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C03221|molecule.C03221]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-7221|molecule.ecocyc.CPD-7221]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-7931`

## Notes

CPD-7221 -> CPD-7222; direction=REVERSIBLE
