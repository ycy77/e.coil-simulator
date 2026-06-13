---
entity_id: "reaction.ecocyc.RXN-15315"
entity_type: "reaction"
name: "RXN-15315"
source_database: "EcoCyc"
source_id: "RXN-15315"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-OUTER-MEM"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-15315

`reaction.ecocyc.RXN-15315`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15315`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-OUTER-MEM

## Enriched Summary

CPD0-1123 -> CPD0-1123; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-1123 -> CPD0-1123; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nanC (protein.P69856). Substrates: N-acetyl-β-neuraminate (molecule.ecocyc.CPD0-1123). Products: N-acetyl-β-neuraminate (molecule.ecocyc.CPD0-1123).

## Annotation

CPD0-1123 -> CPD0-1123; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P69856|protein.P69856]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD0-1123|molecule.ecocyc.CPD0-1123]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1123|molecule.ecocyc.CPD0-1123]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-15315`

## Notes

CPD0-1123 -> CPD0-1123; direction=LEFT-TO-RIGHT
