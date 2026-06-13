---
entity_id: "reaction.ecocyc.SULFOCYS-RXN"
entity_type: "reaction"
name: "SULFOCYS-RXN"
source_database: "EcoCyc"
source_id: "SULFOCYS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# SULFOCYS-RXN

`reaction.ecocyc.SULFOCYS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:SULFOCYS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ACETYLSERINE + S2O3 -> PROTON + SULFO-CYSTEINE + ACET; direction=REVERSIBLE EcoCyc reaction equation: ACETYLSERINE + S2O3 -> PROTON + SULFO-CYSTEINE + ACET; direction=REVERSIBLE.

## Biological Role

Catalyzed by cysteine synthase B (complex.ecocyc.ACSERLYB-CPLX). Substrates: Thiosulfate (molecule.C00320), O-Acetyl-L-serine (molecule.C00979). Products: Acetate (molecule.C00033), H+ (molecule.C00080), S-Sulfo-L-cysteine (molecule.C05824).

## Enriched Pathways

- `ecocyc.PWY-7870` L-cysteine biosynthesis VII (from S-sulfo-L-cysteine) (EcoCyc)

## Annotation

ACETYLSERINE + S2O3 -> PROTON + SULFO-CYSTEINE + ACET; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY-7870` L-cysteine biosynthesis VII (from S-sulfo-L-cysteine) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.ACSERLYB-CPLX|complex.ecocyc.ACSERLYB-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00033|molecule.C00033]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05824|molecule.C05824]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00320|molecule.C00320]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00979|molecule.C00979]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:SULFOCYS-RXN`

## Notes

ACETYLSERINE + S2O3 -> PROTON + SULFO-CYSTEINE + ACET; direction=REVERSIBLE
