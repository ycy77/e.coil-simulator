---
entity_id: "reaction.ecocyc.2.7.8.25-RXN"
entity_type: "reaction"
name: "2.7.8.25-RXN"
source_database: "EcoCyc"
source_id: "2.7.8.25-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "2'-(5''-triphosphoribosyl)-3-dephospho-CoA synthase"
---

# 2.7.8.25-RXN

`reaction.ecocyc.2.7.8.25-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2.7.8.25-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DEPHOSPHO-COA + ATP -> 2-5-TRIPHOSPHORIBOSYL-3-DEPHOSPHO- + ADENINE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: DEPHOSPHO-COA + ATP -> 2-5-TRIPHOSPHORIBOSYL-3-DEPHOSPHO- + ADENINE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by citG (protein.P77231). Substrates: ATP (molecule.C00002), Dephospho-CoA (molecule.C00882). Products: Adenine (molecule.C00147), 2'-(5''-triphospho-α-D-ribosyl)-3'-dephospho-CoA (molecule.ecocyc.2-5-TRIPHOSPHORIBOSYL-3-DEPHOSPHO-).

## Enriched Pathways

- `ecocyc.P2-PWY` citrate lyase activation (EcoCyc)

## Annotation

DEPHOSPHO-COA + ATP -> 2-5-TRIPHOSPHORIBOSYL-3-DEPHOSPHO- + ADENINE; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.P2-PWY` citrate lyase activation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P77231|protein.P77231]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00147|molecule.C00147]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.2-5-TRIPHOSPHORIBOSYL-3-DEPHOSPHO-|molecule.ecocyc.2-5-TRIPHOSPHORIBOSYL-3-DEPHOSPHO-]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00882|molecule.C00882]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:2.7.8.25-RXN`

## Notes

DEPHOSPHO-COA + ATP -> 2-5-TRIPHOSPHORIBOSYL-3-DEPHOSPHO- + ADENINE; direction=PHYSIOL-LEFT-TO-RIGHT
