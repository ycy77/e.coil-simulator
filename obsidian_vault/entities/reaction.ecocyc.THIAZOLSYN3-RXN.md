---
entity_id: "reaction.ecocyc.THIAZOLSYN3-RXN"
entity_type: "reaction"
name: "THIAZOLSYN3-RXN"
source_database: "EcoCyc"
source_id: "THIAZOLSYN3-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# THIAZOLSYN3-RXN

`reaction.ecocyc.THIAZOLSYN3-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:THIAZOLSYN3-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the third part of the multistep synthesis of the thiazole moiety of thiamin. EcoCyc reaction equation: ATP + THZ -> PROTON + ADP + THZ-P; direction=PHYSIOL-LEFT-TO-RIGHT. This is the third part of the multistep synthesis of the thiazole moiety of thiamin.

## Biological Role

Catalyzed by hydroxyethylthiazole kinase (complex.ecocyc.CPLX0-8211). Substrates: ATP (molecule.C00002), 5-(2-Hydroxyethyl)-4-methylthiazole (molecule.C04294). Products: ADP (molecule.C00008), H+ (molecule.C00080), 4-Methyl-5-(2-phosphooxyethyl)thiazole (molecule.C04327).

## Enriched Pathways

- `ecocyc.PWY-6897` thiamine diphosphate salvage II (EcoCyc)

## Annotation

This is the third part of the multistep synthesis of the thiazole moiety of thiamin.

## Pathways

- `ecocyc.PWY-6897` thiamine diphosphate salvage II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8211|complex.ecocyc.CPLX0-8211]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04327|molecule.C04327]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04294|molecule.C04294]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:THIAZOLSYN3-RXN`

## Notes

ATP + THZ -> PROTON + ADP + THZ-P; direction=PHYSIOL-LEFT-TO-RIGHT
