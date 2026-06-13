---
entity_id: "reaction.ecocyc.3.2.1.52-RXN"
entity_type: "reaction"
name: "3.2.1.52-RXN"
source_database: "EcoCyc"
source_id: "3.2.1.52-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "N-acetyl-&beta"
  - "-D-hexosaminidase"
---

# 3.2.1.52-RXN

`reaction.ecocyc.3.2.1.52-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.2.1.52-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

N-Acetyl-beta-D-Hexosaminides + WATER -> N-acetyl-beta-D-hexosamines + Alcohols; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: N-Acetyl-beta-D-Hexosaminides + WATER -> N-acetyl-beta-D-hexosamines + Alcohols; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), an N-acetyl-β-D-hexosaminide (molecule.ecocyc.N-Acetyl-beta-D-Hexosaminides). Products: an alcohol (molecule.ecocyc.Alcohols), an N-acetyl-β-D-hexosamine (molecule.ecocyc.N-acetyl-beta-D-hexosamines).

## Annotation

N-Acetyl-beta-D-Hexosaminides + WATER -> N-acetyl-beta-D-hexosamines + Alcohols; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.ecocyc.Alcohols|molecule.ecocyc.Alcohols]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.N-acetyl-beta-D-hexosamines|molecule.ecocyc.N-acetyl-beta-D-hexosamines]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.N-Acetyl-beta-D-Hexosaminides|molecule.ecocyc.N-Acetyl-beta-D-Hexosaminides]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3.2.1.52-RXN`

## Notes

N-Acetyl-beta-D-Hexosaminides + WATER -> N-acetyl-beta-D-hexosamines + Alcohols; direction=PHYSIOL-LEFT-TO-RIGHT
