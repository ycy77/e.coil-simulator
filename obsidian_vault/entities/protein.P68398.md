---
entity_id: "protein.P68398"
entity_type: "protein"
name: "tadA"
source_database: "UniProt"
source_id: "P68398"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tadA yfhC b2559 JW2543"
---

# tadA

`protein.P68398`

## Static

- Type: `protein`
- Source: `UniProt:P68398`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the deamination of adenosine to inosine at the wobble position 34 of tRNA(Arg2). Essential for cell viability. {ECO:0000255|HAMAP-Rule:MF_00972, ECO:0000269|PubMed:12110595, ECO:0000269|PubMed:16700551}. tRNA adenosine34 deaminase (TadA) belongs to the family of adenosine deaminases of tRNA (ADATs). It catalyzes deamination of adenosine to inosine at position 34, the wobble base of the anticodon loop, of tRNAArg2. Substrate requirements have been evaluated; the anticodon stem and loop are found to be sufficient for inosine formation . Surprisingly, a small number of mRNAs are also targets for A-to-I editing in E. coli, and TadA was identified as the responsible enzyme. One of the edited mRNAs is G0-9610 hokB, which encodes a small toxic protein. Because inosine is recognized as guanine by the translation machinery, editing of hokB mRNA changes a tyrosine (TAC) codon into a cysteine (TGC) codon at position 29. The predicted secondary structure of the hokB mRNA resembles that of an anticodon stem-loop, with the edited nucleotide positioned in the loop . TadA forms a homodimer . A crystal structure of TadA has been solved at 2.0 Å resolution . The transition state structure of TadA was investigated using kinetic isotope effects . The tadA gene is essential...

## Biological Role

Catalyzes tRNA(adenine34) aminohydrolase (reaction.R10223). Component of tRNA adenosine34 deaminase (complex.ecocyc.CPLX0-901).

## Annotation

FUNCTION: Catalyzes the deamination of adenosine to inosine at the wobble position 34 of tRNA(Arg2). Essential for cell viability. {ECO:0000255|HAMAP-Rule:MF_00972, ECO:0000269|PubMed:12110595, ECO:0000269|PubMed:16700551}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R10223|reaction.R10223]] `KEGG` `database` - via EC:3.5.4.33
- `is_component_of` --> [[complex.ecocyc.CPLX0-901|complex.ecocyc.CPLX0-901]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2559|gene.b2559]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P68398`
- `KEGG:ecj:JW2543;eco:b2559;ecoc:C3026_14165;`
- `GeneID:75206252;947027;`
- `GO:GO:0002100; GO:0006382; GO:0008270; GO:0042803; GO:0052717`
- `EC:3.5.4.33`

## Notes

tRNA-specific adenosine deaminase (EC 3.5.4.33)
