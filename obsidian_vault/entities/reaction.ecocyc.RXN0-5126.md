---
entity_id: "reaction.ecocyc.RXN0-5126"
entity_type: "reaction"
name: "RXN0-5126"
source_database: "EcoCyc"
source_id: "RXN0-5126"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5126

`reaction.ecocyc.RXN0-5126`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5126`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Four conserved aspartic residues, Asp-129, 131, 215 and 217 of WaaR are important for its catalytic function . EcoCyc reaction equation: CPD-12575 + CPD0-937 -> PROTON + CPD0-938 + UDP; direction=PHYSIOL-LEFT-TO-RIGHT. Four conserved aspartic residues, Asp-129, 131, 215 and 217 of WaaR are important for its catalytic function .

## Biological Role

Catalyzed by waaJ (protein.P27129). Substrates: UDP-glucose (molecule.C00029), galactosyl-(glucosyl)2-(heptosyl)3-Kdo2-lipid A-bisphosphate (E. coli) (molecule.ecocyc.CPD0-937). Products: UDP (molecule.C00015), H+ (molecule.C00080), galactosyl-(glucosyl)3-(heptosyl)3-Kdo2-lipid A-bisphosphate (E. coli) (molecule.ecocyc.CPD0-938).

## Enriched Pathways

- `ecocyc.LIPA-CORESYN-PWY` lipid A-core biosynthesis (E. coli K-12) (EcoCyc)

## Annotation

Four conserved aspartic residues, Asp-129, 131, 215 and 217 of WaaR are important for its catalytic function .

## Pathways

- `ecocyc.LIPA-CORESYN-PWY` lipid A-core biosynthesis (E. coli K-12) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P27129|protein.P27129]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00015|molecule.C00015]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-938|molecule.ecocyc.CPD0-938]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00029|molecule.C00029]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-937|molecule.ecocyc.CPD0-937]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5126`

## Notes

CPD-12575 + CPD0-937 -> PROTON + CPD0-938 + UDP; direction=PHYSIOL-LEFT-TO-RIGHT
