---
entity_id: "reaction.ecocyc.TRANS-RXN0-468"
entity_type: "reaction"
name: "TRANS-RXN0-468"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-468"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-OUTER-MEM"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-468

`reaction.ecocyc.TRANS-RXN0-468`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-468`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-OUTER-MEM

## Enriched Summary

Nucleosides -> Nucleosides; direction=LEFT-TO-RIGHT EcoCyc reaction equation: Nucleosides -> Nucleosides; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by tsx (protein.P0A927). Substrates: a nucleoside (molecule.ecocyc.Nucleosides). Products: a nucleoside (molecule.ecocyc.Nucleosides).

## Annotation

Nucleosides -> Nucleosides; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P0A927|protein.P0A927]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Nucleosides|molecule.ecocyc.Nucleosides]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Nucleosides|molecule.ecocyc.Nucleosides]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-468`

## Notes

Nucleosides -> Nucleosides; direction=LEFT-TO-RIGHT
