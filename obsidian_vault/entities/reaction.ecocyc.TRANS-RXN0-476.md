---
entity_id: "reaction.ecocyc.TRANS-RXN0-476"
entity_type: "reaction"
name: "TRANS-RXN0-476"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-476"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-476

`reaction.ecocyc.TRANS-RXN0-476`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-476`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

E. coli K-12 is capable of cobamide-dependent growth with ethanolamine as the sole source of carbon and nitrogen . EcoCyc reaction equation: ETHANOL-AMINE -> ETHANOL-AMINE; direction=LEFT-TO-RIGHT. E. coli K-12 is capable of cobamide-dependent growth with ethanolamine as the sole source of carbon and nitrogen .

## Biological Role

Substrates: Ethanolamine (molecule.C00189). Products: Ethanolamine (molecule.C00189).

## Annotation

E. coli K-12 is capable of cobamide-dependent growth with ethanolamine as the sole source of carbon and nitrogen .

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00189|molecule.C00189]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00189|molecule.C00189]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-476`

## Notes

ETHANOL-AMINE -> ETHANOL-AMINE; direction=LEFT-TO-RIGHT
