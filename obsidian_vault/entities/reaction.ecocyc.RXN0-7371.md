---
entity_id: "reaction.ecocyc.RXN0-7371"
entity_type: "reaction"
name: "RXN0-7371"
source_database: "EcoCyc"
source_id: "RXN0-7371"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7371

`reaction.ecocyc.RXN0-7371`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7371`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Protein-L-serine-or-L-threonine + ATP -> Protein-Ser-or-Thr-adenylate + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Protein-L-serine-or-L-threonine + ATP -> Protein-Ser-or-Thr-adenylate + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by selO (protein.P77649). Substrates: ATP (molecule.C00002), a [protein]-(L-serine/L-threonine) (molecule.ecocyc.Protein-L-serine-or-L-threonine). Products: Diphosphate (molecule.C00013), an O-(5'-adenylyl)-L-serine/L-threonine-[protein] (molecule.ecocyc.Protein-Ser-or-Thr-adenylate).

## Annotation

Protein-L-serine-or-L-threonine + ATP -> Protein-Ser-or-Thr-adenylate + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P77649|protein.P77649]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Protein-Ser-or-Thr-adenylate|molecule.ecocyc.Protein-Ser-or-Thr-adenylate]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Protein-L-serine-or-L-threonine|molecule.ecocyc.Protein-L-serine-or-L-threonine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7371`

## Notes

Protein-L-serine-or-L-threonine + ATP -> Protein-Ser-or-Thr-adenylate + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
