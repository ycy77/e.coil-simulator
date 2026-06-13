---
entity_id: "reaction.ecocyc.RXN-24100"
entity_type: "reaction"
name: "RXN-24100"
source_database: "EcoCyc"
source_id: "RXN-24100"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-24100

`reaction.ecocyc.RXN-24100`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-24100`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + Protein-L-serines -> ADP + Protein-Phosphoserines + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + Protein-L-serines -> ADP + Protein-Phosphoserines + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), a [protein]-L-serine (molecule.ecocyc.Protein-L-serines). Products: ADP (molecule.C00008), H+ (molecule.C00080), a [protein]-O-phospho-L-serine (molecule.ecocyc.Protein-Phosphoserines).

## Annotation

ATP + Protein-L-serines -> ADP + Protein-Phosphoserines + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Protein-Phosphoserines|molecule.ecocyc.Protein-Phosphoserines]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Protein-L-serines|molecule.ecocyc.Protein-L-serines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-24100`

## Notes

ATP + Protein-L-serines -> ADP + Protein-Phosphoserines + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
