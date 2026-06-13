---
entity_id: "reaction.ecocyc.RXN0-5330"
entity_type: "reaction"
name: "RXN0-5330"
source_database: "EcoCyc"
source_id: "RXN0-5330"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5330

`reaction.ecocyc.RXN0-5330`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5330`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

A reaction in the electron transport chain of E. coli. EcoCyc reaction equation: Ubiquinones + PROTON + NADH -> Ubiquinols + NAD; direction=PHYSIOL-LEFT-TO-RIGHT. A reaction in the electron transport chain of E. coli.

## Biological Role

Catalyzed by ndh (protein.P00393). Substrates: NADH (molecule.C00004), H+ (molecule.C00080), a ubiquinone (molecule.ecocyc.Ubiquinones). Products: NAD+ (molecule.C00003), Ubiquinol (molecule.C00390).

## Enriched Pathways

- `ecocyc.PWY0-1567` NADH to cytochrome bo oxidase electron transfer II (EcoCyc)
- `ecocyc.PWY0-1568` NADH to cytochrome bd oxidase electron transfer II (EcoCyc)
- `ecocyc.PWY0-1573` nitrate reduction VIIIb (dissimilatory) (EcoCyc)

## Annotation

A reaction in the electron transport chain of E. coli.

## Pathways

- `ecocyc.PWY0-1567` NADH to cytochrome bo oxidase electron transfer II (EcoCyc)
- `ecocyc.PWY0-1568` NADH to cytochrome bd oxidase electron transfer II (EcoCyc)
- `ecocyc.PWY0-1573` nitrate reduction VIIIb (dissimilatory) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P00393|protein.P00393]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00390|molecule.C00390]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Ubiquinones|molecule.ecocyc.Ubiquinones]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5330`

## Notes

Ubiquinones + PROTON + NADH -> Ubiquinols + NAD; direction=PHYSIOL-LEFT-TO-RIGHT
