---
entity_id: "reaction.ecocyc.DIOHBUTANONEPSYN-RXN"
entity_type: "reaction"
name: "DIOHBUTANONEPSYN-RXN"
source_database: "EcoCyc"
source_id: "DIOHBUTANONEPSYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DIOHBUTANONEPSYN-RXN

`reaction.ecocyc.DIOHBUTANONEPSYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DIOHBUTANONEPSYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

A reaction involved in the synthesis of riboflavin: generation of an unusual 4 carbon carbohydrate. EcoCyc reaction equation: RIBULOSE-5P -> PROTON + DIHYDROXY-BUTANONE-P + FORMATE; direction=LEFT-TO-RIGHT. A reaction involved in the synthesis of riboflavin: generation of an unusual 4 carbon carbohydrate.

## Biological Role

Catalyzed by 3,4-dihydroxy-2-butanone-4-phosphate synthase (complex.ecocyc.DIOHBUTANONEPSYN-CPLX). Substrates: D-Ribulose 5-phosphate (molecule.C00199). Products: Formate (molecule.C00058), H+ (molecule.C00080), L-3,4-Dihydroxybutan-2-one 4-phosphate (molecule.C15556).

## Enriched Pathways

- `ecocyc.RIBOSYN2-PWY` flavin biosynthesis I (bacteria and plants) (EcoCyc)

## Annotation

A reaction involved in the synthesis of riboflavin: generation of an unusual 4 carbon carbohydrate.

## Pathways

- `ecocyc.RIBOSYN2-PWY` flavin biosynthesis I (bacteria and plants) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.DIOHBUTANONEPSYN-CPLX|complex.ecocyc.DIOHBUTANONEPSYN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00058|molecule.C00058]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C15556|molecule.C15556]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00199|molecule.C00199]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:DIOHBUTANONEPSYN-RXN`

## Notes

RIBULOSE-5P -> PROTON + DIHYDROXY-BUTANONE-P + FORMATE; direction=LEFT-TO-RIGHT
