---
entity_id: "reaction.ecocyc.RXN0-6564"
entity_type: "reaction"
name: "RXN0-6564"
source_database: "EcoCyc"
source_id: "RXN0-6564"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6564

`reaction.ecocyc.RXN0-6564`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6564`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2189 + ATP -> PROTON + 4-PHOSPHONOOXY-THREONINE + ADP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-2189 + ATP -> PROTON + 4-PHOSPHONOOXY-THREONINE + ADP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by homoserine kinase (complex.ecocyc.HOMOSERKIN-CPLX). Substrates: ATP (molecule.C00002), 4-Hydroxy-L-threonine (molecule.C06056). Products: ADP (molecule.C00008), H+ (molecule.C00080), O-Phospho-4-hydroxy-L-threonine (molecule.C06055).

## Annotation

CPD0-2189 + ATP -> PROTON + 4-PHOSPHONOOXY-THREONINE + ADP; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.HOMOSERKIN-CPLX|complex.ecocyc.HOMOSERKIN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C06055|molecule.C06055]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C06056|molecule.C06056]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6564`

## Notes

CPD0-2189 + ATP -> PROTON + 4-PHOSPHONOOXY-THREONINE + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
