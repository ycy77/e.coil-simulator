---
entity_id: "reaction.ecocyc.RXN0-7023"
entity_type: "reaction"
name: "RXN0-7023"
source_database: "EcoCyc"
source_id: "RXN0-7023"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7023

`reaction.ecocyc.RXN0-7023`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7023`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

RNASE-R-DEGRADATION-SUBSTRATE-RNA + WATER -> Nucleoside-Monophosphates + Diribonucleotide; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: RNASE-R-DEGRADATION-SUBSTRATE-RNA + WATER -> Nucleoside-Monophosphates + Diribonucleotide; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rnr (protein.P21499). Substrates: H2O (molecule.C00001). Products: a diribonucleotide (molecule.ecocyc.Diribonucleotide), a nucleoside 5'-monophosphate (molecule.ecocyc.Nucleoside-Monophosphates).

## Annotation

RNASE-R-DEGRADATION-SUBSTRATE-RNA + WATER -> Nucleoside-Monophosphates + Diribonucleotide; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `activates` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P21499|protein.P21499]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Diribonucleotide|molecule.ecocyc.Diribonucleotide]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Nucleoside-Monophosphates|molecule.ecocyc.Nucleoside-Monophosphates]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7023`

## Notes

RNASE-R-DEGRADATION-SUBSTRATE-RNA + WATER -> Nucleoside-Monophosphates + Diribonucleotide; direction=PHYSIOL-LEFT-TO-RIGHT
