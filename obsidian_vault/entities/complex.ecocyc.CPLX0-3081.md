---
entity_id: "complex.ecocyc.CPLX0-3081"
entity_type: "complex"
name: "Xaa-Pro aminopeptidase"
source_database: "EcoCyc"
source_id: "CPLX0-3081"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# Xaa-Pro aminopeptidase

`complex.ecocyc.CPLX0-3081`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3081`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P15034|protein.P15034]]

## Enriched Summary

Aminopeptidase P is an exopeptidase that cleaves the amino-terminal residue from polypeptides, as long as the following residue is a proline . Aminopeptidase P comprises four PepP monomers, arranged as a dimer of dimers . Kinetic and structural analysis of PepP has identified residues comprising the active site as well as parts of its structure that are required for substrate specificity . The enzyme was initially purified and characterized from E. coli B . Fluorogenic assay substrates have been described . Recombinant enzyme has also been purified from cell extracts of E. coli strain HB101 . Strain HB101 is a hybrid K-12/B strain . Using recombinant aminopeptidase P purified from extracts of the E. coli K-12 strain JM83, kinetic analysis using peptides of different lengths revealed several subsites on the enzyme that interact with substrates, two of which are highly stereospecific for L-amino acids . The enzyme is also capable of hydrolyzing toxic organophosphorus compounds . Potent inhibitors of aminopeptidase P have been synthesized . A number of crystal structures of the enzyme have been solved at varying resolutions, including: the native enzyme at 1...

## Biological Role

Catalyzes 3.4.11.9-RXN (reaction.ecocyc.3.4.11.9-RXN). Bound by Mn2+ (molecule.ecocyc.MN_2).

## Annotation

Aminopeptidase P is an exopeptidase that cleaves the amino-terminal residue from polypeptides, as long as the following residue is a proline . Aminopeptidase P comprises four PepP monomers, arranged as a dimer of dimers . Kinetic and structural analysis of PepP has identified residues comprising the active site as well as parts of its structure that are required for substrate specificity . The enzyme was initially purified and characterized from E. coli B . Fluorogenic assay substrates have been described . Recombinant enzyme has also been purified from cell extracts of E. coli strain HB101 . Strain HB101 is a hybrid K-12/B strain . Using recombinant aminopeptidase P purified from extracts of the E. coli K-12 strain JM83, kinetic analysis using peptides of different lengths revealed several subsites on the enzyme that interact with substrates, two of which are highly stereospecific for L-amino acids . The enzyme is also capable of hydrolyzing toxic organophosphorus compounds . Potent inhibitors of aminopeptidase P have been synthesized . A number of crystal structures of the enzyme have been solved at varying resolutions, including: the native enzyme at 1.90 Å resolution (PDB 1WL9) and an orthorhombic crystal form ; a low pH inactive form ; an apo form, and forms with various metal ion substitutions ; the enzyme in complex with bound inhibitors and bound substrate ; several alanine substitution mutants , and three of these mutants in complex with substrate or product . Each subunit of the tetramer has a catalytic site centered on a dinuclear Mn(II) cluster. Significant activity is seen only in the manganese-bound form of the enzyme . Site-directed alanine substitution mutagenesis of conserved active site residues showed that His243 and His361 are required for catalysis

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.3.4.11.9-RXN|reaction.ecocyc.3.4.11.9-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P15034|protein.P15034]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-3081`
- `QSPROTEOME:QS00191631`

## Notes

4*protein.P15034
