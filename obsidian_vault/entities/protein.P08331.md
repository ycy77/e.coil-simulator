---
entity_id: "protein.P08331"
entity_type: "protein"
name: "cpdB"
source_database: "UniProt"
source_id: "P08331"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:3005231}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cpdB b4213 JW4171"
---

# cpdB

`protein.P08331`

## Static

- Type: `protein`
- Source: `UniProt:P08331`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:3005231}.

## Enriched Summary

FUNCTION: This bifunctional enzyme catalyzes two consecutive reactions during ribonucleic acid degradation. Converts a 2',3'-cyclic nucleotide to a 3'-nucleotide and then the 3'-nucleotide to the corresponding nucleoside and phosphate. {ECO:0000269|PubMed:3005231}. cpdB encodes periplasmic 2',3'-cyclic nucleotide 2'-phosphodiesterase . First characterized in E. coli B, the enzyme contains both cyclic phosphodiesterase and 3'-nucleotidase activity and catalyses the hydrolysis of 2',3'-cyclic nucleotides to yield nucleotides and phosphate via a two-step reaction . Kinetic analyses suggest that the enzyme has two distinct active sites . The physiological role of CpdB may be to break down ribonucleotide 2',3'-cyclic phosphates which can be formed when RNA is digested by ribosome-bound RNase . Purified, recombinant CpdB, cloned from E. coli BL21, is a broad specificity phosphohydrolase; in addition to the major substrates - 2',3'-cyclic nucleotides and 3'-nucleotides - it also has moderate activity on linear dinucleotides (pApA, pGpG), cyclic-dinucleotides (c-di-AMPand c-di-GMP), diadenosine oligophosphates, and adenosine 5'-oligophosphates (ATP, ADP); kinetic parameters are reported for all substrates . Cyclic-dinucleotide phosphodiesterase activity may be relevant as a virulence factor...

## Biological Role

Catalyzes uridine 3'-monophosphate phosphohydrolase (reaction.R01877), cytidine 3'-phosphate phosphohydrolase (reaction.R02370), nucleoside-2',3'-cyclic-phosphate 3'-nucleotidohydrolase (reaction.R03423), 3-NUCLEOTID-RXN (reaction.ecocyc.3-NUCLEOTID-RXN), CYCPHOSDIESTER-RXN (reaction.ecocyc.CYCPHOSDIESTER-RXN), RXN-14064 (reaction.ecocyc.RXN-14064), RXN-14090 (reaction.ecocyc.RXN-14090), RXN-14091 (reaction.ecocyc.RXN-14091), and 5 more.

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: This bifunctional enzyme catalyzes two consecutive reactions during ribonucleic acid degradation. Converts a 2',3'-cyclic nucleotide to a 3'-nucleotide and then the 3'-nucleotide to the corresponding nucleoside and phosphate. {ECO:0000269|PubMed:3005231}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (13)

- `catalyzes` --> [[reaction.R01877|reaction.R01877]] `KEGG` `database` - via EC:3.1.3.6
- `catalyzes` --> [[reaction.R02370|reaction.R02370]] `KEGG` `database` - via EC:3.1.3.6
- `catalyzes` --> [[reaction.R03423|reaction.R03423]] `KEGG` `database` - via EC:3.1.4.16
- `catalyzes` --> [[reaction.ecocyc.3-NUCLEOTID-RXN|reaction.ecocyc.3-NUCLEOTID-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.CYCPHOSDIESTER-RXN|reaction.ecocyc.CYCPHOSDIESTER-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-14064|reaction.ecocyc.RXN-14064]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-14090|reaction.ecocyc.RXN-14090]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-14091|reaction.ecocyc.RXN-14091]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-14112|reaction.ecocyc.RXN-14112]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-14113|reaction.ecocyc.RXN-14113]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-14115|reaction.ecocyc.RXN-14115]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-14124|reaction.ecocyc.RXN-14124]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-14126|reaction.ecocyc.RXN-14126]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4213|gene.b4213]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P08331`
- `KEGG:ecj:JW4171;eco:b4213;ecoc:C3026_22755;`
- `GeneID:75169736;948729;`
- `GO:GO:0000166; GO:0006974; GO:0008254; GO:0008663; GO:0009166; GO:0030288; GO:0046872`
- `EC:3.1.3.6; 3.1.4.16`

## Notes

2',3'-cyclic-nucleotide 2'-phosphodiesterase/3'-nucleotidase (EC 3.1.3.6) (EC 3.1.4.16)
