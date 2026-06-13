---
entity_id: "reaction.ecocyc.2.7.7.61-RXN"
entity_type: "reaction"
name: "2.7.7.61-RXN"
source_database: "EcoCyc"
source_id: "2.7.7.61-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "2'-(5''-triphosphoribosyl)-3'-dephospho-CoA:apo-citrate"
  - "2'-(5''-phosphoribosyl)-3'-dephospho-CoA transferase"
---

# 2.7.7.61-RXN

`reaction.ecocyc.2.7.7.61-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2.7.7.61-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-5-TRIPHOSPHORIBOSYL-3-DEPHOSPHO- + APO-CITRATE-LYASE -> HOLO-CITRATE-LYASE + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 2-5-TRIPHOSPHORIBOSYL-3-DEPHOSPHO- + APO-CITRATE-LYASE -> HOLO-CITRATE-LYASE + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by citX (protein.P0A6G5). Substrates: 2'-(5''-triphospho-α-D-ribosyl)-3'-dephospho-CoA (molecule.ecocyc.2-5-TRIPHOSPHORIBOSYL-3-DEPHOSPHO-). Products: Diphosphate (molecule.C00013).

## Enriched Pathways

- `ecocyc.P2-PWY` citrate lyase activation (EcoCyc)

## Annotation

2-5-TRIPHOSPHORIBOSYL-3-DEPHOSPHO- + APO-CITRATE-LYASE -> HOLO-CITRATE-LYASE + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.P2-PWY` citrate lyase activation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P0A6G5|protein.P0A6G5]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.2-5-TRIPHOSPHORIBOSYL-3-DEPHOSPHO-|molecule.ecocyc.2-5-TRIPHOSPHORIBOSYL-3-DEPHOSPHO-]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:2.7.7.61-RXN`

## Notes

2-5-TRIPHOSPHORIBOSYL-3-DEPHOSPHO- + APO-CITRATE-LYASE -> HOLO-CITRATE-LYASE + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
