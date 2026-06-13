---
entity_id: "reaction.ecocyc.RXN0-6259"
entity_type: "reaction"
name: "RXN0-6259"
source_database: "EcoCyc"
source_id: "RXN0-6259"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6259

`reaction.ecocyc.RXN0-6259`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6259`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Menaquinols + PROTOPORPHYRIN_IX -> Menaquinones + PROTOPORPHYRINOGEN; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: Menaquinols + PROTOPORPHYRIN_IX -> Menaquinones + PROTOPORPHYRINOGEN; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by protoporphyrinogen oxidase (complex.ecocyc.CPLX0-7811). Substrates: Protoporphyrin (molecule.C02191), Menaquinol (molecule.C05819). Products: Menaquinone (molecule.C00828), Protoporphyrinogen IX (molecule.C01079).

## Enriched Pathways

- `ecocyc.HEMESYN2-PWY` heme b biosynthesis II (oxygen-independent) (EcoCyc)

## Annotation

Menaquinols + PROTOPORPHYRIN_IX -> Menaquinones + PROTOPORPHYRINOGEN; direction=PHYSIOL-RIGHT-TO-LEFT

## Pathways

- `ecocyc.HEMESYN2-PWY` heme b biosynthesis II (oxygen-independent) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7811|complex.ecocyc.CPLX0-7811]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00828|molecule.C00828]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01079|molecule.C01079]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C02191|molecule.C02191]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05819|molecule.C05819]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6259`

## Notes

Menaquinols + PROTOPORPHYRIN_IX -> Menaquinones + PROTOPORPHYRINOGEN; direction=PHYSIOL-RIGHT-TO-LEFT
