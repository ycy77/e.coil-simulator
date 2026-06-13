---
entity_id: "reaction.ecocyc.RXN-19854"
entity_type: "reaction"
name: "RXN-19854"
source_database: "EcoCyc"
source_id: "RXN-19854"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19854

`reaction.ecocyc.RXN-19854`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19854`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Protein-L-Aspartates + Protein-phospho-L-histidines -> Protein-Histidines + CPD-21398; direction=REVERSIBLE EcoCyc reaction equation: Protein-L-Aspartates + Protein-phospho-L-histidines -> Protein-Histidines + CPD-21398; direction=REVERSIBLE.

## Biological Role

Substrates: a [protein]-L-aspartate (molecule.ecocyc.Protein-L-Aspartates), a [protein]-N-phospho-L-histidine (molecule.ecocyc.Protein-phospho-L-histidines). Products: a [protein]-phospho-L-aspartate (molecule.ecocyc.CPD-21398), a [protein]-L-histidine (molecule.ecocyc.Protein-Histidines).

## Annotation

Protein-L-Aspartates + Protein-phospho-L-histidines -> Protein-Histidines + CPD-21398; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.ecocyc.CPD-21398|molecule.ecocyc.CPD-21398]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Protein-Histidines|molecule.ecocyc.Protein-Histidines]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Protein-L-Aspartates|molecule.ecocyc.Protein-L-Aspartates]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Protein-phospho-L-histidines|molecule.ecocyc.Protein-phospho-L-histidines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19854`

## Notes

Protein-L-Aspartates + Protein-phospho-L-histidines -> Protein-Histidines + CPD-21398; direction=REVERSIBLE
