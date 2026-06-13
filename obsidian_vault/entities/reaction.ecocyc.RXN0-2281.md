---
entity_id: "reaction.ecocyc.RXN0-2281"
entity_type: "reaction"
name: "RXN0-2281"
source_database: "EcoCyc"
source_id: "RXN0-2281"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-2281

`reaction.ecocyc.RXN0-2281`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-2281`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The identity of the second product of this reaction is not known. EcoCyc reaction equation: SEPO3 + tRNA-Containing-5MeAminoMe-2-ThioU + GERANYL-PP + WATER -> Mnm5Se2U-containing-tRNAs + CPD-22373 + PPI + Pi; direction=PHYSIOL-LEFT-TO-RIGHT. The identity of the second product of this reaction is not known.

## Biological Role

Catalyzed by selU (protein.P33667). Substrates: H2O (molecule.C00001), Geranyl diphosphate (molecule.C00341), Selenophosphoric acid (molecule.C05172), a 5-[(methylamino)methyl]-2-thiouridine34 in tRNA (molecule.ecocyc.tRNA-Containing-5MeAminoMe-2-ThioU). Products: Diphosphate (molecule.C00013), (2E)-3,7-dimethylocta-2,6-diene-1-thiol (molecule.ecocyc.CPD-22373), a 5-methylaminomethyl-2-selenouridine34 in tRNA (molecule.ecocyc.Mnm5Se2U-containing-tRNAs), phosphate (molecule.ecocyc.Pi).

## Annotation

The identity of the second product of this reaction is not known.

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P33667|protein.P33667]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-22373|molecule.ecocyc.CPD-22373]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Mnm5Se2U-containing-tRNAs|molecule.ecocyc.Mnm5Se2U-containing-tRNAs]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00341|molecule.C00341]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05172|molecule.C05172]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.tRNA-Containing-5MeAminoMe-2-ThioU|molecule.ecocyc.tRNA-Containing-5MeAminoMe-2-ThioU]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-2281`

## Notes

SEPO3 + tRNA-Containing-5MeAminoMe-2-ThioU + GERANYL-PP + WATER -> Mnm5Se2U-containing-tRNAs + CPD-22373 + PPI + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
