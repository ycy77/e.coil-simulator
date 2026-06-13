---
entity_id: "reaction.ecocyc.RXN0-1661"
entity_type: "reaction"
name: "enterobactin hydrolase"
source_database: "EcoCyc"
source_id: "RXN0-1661"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# enterobactin hydrolase

`reaction.ecocyc.RXN0-1661`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-1661`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The products of the reaction include the monomer, dimer, and linearized trimer of 2,3-dihydroxybenzoylserine subunits. EcoCyc reaction equation: ENTEROBACTIN + WATER -> PROTON + N-23-DIHYDROXYBENZOYL-L-SERINE; direction=PHYSIOL-LEFT-TO-RIGHT. The products of the reaction include the monomer, dimer, and linearized trimer of 2,3-dihydroxybenzoylserine subunits.

## Biological Role

Catalyzed by fes (protein.P13039). Substrates: H2O (molecule.C00001), Enterochelin (molecule.C05821). Products: H+ (molecule.C00080), N-(2,3-dihydroxybenzoyl)-L-serine (molecule.ecocyc.N-23-DIHYDROXYBENZOYL-L-SERINE).

## Annotation

The products of the reaction include the monomer, dimer, and linearized trimer of 2,3-dihydroxybenzoylserine subunits.

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P13039|protein.P13039]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.N-23-DIHYDROXYBENZOYL-L-SERINE|molecule.ecocyc.N-23-DIHYDROXYBENZOYL-L-SERINE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05821|molecule.C05821]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-1661`

## Notes

ENTEROBACTIN + WATER -> PROTON + N-23-DIHYDROXYBENZOYL-L-SERINE; direction=PHYSIOL-LEFT-TO-RIGHT
