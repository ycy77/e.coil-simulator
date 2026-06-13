---
entity_id: "reaction.ecocyc.RXN-20691"
entity_type: "reaction"
name: "RXN-20691"
source_database: "EcoCyc"
source_id: "RXN-20691"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-20691

`reaction.ecocyc.RXN-20691`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-20691`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Ox-Prx-Disulfide-Reductases + NADH + PROTON -> Red-Prx-Disulfide-Reductases + NAD; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: Ox-Prx-Disulfide-Reductases + NADH + PROTON -> Red-Prx-Disulfide-Reductases + NAD; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Substrates: NADH (molecule.C00004), H+ (molecule.C00080). Products: NAD+ (molecule.C00003).

## Annotation

Ox-Prx-Disulfide-Reductases + NADH + PROTON -> Red-Prx-Disulfide-Reductases + NAD; direction=PHYSIOL-RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-20691`

## Notes

Ox-Prx-Disulfide-Reductases + NADH + PROTON -> Red-Prx-Disulfide-Reductases + NAD; direction=PHYSIOL-RIGHT-TO-LEFT
