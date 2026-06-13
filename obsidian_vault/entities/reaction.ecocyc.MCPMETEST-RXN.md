---
entity_id: "reaction.ecocyc.MCPMETEST-RXN"
entity_type: "reaction"
name: "MCPMETEST-RXN"
source_database: "EcoCyc"
source_id: "MCPMETEST-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# MCPMETEST-RXN

`reaction.ecocyc.MCPMETEST-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:MCPMETEST-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Some examples of methyl-accepting chemotaxis proteins (MCPs) in E. coli are Tar, Tsr, Trg and Tap. EcoCyc reaction equation: WATER + protein-L-glutamate-O4-methyl-ester -> Protein-alpha-L-Glutamates + METOH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. Some examples of methyl-accepting chemotaxis proteins (MCPs) in E. coli are Tar, Tsr, Trg and Tap.

## Biological Role

Catalyzed by cheB (protein.P07330). Substrates: H2O (molecule.C00001), a [protein]-L-glutamate-O5-methyl-ester (molecule.ecocyc.protein-L-glutamate-O4-methyl-ester). Products: H+ (molecule.C00080), Methanol (molecule.C00132), a [protein]-α-L-glutamate (molecule.ecocyc.Protein-alpha-L-Glutamates).

## Annotation

Some examples of methyl-accepting chemotaxis proteins (MCPs) in E. coli are Tar, Tsr, Trg and Tap.

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P07330|protein.P07330]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00132|molecule.C00132]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Protein-alpha-L-Glutamates|molecule.ecocyc.Protein-alpha-L-Glutamates]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.protein-L-glutamate-O4-methyl-ester|molecule.ecocyc.protein-L-glutamate-O4-methyl-ester]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.Sulfhydryl-Reagents|molecule.ecocyc.Sulfhydryl-Reagents]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:MCPMETEST-RXN`

## Notes

WATER + protein-L-glutamate-O4-methyl-ester -> Protein-alpha-L-Glutamates + METOH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
