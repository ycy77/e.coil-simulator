---
entity_id: "reaction.ecocyc.RXN-22616"
entity_type: "reaction"
name: "RXN-22616"
source_database: "EcoCyc"
source_id: "RXN-22616"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22616

`reaction.ecocyc.RXN-22616`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22616`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

1-Cys-Peroxiredoxin-L-hydroxycysteine + Red-Thioredoxin -> 1-Cys-Peroxiredoxin-L-cysteine + Ox-Thioredoxin + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 1-Cys-Peroxiredoxin-L-hydroxycysteine + Red-Thioredoxin -> 1-Cys-Peroxiredoxin-L-cysteine + Ox-Thioredoxin + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: a [1-Cys-peroxiredoxin]-S-hydroxy-L-cysteine (molecule.ecocyc.1-Cys-Peroxiredoxin-L-hydroxycysteine). Products: H2O (molecule.C00001), a [1-Cys-peroxiredoxin]-L-cysteine (molecule.ecocyc.1-Cys-Peroxiredoxin-L-cysteine).

## Annotation

1-Cys-Peroxiredoxin-L-hydroxycysteine + Red-Thioredoxin -> 1-Cys-Peroxiredoxin-L-cysteine + Ox-Thioredoxin + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.1-Cys-Peroxiredoxin-L-cysteine|molecule.ecocyc.1-Cys-Peroxiredoxin-L-cysteine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.1-Cys-Peroxiredoxin-L-hydroxycysteine|molecule.ecocyc.1-Cys-Peroxiredoxin-L-hydroxycysteine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22616`

## Notes

1-Cys-Peroxiredoxin-L-hydroxycysteine + Red-Thioredoxin -> 1-Cys-Peroxiredoxin-L-cysteine + Ox-Thioredoxin + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
