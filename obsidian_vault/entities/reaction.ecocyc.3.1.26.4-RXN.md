---
entity_id: "reaction.ecocyc.3.1.26.4-RXN"
entity_type: "reaction"
name: "3.1.26.4-RXN"
source_database: "EcoCyc"
source_id: "3.1.26.4-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Endoribonuclease H"
---

# 3.1.26.4-RXN

`reaction.ecocyc.3.1.26.4-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.1.26.4-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is the endonucleolytic cleavage of RNA in an RNA-DNA hybrid to yield a 5'-phosphomonoester. EcoCyc reaction equation: RNA-DNA-hybrids + WATER -> ssDNA-Holder + Ribonucleoside-Monophosphates; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is the endonucleolytic cleavage of RNA in an RNA-DNA hybrid to yield a 5'-phosphomonoester.

## Biological Role

Catalyzed by rnhA (protein.P0A7Y4), rnhB (protein.P10442). Substrates: H2O (molecule.C00001). Products: a ribonucleoside 5'-monophosphate (molecule.ecocyc.Ribonucleoside-Monophosphates), a single-stranded DNA (molecule.ecocyc.ssDNA-Holder).

## Annotation

This reaction is the endonucleolytic cleavage of RNA in an RNA-DNA hybrid to yield a 5'-phosphomonoester.

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P0A7Y4|protein.P0A7Y4]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P10442|protein.P10442]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Ribonucleoside-Monophosphates|molecule.ecocyc.Ribonucleoside-Monophosphates]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.ssDNA-Holder|molecule.ecocyc.ssDNA-Holder]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.N-ETHYLMALEIMIDE|molecule.ecocyc.N-ETHYLMALEIMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:3.1.26.4-RXN`

## Notes

RNA-DNA-hybrids + WATER -> ssDNA-Holder + Ribonucleoside-Monophosphates; direction=PHYSIOL-LEFT-TO-RIGHT
