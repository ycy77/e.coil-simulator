---
entity_id: "reaction.ecocyc.RXN0-5052"
entity_type: "reaction"
name: "RXN0-5052"
source_database: "EcoCyc"
source_id: "RXN0-5052"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5052

`reaction.ecocyc.RXN0-5052`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5052`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Aminopeptidase-Substrates + WATER -> Amino-Acids-20 + Peptide-Holder-Alternative; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Aminopeptidase-Substrates + WATER -> Amino-Acids-20 + Peptide-Holder-Alternative; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by aminopeptidase YpdF (complex.ecocyc.CPLX0-8290), mtfA (protein.P76346). Substrates: H2O (molecule.C00001). Products: a proteinogenic amino acid (molecule.ecocyc.Amino-Acids-20).

## Annotation

Aminopeptidase-Substrates + WATER -> Amino-Acids-20 + Peptide-Holder-Alternative; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8290|complex.ecocyc.CPLX0-8290]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P76346|protein.P76346]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Amino-Acids-20|molecule.ecocyc.Amino-Acids-20]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5052`

## Notes

Aminopeptidase-Substrates + WATER -> Amino-Acids-20 + Peptide-Holder-Alternative; direction=PHYSIOL-LEFT-TO-RIGHT
