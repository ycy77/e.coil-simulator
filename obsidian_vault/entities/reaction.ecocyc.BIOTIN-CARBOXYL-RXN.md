---
entity_id: "reaction.ecocyc.BIOTIN-CARBOXYL-RXN"
entity_type: "reaction"
name: "BIOTIN-CARBOXYL-RXN"
source_database: "EcoCyc"
source_id: "BIOTIN-CARBOXYL-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# BIOTIN-CARBOXYL-RXN

`reaction.ecocyc.BIOTIN-CARBOXYL-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:BIOTIN-CARBOXYL-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is a subreaction of the overall acetyl-CoA carboxylase reaction, which is the first committed step in fatty acid synthesis. EcoCyc reaction equation: biotin-L-lysine-in-BCCP-dimers + HCO3 + ATP -> Pi + carboxybiotin-L-lysine-in-BCCP-dimers + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. This is a subreaction of the overall acetyl-CoA carboxylase reaction, which is the first committed step in fatty acid synthesis.

## Biological Role

Catalyzed by biotin carboxylase (complex.ecocyc.BIOTIN-CARBOXYL-CPLX). Substrates: ATP (molecule.C00002), HCO3- (molecule.C00288), a [biotin carboxyl-carrier-protein dimer]-N6-biotinyl-L-lysine (molecule.ecocyc.biotin-L-lysine-in-BCCP-dimers). Products: ADP (molecule.C00008), H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi), a [carboxyl-carrier protein dimer]-N6-carboxybiotinyl-L-lysine (molecule.ecocyc.carboxybiotin-L-lysine-in-BCCP-dimers).

## Enriched Pathways

- `ecocyc.PWY0-1264` malonyl-CoA biosynthesis via biotin-carboxyl carrier protein (EcoCyc)

## Annotation

This is a subreaction of the overall acetyl-CoA carboxylase reaction, which is the first committed step in fatty acid synthesis.

## Pathways

- `ecocyc.PWY0-1264` malonyl-CoA biosynthesis via biotin-carboxyl carrier protein (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[complex.ecocyc.BIOTIN-CARBOXYL-CPLX|complex.ecocyc.BIOTIN-CARBOXYL-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.carboxybiotin-L-lysine-in-BCCP-dimers|molecule.ecocyc.carboxybiotin-L-lysine-in-BCCP-dimers]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00288|molecule.C00288]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.biotin-L-lysine-in-BCCP-dimers|molecule.ecocyc.biotin-L-lysine-in-BCCP-dimers]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00120|molecule.C00120]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C05682|molecule.C05682]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:BIOTIN-CARBOXYL-RXN`

## Notes

biotin-L-lysine-in-BCCP-dimers + HCO3 + ATP -> Pi + carboxybiotin-L-lysine-in-BCCP-dimers + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
