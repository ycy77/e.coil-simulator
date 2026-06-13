---
entity_id: "protein.P07395"
entity_type: "protein"
name: "pheT"
source_database: "UniProt"
source_id: "P07395"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pheT b1713 JW1703"
---

# pheT

`protein.P07395`

## Static

- Type: `protein`
- Source: `UniProt:P07395`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

Phenylalanine--tRNA ligase beta subunit (EC 6.1.1.20) (Phenylalanyl-tRNA synthetase beta subunit) (PheRS) The β subunit of PheRS (also called PheST) contains the Phe-tRNAPhe binding site . The editing site of the enzyme localizes to the B3/B4 domain of the β subunit . Amino acid residues involved in the editing activity have been identified . The B2 OB-fold domain is not essential for catalytic activity, but may play a role as a secondary tRNA binding site in post-transfer editing . Isolated β subunits exist primarily as monomers . A Glu571Lys mutant (pheT36) is temperature-sensitive . The temperature-sensitive fitA76 and fit95 mutants related to pheS and pheT, respectively, have been genetically characterized . Reviews:

## Biological Role

Catalyzes L-phenylalanine:tRNA(Ala) ligase (AMP-forming) (reaction.R03660). Component of phenylalanine—tRNA ligase (complex.ecocyc.PHES-CPLX).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

Phenylalanine--tRNA ligase beta subunit (EC 6.1.1.20) (Phenylalanyl-tRNA synthetase beta subunit) (PheRS)

## Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R03660|reaction.R03660]] `KEGG` `database` - via EC:6.1.1.20
- `is_component_of` --> [[complex.ecocyc.PHES-CPLX|complex.ecocyc.PHES-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1713|gene.b1713]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P07395`
- `KEGG:ecj:JW1703;eco:b1713;ecoc:C3026_09805;`
- `GeneID:945382;`
- `GO:GO:0000049; GO:0000287; GO:0004826; GO:0005524; GO:0005829; GO:0006432; GO:0009328; GO:0016020; GO:0042802`
- `EC:6.1.1.20`

## Notes

Phenylalanine--tRNA ligase beta subunit (EC 6.1.1.20) (Phenylalanyl-tRNA synthetase beta subunit) (PheRS)
