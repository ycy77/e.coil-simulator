---
entity_id: "reaction.ecocyc.TRANS-RXN0-631"
entity_type: "reaction"
name: "TRANS-RXN0-631"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-631"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-631

`reaction.ecocyc.TRANS-RXN0-631`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-631`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Purine-Nucleosides -> Purine-Nucleosides; direction=LEFT-TO-RIGHT EcoCyc reaction equation: Purine-Nucleosides -> Purine-Nucleosides; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by punC (protein.P37597). Substrates: a purine nucleoside (molecule.ecocyc.Purine-Nucleosides). Products: a purine nucleoside (molecule.ecocyc.Purine-Nucleosides).

## Annotation

Purine-Nucleosides -> Purine-Nucleosides; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P37597|protein.P37597]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Purine-Nucleosides|molecule.ecocyc.Purine-Nucleosides]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Purine-Nucleosides|molecule.ecocyc.Purine-Nucleosides]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-631`

## Notes

Purine-Nucleosides -> Purine-Nucleosides; direction=LEFT-TO-RIGHT
