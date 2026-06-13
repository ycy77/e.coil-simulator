---
entity_id: "reaction.ecocyc.SUCCCOASYN-RXN"
entity_type: "reaction"
name: "SUCCCOASYN-RXN"
source_database: "EcoCyc"
source_id: "SUCCCOASYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "SUCCINYL-COA SYNTHETASE (ADP-FORMING)"
---

# SUCCCOASYN-RXN

`reaction.ecocyc.SUCCCOASYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:SUCCCOASYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

SUBREACTIONS: Enz + ATP = Enz-P + ADP Enz-P + succinate = Enz.succinylP Enz.succinylP + CoA = Enz + Pi + succinylCoa EcoCyc reaction equation: SUC + CO-A + ATP -> SUC-COA + ADP + Pi; direction=REVERSIBLE. SUBREACTIONS: Enz + ATP = Enz-P + ADP Enz-P + succinate = Enz.succinylP Enz.succinylP + CoA = Enz + Pi + succinylCoa

## Biological Role

Catalyzed by succinyl-CoA synthetase (complex.ecocyc.SUCCCOASYN). Substrates: ATP (molecule.C00002), CoA (molecule.C00010), Succinate (molecule.C00042). Products: ADP (molecule.C00008), Succinyl-CoA (molecule.C00091), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.TCA` TCA cycle I (prokaryotic) (EcoCyc)

## Annotation

SUBREACTIONS: Enz + ATP = Enz-P + ADP Enz-P + succinate = Enz.succinylP Enz.succinylP + CoA = Enz + Pi + succinylCoa

## Pathways

- `ecocyc.TCA` TCA cycle I (prokaryotic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `activates` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.SUCCCOASYN|complex.ecocyc.SUCCCOASYN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00091|molecule.C00091]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:SUCCCOASYN-RXN`

## Notes

SUC + CO-A + ATP -> SUC-COA + ADP + Pi; direction=REVERSIBLE
