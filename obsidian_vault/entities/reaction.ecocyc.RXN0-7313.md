---
entity_id: "reaction.ecocyc.RXN0-7313"
entity_type: "reaction"
name: "RXN0-7313"
source_database: "EcoCyc"
source_id: "RXN0-7313"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7313

`reaction.ecocyc.RXN0-7313`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7313`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

FE+2 + N-23-DIHYDROXYBENZOYL-L-SERINE + NADP -> CPD-17082 + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: FE+2 + N-23-DIHYDROXYBENZOYL-L-SERINE + NADP -> CPD-17082 + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by yqjH (protein.Q46871). Substrates: NADP+ (molecule.C00006), Fe2+ (molecule.C14818), N-(2,3-dihydroxybenzoyl)-L-serine (molecule.ecocyc.N-23-DIHYDROXYBENZOYL-L-SERINE). Products: NADPH (molecule.C00005), H+ (molecule.C00080), iron(III)-[N-(2,3-dihydroxybenzoyl)-L-serine] complex (molecule.ecocyc.CPD-17082).

## Annotation

FE+2 + N-23-DIHYDROXYBENZOYL-L-SERINE + NADP -> CPD-17082 + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.Q46871|protein.Q46871]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-17082|molecule.ecocyc.CPD-17082]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.N-23-DIHYDROXYBENZOYL-L-SERINE|molecule.ecocyc.N-23-DIHYDROXYBENZOYL-L-SERINE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7313`

## Notes

FE+2 + N-23-DIHYDROXYBENZOYL-L-SERINE + NADP -> CPD-17082 + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
