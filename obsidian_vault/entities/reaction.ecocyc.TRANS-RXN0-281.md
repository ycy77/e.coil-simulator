---
entity_id: "reaction.ecocyc.TRANS-RXN0-281"
entity_type: "reaction"
name: "TRANS-RXN0-281"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-281"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-281

`reaction.ecocyc.TRANS-RXN0-281`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-281`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

3-KETOBUTYRATE -> 3-KETOBUTYRATE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: 3-KETOBUTYRATE -> 3-KETOBUTYRATE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by atoE (protein.P76460). Substrates: Acetoacetate (molecule.C00164). Products: Acetoacetate (molecule.C00164).

## Annotation

3-KETOBUTYRATE -> 3-KETOBUTYRATE; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P76460|protein.P76460]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00164|molecule.C00164]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00164|molecule.C00164]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-281`

## Notes

3-KETOBUTYRATE -> 3-KETOBUTYRATE; direction=LEFT-TO-RIGHT
