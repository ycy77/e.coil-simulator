---
entity_id: "reaction.ecocyc.RXN0-1061"
entity_type: "reaction"
name: "RXN0-1061"
source_database: "EcoCyc"
source_id: "RXN0-1061"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-1061

`reaction.ecocyc.RXN0-1061`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-1061`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Unfolded-Proteins + ATP + WATER -> General-Protein-Substrates + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Unfolded-Proteins + ATP + WATER -> General-Protein-Substrates + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by chaperone protein HtpG (complex.ecocyc.CPLX0-2641), regulatory ATPase RavA (complex.ecocyc.CPLX0-3927), GroEL-GroES chaperonin complex (complex.ecocyc.CPLX0-3934), dnaK (protein.P0A6Y8). Substrates: H2O (molecule.C00001), ATP (molecule.C00002). Products: ADP (molecule.C00008), H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi).

## Annotation

Unfolded-Proteins + ATP + WATER -> General-Protein-Substrates + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-2641|complex.ecocyc.CPLX0-2641]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-3927|complex.ecocyc.CPLX0-3927]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-3934|complex.ecocyc.CPLX0-3934]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0A6Y8|protein.P0A6Y8]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-1061`

## Notes

Unfolded-Proteins + ATP + WATER -> General-Protein-Substrates + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
