---
entity_id: "protein.P08312"
entity_type: "protein"
name: "pheS"
source_database: "UniProt"
source_id: "P08312"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pheS b1714 JW5277"
---

# pheS

`protein.P08312`

## Static

- Type: `protein`
- Source: `UniProt:P08312`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

Phenylalanine--tRNA ligase alpha subunit (EC 6.1.1.20) (Phenylalanyl-tRNA synthetase alpha subunit) (PheRS) The α subunit of PheRS (also called PheTS) contains the phenylalanine binding site within the conserved motif 2 and motif 3 of the protein . It interacts with the 3'-adenosine of tRNAPhe . Isolated α subunits exist primarily as dimers . The pheS5 mutant allele (leading to a G98D change in amino acid sequence) causes temperature-sensitive PheRS activity . Intragenic supressors of the pheS5 mutation have been isolated and analyzed . The temperature-sensitive fitA76 and fit95 mutants related to pheS and pheT, respectively, have been genetically characterized . There is a general discrepancy between kcat values of aminoacyl-tRNA synthetases that were measured in vitro and values that were calculated as needed to support measured growth rates . Modeling of these parameters in E. coli has found that the required kcat values are on average 7.6-fold higher than those measured in vitro . Reviews:

## Biological Role

Catalyzes L-phenylalanine:tRNA(Ala) ligase (AMP-forming) (reaction.R03660). Component of phenylalanine—tRNA ligase (complex.ecocyc.PHES-CPLX).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

Phenylalanine--tRNA ligase alpha subunit (EC 6.1.1.20) (Phenylalanyl-tRNA synthetase alpha subunit) (PheRS)

## Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R03660|reaction.R03660]] `KEGG` `database` - via EC:6.1.1.20
- `is_component_of` --> [[complex.ecocyc.PHES-CPLX|complex.ecocyc.PHES-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1714|gene.b1714]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P08312`
- `KEGG:ecj:JW5277;eco:b1714;ecoc:C3026_09810;`
- `GeneID:75205640;946223;`
- `GO:GO:0000049; GO:0000287; GO:0004826; GO:0005524; GO:0005737; GO:0005829; GO:0006432; GO:0009328`
- `EC:6.1.1.20`

## Notes

Phenylalanine--tRNA ligase alpha subunit (EC 6.1.1.20) (Phenylalanyl-tRNA synthetase alpha subunit) (PheRS)
