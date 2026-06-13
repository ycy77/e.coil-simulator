---
entity_id: "protein.P22333"
entity_type: "protein"
name: "add"
source_database: "UniProt"
source_id: "P22333"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "add b1623 JW1615"
---

# add

`protein.P22333`

## Static

- Type: `protein`
- Source: `UniProt:P22333`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the hydrolytic deamination of adenosine and 2-deoxyadenosine. {ECO:0000255|HAMAP-Rule:MF_00540, ECO:0000269|PubMed:357905}. Adenosine deaminase participates in pathways for the degradation and salvage of purine ribonucleotides and deoxyribonucleotides. The salvage pathways can convert adenine, adenosine and deoxyadenosine to guanine nucleotides (see pathways PWY0-1296, PWY0-1297, PWY-6605, PWY-6609 and PWY-6611). This enzyme is one of two adenosine deaminases in E. coli, the other is TadA, CPLX0-901. The enzyme was shown to be induced in E. coli B by the presence of adenine or hypoxanthine in the culture medium . The native apparent molecular mass of the enzyme from E. coli K-12 was determined to be 29 kDa by gel filtration chromatography, using either purified enzyme, or enzyme from crude extracts . E. coli adenosine deaminase shares approximately 33% amino acid sequence identity and 50% overall homology with mammalian adenosine deaminases, suggesting structural and functional similarity . Murine adenosine deaminase is a monomeric enzyme that requires Zn2+ as a cofactor. Its crystal structure has been determined .

## Biological Role

Catalyzes ADDALT-RXN (reaction.ecocyc.ADDALT-RXN), ADENODEAMIN-RXN (reaction.ecocyc.ADENODEAMIN-RXN).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the hydrolytic deamination of adenosine and 2-deoxyadenosine. {ECO:0000255|HAMAP-Rule:MF_00540, ECO:0000269|PubMed:357905}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.ADDALT-RXN|reaction.ecocyc.ADDALT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.ADENODEAMIN-RXN|reaction.ecocyc.ADENODEAMIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1623|gene.b1623]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P22333`
- `KEGG:ecj:JW1615;eco:b1623;ecoc:C3026_09330;`
- `GeneID:75171683;75204467;945851;`
- `GO:GO:0004000; GO:0005829; GO:0006154; GO:0006974; GO:0008270; GO:0009168; GO:0015950; GO:0032261; GO:0043103; GO:0046101; GO:0046103; GO:0046936`
- `EC:3.5.4.4`

## Notes

Adenosine deaminase (EC 3.5.4.4) (Adenosine aminohydrolase)
