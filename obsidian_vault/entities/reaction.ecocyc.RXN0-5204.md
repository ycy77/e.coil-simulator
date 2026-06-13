---
entity_id: "reaction.ecocyc.RXN0-5204"
entity_type: "reaction"
name: "RXN0-5204"
source_database: "EcoCyc"
source_id: "RXN0-5204"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5204

`reaction.ecocyc.RXN0-5204`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5204`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PepB-Aminopeptidase-Substrates + WATER -> Amino-Acids-20 + Peptide-Holder-Alternative; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PepB-Aminopeptidase-Substrates + WATER -> Amino-Acids-20 + Peptide-Holder-Alternative; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by aminopeptidase B (complex.ecocyc.CPLX0-8122). Substrates: H2O (molecule.C00001). Products: a proteinogenic amino acid (molecule.ecocyc.Amino-Acids-20).

## Annotation

PepB-Aminopeptidase-Substrates + WATER -> Amino-Acids-20 + Peptide-Holder-Alternative; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8122|complex.ecocyc.CPLX0-8122]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Amino-Acids-20|molecule.ecocyc.Amino-Acids-20]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.O-PHENANTHROLINE|molecule.ecocyc.O-PHENANTHROLINE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-5204`

## Notes

PepB-Aminopeptidase-Substrates + WATER -> Amino-Acids-20 + Peptide-Holder-Alternative; direction=PHYSIOL-LEFT-TO-RIGHT
