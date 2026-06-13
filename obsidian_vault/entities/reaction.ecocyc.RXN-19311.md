---
entity_id: "reaction.ecocyc.RXN-19311"
entity_type: "reaction"
name: "RXN-19311"
source_database: "EcoCyc"
source_id: "RXN-19311"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19311

`reaction.ecocyc.RXN-19311`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19311`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

2-ACYL-GPE + WATER -> Carboxylates + L-1-GLYCEROPHOSPHORYLETHANOL-AMINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 2-ACYL-GPE + WATER -> Carboxylates + L-1-GLYCEROPHOSPHORYLETHANOL-AMINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by outer membrane phospholipase A (complex.ecocyc.CPLX0-7944), pldB (protein.P07000). Substrates: H2O (molecule.C00001), 2-Acyl-sn-glycero-3-phosphoethanolamine (molecule.C05973). Products: H+ (molecule.C00080), sn-Glycero-3-phosphoethanolamine (molecule.C01233), a carboxylate (molecule.ecocyc.Carboxylates).

## Annotation

2-ACYL-GPE + WATER -> Carboxylates + L-1-GLYCEROPHOSPHORYLETHANOL-AMINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7944|complex.ecocyc.CPLX0-7944]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P07000|protein.P07000]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01233|molecule.C01233]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Carboxylates|molecule.ecocyc.Carboxylates]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05973|molecule.C05973]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19311`

## Notes

2-ACYL-GPE + WATER -> Carboxylates + L-1-GLYCEROPHOSPHORYLETHANOL-AMINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
