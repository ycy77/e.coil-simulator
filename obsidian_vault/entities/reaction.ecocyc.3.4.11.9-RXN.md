---
entity_id: "reaction.ecocyc.3.4.11.9-RXN"
entity_type: "reaction"
name: "3.4.11.9-RXN"
source_database: "EcoCyc"
source_id: "3.4.11.9-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Proline aminopeptidase"
  - "Aminopeptidase P"
  - "Aminoacylproline aminopeptidase"
---

# 3.4.11.9-RXN

`reaction.ecocyc.3.4.11.9-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.4.11.9-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is the hydrolysis of a peptide bond between the amino-terminal residue of a polypeptide and the following residue, as long as the following residue is proline. Hydrolysis of dipeptides is slower than hydrolysis of longer polypeptides. Dipeptides with proline followed by a hydrophobic residue competitively inhibit this reaction. EcoCyc reaction equation: Protein-With-N-Terminal-X-Pro + WATER -> Amino-Acids-20 + Protein-With-N-Terminal-Pro + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is the hydrolysis of a peptide bond between the amino-terminal residue of a polypeptide and the following residue, as long as the following residue is proline. Hydrolysis of dipeptides is slower than hydrolysis of longer polypeptides. Dipeptides with proline followed by a hydrophobic residue competitively inhibit this reaction.

## Biological Role

Catalyzed by Xaa-Pro aminopeptidase (complex.ecocyc.CPLX0-3081). Substrates: H2O (molecule.C00001). Products: H+ (molecule.C00080), a proteinogenic amino acid (molecule.ecocyc.Amino-Acids-20).

## Annotation

This reaction is the hydrolysis of a peptide bond between the amino-terminal residue of a polypeptide and the following residue, as long as the following residue is proline. Hydrolysis of dipeptides is slower than hydrolysis of longer polypeptides. Dipeptides with proline followed by a hydrophobic residue competitively inhibit this reaction.

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `activates` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-3081|complex.ecocyc.CPLX0-3081]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Amino-Acids-20|molecule.ecocyc.Amino-Acids-20]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3.4.11.9-RXN`

## Notes

Protein-With-N-Terminal-X-Pro + WATER -> Amino-Acids-20 + Protein-With-N-Terminal-Pro + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
