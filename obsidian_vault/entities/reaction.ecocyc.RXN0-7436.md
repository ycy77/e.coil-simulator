---
entity_id: "reaction.ecocyc.RXN0-7436"
entity_type: "reaction"
name: "RXN0-7436"
source_database: "EcoCyc"
source_id: "RXN0-7436"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7436

`reaction.ecocyc.RXN0-7436`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7436`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + CPD0-1605 -> ADP + CPD0-1221 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + CPD0-1605 -> ADP + CPD0-1221 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by pyridoxal kinase 1 / hydroxymethylpyrimidine kinase (complex.ecocyc.PDXK-CPLX). Substrates: ATP (molecule.C00002), 4-deoxypyridoxine (molecule.ecocyc.CPD0-1605). Products: ADP (molecule.C00008), H+ (molecule.C00080), 4-deoxypyridoxine 5'-phosphate (molecule.ecocyc.CPD0-1221).

## Annotation

ATP + CPD0-1605 -> ADP + CPD0-1221 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.PDXK-CPLX|complex.ecocyc.PDXK-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-1221|molecule.ecocyc.CPD0-1221]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1605|molecule.ecocyc.CPD0-1605]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7436`

## Notes

ATP + CPD0-1605 -> ADP + CPD0-1221 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
