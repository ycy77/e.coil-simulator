---
entity_id: "protein.P30014"
entity_type: "protein"
name: "rnt"
source_database: "UniProt"
source_id: "P30014"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rnt b1652 JW1644"
---

# rnt

`protein.P30014`

## Static

- Type: `protein`
- Source: `UniProt:P30014`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Trims short 3' overhangs of a variety of RNA species, leaving a one or two nucleotide 3' overhang. Responsible for the end-turnover of tRNA: specifically removes the terminal AMP residue from uncharged tRNA (tRNA-C-C-A). Also appears to be involved in tRNA biosynthesis, especially in strains lacking other exoribonucleases. {ECO:0000255|HAMAP-Rule:MF_00157, ECO:0000269|PubMed:12364334, ECO:0000269|PubMed:17437714, ECO:0000269|PubMed:21317904}.; FUNCTION: A general regulator of small RNAs (sRNA), contributes to their degradation. Upon overexpression suppresses sRNA-mediated RhyB-silencing of multiple RNA targets; overexpression leads to nearly complete loss of RhyB sRNA. {ECO:0000269|PubMed:34210798}.

## Biological Role

Component of ribonuclease T (complex.ecocyc.CPLX0-3602).

## Annotation

FUNCTION: Trims short 3' overhangs of a variety of RNA species, leaving a one or two nucleotide 3' overhang. Responsible for the end-turnover of tRNA: specifically removes the terminal AMP residue from uncharged tRNA (tRNA-C-C-A). Also appears to be involved in tRNA biosynthesis, especially in strains lacking other exoribonucleases. {ECO:0000255|HAMAP-Rule:MF_00157, ECO:0000269|PubMed:12364334, ECO:0000269|PubMed:17437714, ECO:0000269|PubMed:21317904}.; FUNCTION: A general regulator of small RNAs (sRNA), contributes to their degradation. Upon overexpression suppresses sRNA-mediated RhyB-silencing of multiple RNA targets; overexpression leads to nearly complete loss of RhyB sRNA. {ECO:0000269|PubMed:34210798}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3602|complex.ecocyc.CPLX0-3602]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1652|gene.b1652]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P30014`
- `KEGG:ecj:JW1644;eco:b1652;ecoc:C3026_09480;`
- `GeneID:946159;`
- `GO:GO:0000175; GO:0000287; GO:0003676; GO:0005829; GO:0006974; GO:0008310; GO:0008408; GO:0031125; GO:0034644; GO:0042780; GO:0042802; GO:0042803; GO:0043628; GO:0045004`
- `EC:3.1.13.-`

## Notes

Ribonuclease T (EC 3.1.13.-) (Exoribonuclease T) (RNase T)
