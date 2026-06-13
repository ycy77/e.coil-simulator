---
entity_id: "reaction.ecocyc.RXN0-5051"
entity_type: "reaction"
name: "RXN0-5051"
source_database: "EcoCyc"
source_id: "RXN0-5051"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5051

`reaction.ecocyc.RXN0-5051`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5051`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Exoaminopeptidase-Substrates + WATER -> Peptides-holder + Amino-Acids-20 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Exoaminopeptidase-Substrates + WATER -> Peptides-holder + Amino-Acids-20 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ypdE (protein.P77585). Substrates: H2O (molecule.C00001). Products: H+ (molecule.C00080), a proteinogenic amino acid (molecule.ecocyc.Amino-Acids-20).

## Annotation

Exoaminopeptidase-Substrates + WATER -> Peptides-holder + Amino-Acids-20 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P77585|protein.P77585]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Amino-Acids-20|molecule.ecocyc.Amino-Acids-20]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5051`

## Notes

Exoaminopeptidase-Substrates + WATER -> Peptides-holder + Amino-Acids-20 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
