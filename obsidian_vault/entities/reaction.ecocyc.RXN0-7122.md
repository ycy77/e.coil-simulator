---
entity_id: "reaction.ecocyc.RXN0-7122"
entity_type: "reaction"
name: "RXN0-7122"
source_database: "EcoCyc"
source_id: "RXN0-7122"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7122

`reaction.ecocyc.RXN0-7122`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7122`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-ACYL-GPE + GLYCEROPHOSPHOGLYCEROL -> L-1-GLYCEROPHOSPHORYLETHANOL-AMINE + Lysophosphatidylglycerols; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 2-ACYL-GPE + GLYCEROPHOSPHOGLYCEROL -> L-1-GLYCEROPHOSPHORYLETHANOL-AMINE + Lysophosphatidylglycerols; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by pldB (protein.P07000). Substrates: 2-Acyl-sn-glycero-3-phosphoethanolamine (molecule.C05973), glycerophosphoglycerol (molecule.ecocyc.GLYCEROPHOSPHOGLYCEROL). Products: sn-Glycero-3-phosphoethanolamine (molecule.C01233), a lysophosphatidylglycerol (molecule.ecocyc.Lysophosphatidylglycerols).

## Annotation

2-ACYL-GPE + GLYCEROPHOSPHOGLYCEROL -> L-1-GLYCEROPHOSPHORYLETHANOL-AMINE + Lysophosphatidylglycerols; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P07000|protein.P07000]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C01233|molecule.C01233]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Lysophosphatidylglycerols|molecule.ecocyc.Lysophosphatidylglycerols]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C05973|molecule.C05973]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.GLYCEROPHOSPHOGLYCEROL|molecule.ecocyc.GLYCEROPHOSPHOGLYCEROL]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7122`

## Notes

2-ACYL-GPE + GLYCEROPHOSPHOGLYCEROL -> L-1-GLYCEROPHOSPHORYLETHANOL-AMINE + Lysophosphatidylglycerols; direction=PHYSIOL-LEFT-TO-RIGHT
