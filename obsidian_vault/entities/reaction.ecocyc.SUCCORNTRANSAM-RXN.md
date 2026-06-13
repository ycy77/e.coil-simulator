---
entity_id: "reaction.ecocyc.SUCCORNTRANSAM-RXN"
entity_type: "reaction"
name: "SUCCORNTRANSAM-RXN"
source_database: "EcoCyc"
source_id: "SUCCORNTRANSAM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# SUCCORNTRANSAM-RXN

`reaction.ecocyc.SUCCORNTRANSAM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:SUCCORNTRANSAM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

N2-SUCCINYLORNITHINE + 2-KETOGLUTARATE -> CPD-822 + GLT; direction=REVERSIBLE EcoCyc reaction equation: N2-SUCCINYLORNITHINE + 2-KETOGLUTARATE -> CPD-822 + GLT; direction=REVERSIBLE.

## Biological Role

Catalyzed by succinylornithine transaminase (complex.ecocyc.SUCCORNTRANSAM-CPLX). Substrates: 2-Oxoglutarate (molecule.C00026), N2-Succinyl-L-ornithine (molecule.C03415). Products: L-Glutamate (molecule.C00025), N-Succinyl-L-glutamate 5-semialdehyde (molecule.C05932).

## Enriched Pathways

- `ecocyc.AST-PWY` L-arginine degradation II (AST pathway) (EcoCyc)

## Annotation

N2-SUCCINYLORNITHINE + 2-KETOGLUTARATE -> CPD-822 + GLT; direction=REVERSIBLE

## Pathways

- `ecocyc.AST-PWY` L-arginine degradation II (AST pathway) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.SUCCORNTRANSAM-CPLX|complex.ecocyc.SUCCORNTRANSAM-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05932|molecule.C05932]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03415|molecule.C03415]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:SUCCORNTRANSAM-RXN`

## Notes

N2-SUCCINYLORNITHINE + 2-KETOGLUTARATE -> CPD-822 + GLT; direction=REVERSIBLE
