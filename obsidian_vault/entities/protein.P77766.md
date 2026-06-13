---
entity_id: "protein.P77766"
entity_type: "protein"
name: "rnm"
source_database: "UniProt"
source_id: "P77766"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rnm trpH yciV b1266 JW1258"
---

# rnm

`protein.P77766`

## Static

- Type: `protein`
- Source: `UniProt:P77766`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Exoribonuclease that catalyzes the last steps of 5S, 16S and 23S rRNA 5'-end maturation. Removes 3 nucleotides (nt) from the 5' end of 5S, 16S and 23S rRNA precursors to generate the mature 5' ends. Precursors with longer extensions are not processed (7 nt at the 5' end of pre-23S rRNA or 66 nt at the 5'-end of 16S rRNA are not processed). 5S and 23S rRNA maturation occurs more efficiently and accurately on ribosomal particles as compared to free RNA; the enzyme overdigests free RNA but generates the correct 5'-end in ribosomes from rnm deletion strains (PubMed:32343306). Efficiently catalyzes the hydrolysis of the 3'-phosphate from 3',5'-bis-phosphonucleotides as well as the successive hydrolysis of 5'-phosphomononucleotides from the 5'-end of short pieces of RNA and DNA, with no specificity toward the identity of the nucleotide base. Is more efficient at hydrolyzing RNA oligonucleotides than DNA oligonucleotides. This enzyme can also hydrolyze annealed DNA duplexes, albeit at a catalytic efficiency approximately 10-fold lower than that of the corresponding single-stranded oligonucleotides. {ECO:0000269|PubMed:25871919, ECO:0000269|PubMed:32343306}. RNase AM catalyzes the final maturation of the 5' ends of 5S, 16S and 23S rRNA...

## Biological Role

Catalyzes adenosine-3',5'-bisphosphate 3'-phosphohydrolase (reaction.R00188), RXN-16009 (reaction.ecocyc.RXN-16009), 5'-exoribonuclease (reaction.ecocyc.RXN-23862), RXN-24047 (reaction.ecocyc.RXN-24047). Bound by Mn2+ (molecule.ecocyc.MN_2).

## Annotation

FUNCTION: Exoribonuclease that catalyzes the last steps of 5S, 16S and 23S rRNA 5'-end maturation. Removes 3 nucleotides (nt) from the 5' end of 5S, 16S and 23S rRNA precursors to generate the mature 5' ends. Precursors with longer extensions are not processed (7 nt at the 5' end of pre-23S rRNA or 66 nt at the 5'-end of 16S rRNA are not processed). 5S and 23S rRNA maturation occurs more efficiently and accurately on ribosomal particles as compared to free RNA; the enzyme overdigests free RNA but generates the correct 5'-end in ribosomes from rnm deletion strains (PubMed:32343306). Efficiently catalyzes the hydrolysis of the 3'-phosphate from 3',5'-bis-phosphonucleotides as well as the successive hydrolysis of 5'-phosphomononucleotides from the 5'-end of short pieces of RNA and DNA, with no specificity toward the identity of the nucleotide base. Is more efficient at hydrolyzing RNA oligonucleotides than DNA oligonucleotides. This enzyme can also hydrolyze annealed DNA duplexes, albeit at a catalytic efficiency approximately 10-fold lower than that of the corresponding single-stranded oligonucleotides. {ECO:0000269|PubMed:25871919, ECO:0000269|PubMed:32343306}.

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.R00188|reaction.R00188]] `KEGG` `database` - via EC:3.1.3.97
- `catalyzes` --> [[reaction.ecocyc.RXN-16009|reaction.ecocyc.RXN-16009]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-23862|reaction.ecocyc.RXN-23862]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-24047|reaction.ecocyc.RXN-24047]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b1266|gene.b1266]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77766`
- `KEGG:ecj:JW1258;eco:b1266;ecoc:C3026_07420;`
- `GeneID:945857;`
- `GO:GO:0000166; GO:0000470; GO:0000481; GO:0004534; GO:0008252; GO:0030145; GO:0030490; GO:0035312; GO:0097657`
- `EC:3.1.13.-; 3.1.3.97`

## Notes

5'-3' exoribonuclease Rnm (EC 3.1.13.-) (3',5'-nucleotide bisphosphate phosphatase) (EC 3.1.3.97) (RNase AM)
