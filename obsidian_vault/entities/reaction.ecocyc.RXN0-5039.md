---
entity_id: "reaction.ecocyc.RXN0-5039"
entity_type: "reaction"
name: "RXN0-5039"
source_database: "EcoCyc"
source_id: "RXN0-5039"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5039

`reaction.ecocyc.RXN0-5039`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5039`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is the 5' to 3' exonucleolytic cleavage of DNA to yield 5'-mononucleotides. EcoCyc reaction equation: Double-Stranded-DNAs + WATER -> Single-Stranded-DNAs + 5-Phosphomononucleotides; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is the 5' to 3' exonucleolytic cleavage of DNA to yield 5'-mononucleotides.

## Biological Role

Catalyzed by polA (protein.P00582), recE (protein.P15032). Substrates: H2O (molecule.C00001). Products: a 5'-phosphomononucleotide (molecule.ecocyc.5-Phosphomononucleotides).

## Annotation

This reaction is the 5' to 3' exonucleolytic cleavage of DNA to yield 5'-mononucleotides.

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P00582|protein.P00582]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P15032|protein.P15032]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.5-Phosphomononucleotides|molecule.ecocyc.5-Phosphomononucleotides]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5039`

## Notes

Double-Stranded-DNAs + WATER -> Single-Stranded-DNAs + 5-Phosphomononucleotides; direction=PHYSIOL-LEFT-TO-RIGHT
