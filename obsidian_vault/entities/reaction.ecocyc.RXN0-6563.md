---
entity_id: "reaction.ecocyc.RXN0-6563"
entity_type: "reaction"
name: "RXN0-6563"
source_database: "EcoCyc"
source_id: "RXN0-6563"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6563

`reaction.ecocyc.RXN0-6563`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6563`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2189 -> GLYCOLALDEHYDE + GLY; direction=REVERSIBLE EcoCyc reaction equation: CPD0-2189 -> GLYCOLALDEHYDE + GLY; direction=REVERSIBLE.

## Biological Role

Catalyzed by low-specificity L-threonine aldolase (complex.ecocyc.LTAA-CPLX). Substrates: 4-Hydroxy-L-threonine (molecule.C06056). Products: Glycine (molecule.C00037), Glycolaldehyde (molecule.C00266).

## Annotation

CPD0-2189 -> GLYCOLALDEHYDE + GLY; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.LTAA-CPLX|complex.ecocyc.LTAA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00037|molecule.C00037]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00266|molecule.C00266]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C06056|molecule.C06056]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6563`

## Notes

CPD0-2189 -> GLYCOLALDEHYDE + GLY; direction=REVERSIBLE
