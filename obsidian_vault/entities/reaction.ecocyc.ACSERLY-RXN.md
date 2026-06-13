---
entity_id: "reaction.ecocyc.ACSERLY-RXN"
entity_type: "reaction"
name: "ACSERLY-RXN"
source_database: "EcoCyc"
source_id: "ACSERLY-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ACSERLY-RXN

`reaction.ecocyc.ACSERLY-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ACSERLY-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second reaction in the conversion of serine to cysteine. Thioredoxin can also serve as source of sulfide. EcoCyc reaction equation: ACETYLSERINE + HS -> PROTON + CYS + ACET; direction=LEFT-TO-RIGHT. This is the second reaction in the conversion of serine to cysteine. Thioredoxin can also serve as source of sulfide.

## Biological Role

Catalyzed by cysteine synthase A (complex.ecocyc.ACSERLYA-CPLX), cysteine synthase B (complex.ecocyc.ACSERLYB-CPLX). Substrates: Hydrogen sulfide (molecule.C00283), O-Acetyl-L-serine (molecule.C00979). Products: Acetate (molecule.C00033), H+ (molecule.C00080), L-Cysteine (molecule.C00097).

## Enriched Pathways

- `ecocyc.CYSTSYN-PWY` L-cysteine biosynthesis I (EcoCyc)

## Annotation

This is the second reaction in the conversion of serine to cysteine. Thioredoxin can also serve as source of sulfide.

## Pathways

- `ecocyc.CYSTSYN-PWY` L-cysteine biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.ACSERLYA-CPLX|complex.ecocyc.ACSERLYA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.ACSERLYB-CPLX|complex.ecocyc.ACSERLYB-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00033|molecule.C00033]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00283|molecule.C00283]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00979|molecule.C00979]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ACSERLY-RXN`

## Notes

ACETYLSERINE + HS -> PROTON + CYS + ACET; direction=LEFT-TO-RIGHT
