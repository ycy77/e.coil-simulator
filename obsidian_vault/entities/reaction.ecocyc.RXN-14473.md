---
entity_id: "reaction.ecocyc.RXN-14473"
entity_type: "reaction"
name: "RXN-14473"
source_database: "EcoCyc"
source_id: "RXN-14473"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14473

`reaction.ecocyc.RXN-14473`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14473`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

Nucleoside-Monophosphates + WATER -> Nucleosides + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Nucleoside-Monophosphates + WATER -> Nucleosides + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by acid phosphatase / phosphotransferase (complex.ecocyc.APHA-CPLX). Substrates: H2O (molecule.C00001), a nucleoside 5'-monophosphate (molecule.ecocyc.Nucleoside-Monophosphates). Products: a nucleoside (molecule.ecocyc.Nucleosides), phosphate (molecule.ecocyc.Pi).

## Annotation

Nucleoside-Monophosphates + WATER -> Nucleosides + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.APHA-CPLX|complex.ecocyc.APHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Nucleosides|molecule.ecocyc.Nucleosides]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Nucleoside-Monophosphates|molecule.ecocyc.Nucleoside-Monophosphates]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14473`

## Notes

Nucleoside-Monophosphates + WATER -> Nucleosides + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
