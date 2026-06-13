---
entity_id: "reaction.ecocyc.RXN-17633"
entity_type: "reaction"
name: "RXN-17633"
source_database: "EcoCyc"
source_id: "RXN-17633"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17633

`reaction.ecocyc.RXN-17633`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17633`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

METHYL-GLYOXAL + PROT-CYS -> Protein-Cysteine-Hemithioacetal; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: METHYL-GLYOXAL + PROT-CYS -> Protein-Cysteine-Hemithioacetal; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Methylglyoxal (molecule.C00546), a [protein]-L-cysteine (molecule.ecocyc.PROT-CYS). Products: an S-(1-hydroxy-2-oxopropyl)-[protein]-L-cysteine (molecule.ecocyc.Protein-Cysteine-Hemithioacetal).

## Annotation

METHYL-GLYOXAL + PROT-CYS -> Protein-Cysteine-Hemithioacetal; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.ecocyc.Protein-Cysteine-Hemithioacetal|molecule.ecocyc.Protein-Cysteine-Hemithioacetal]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00546|molecule.C00546]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.PROT-CYS|molecule.ecocyc.PROT-CYS]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17633`

## Notes

METHYL-GLYOXAL + PROT-CYS -> Protein-Cysteine-Hemithioacetal; direction=PHYSIOL-LEFT-TO-RIGHT
