---
entity_id: "reaction.ecocyc.RXN0-301"
entity_type: "reaction"
name: "RXN0-301"
source_database: "EcoCyc"
source_id: "RXN0-301"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-301

`reaction.ecocyc.RXN0-301`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-301`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

OXYGEN-MOLECULE + WATER + N-METHYLTRYPTOPHAN -> TRP + HYDROGEN-PEROXIDE + FORMALDEHYDE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: OXYGEN-MOLECULE + WATER + N-METHYLTRYPTOPHAN -> TRP + HYDROGEN-PEROXIDE + FORMALDEHYDE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by solA (protein.P40874). Substrates: H2O (molecule.C00001), Oxygen (molecule.C00007), N-methyl-L-tryptophan (molecule.ecocyc.N-METHYLTRYPTOPHAN). Products: Hydrogen peroxide (molecule.C00027), Formaldehyde (molecule.C00067), L-Tryptophan (molecule.C00078).

## Annotation

OXYGEN-MOLECULE + WATER + N-METHYLTRYPTOPHAN -> TRP + HYDROGEN-PEROXIDE + FORMALDEHYDE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P40874|protein.P40874]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00027|molecule.C00027]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00067|molecule.C00067]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00078|molecule.C00078]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.N-METHYLTRYPTOPHAN|molecule.ecocyc.N-METHYLTRYPTOPHAN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00180|molecule.C00180]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1380|molecule.ecocyc.CPD0-1380]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-301`

## Notes

OXYGEN-MOLECULE + WATER + N-METHYLTRYPTOPHAN -> TRP + HYDROGEN-PEROXIDE + FORMALDEHYDE; direction=PHYSIOL-LEFT-TO-RIGHT
