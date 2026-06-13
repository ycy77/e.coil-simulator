---
entity_id: "reaction.ecocyc.3.4.11.1-RXN"
entity_type: "reaction"
name: "3.4.11.1-RXN"
source_database: "EcoCyc"
source_id: "3.4.11.1-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Cytosol aminopeptidase"
  - "Leucine aminopeptidase"
  - "Peptidase S"
---

# 3.4.11.1-RXN

`reaction.ecocyc.3.4.11.1-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.4.11.1-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is the hydrolysis of a peptide bond in a dipeptide. Substrates include cysteinylglycine. EcoCyc reaction equation: Protein-With-N-Terminal-X-Pro + WATER -> Amino-Acids-20 + Protein-With-N-Terminal-Pro + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is the hydrolysis of a peptide bond in a dipeptide. Substrates include cysteinylglycine.

## Biological Role

Catalyzed by aminopeptidase A/I and DNA-binding transcriptional repressor PepA (complex.ecocyc.CPLX0-3061). Substrates: H2O (molecule.C00001). Products: H+ (molecule.C00080), a proteinogenic amino acid (molecule.ecocyc.Amino-Acids-20).

## Annotation

This reaction is the hydrolysis of a peptide bond in a dipeptide. Substrates include cysteinylglycine.

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `activates` <-- [[molecule.C00288|molecule.C00288]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-3061|complex.ecocyc.CPLX0-3061]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Amino-Acids-20|molecule.ecocyc.Amino-Acids-20]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3.4.11.1-RXN`

## Notes

Protein-With-N-Terminal-X-Pro + WATER -> Amino-Acids-20 + Protein-With-N-Terminal-Pro + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
