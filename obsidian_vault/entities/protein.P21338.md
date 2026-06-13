---
entity_id: "protein.P21338"
entity_type: "protein"
name: "rna"
source_database: "UniProt"
source_id: "P21338"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm. Cytoplasm. Note=RNase I (periplasmic) and RNase I* (cytoplasmic) appear to be isoforms apparently encoded by the same gene. The cytoplasmic form is less active towards natural polymer RNA."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rna rnsA b0611 JW0603"
---

# rna

`protein.P21338`

## Static

- Type: `protein`
- Source: `UniProt:P21338`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm. Cytoplasm. Note=RNase I (periplasmic) and RNase I* (cytoplasmic) appear to be isoforms apparently encoded by the same gene. The cytoplasmic form is less active towards natural polymer RNA.

## Enriched Summary

FUNCTION: One of the few RNases that cleaves the phosphodiester bond between any two nucleotide. Shows a preference for cytidylic or guanylic acid. Ribonuclease I (RNase I) is an endoribonuclease that cleaves phosphodiester bonds between any two nucleotides in RNA, yielding nucleoside 3'-phosphates and 3'-phosphooligonucleotides . RNase I is partially responsible for the degradation of total and ribosomal RNA during both normal and nutrient starvation conditions, especially during carbon starvation . RNase I is specifically required for the breakdown of 23S RNA, though it is not required for degradation of 16S RNA or very small (4S) RNA fragments that result from breakdown of larger RNA . RNase I degradation of the 50S ribosomal subunit releases the ribosomal proteins L4, L10 and L7/12 in addition to cleaving the 23S RNA to yield a smaller product . Polyamines stimulate the activity of RNase I against synthetic polynucleotides in vitro . RNase I is primarily a periplasmic protein that can be released by spheroblasting or treatment of cells with N-dodecyldiethanolamine. The latter treatment allows subsequent enhanced breakdown of rRNA by RNase I . RNase I appears to remain with the membrane fraction in disrupted cells and is associated with the 30S ribosomal subunit . The gene encoding RNase I was cloned, sequenced, and its physical map position determined...

## Biological Role

Catalyzes 3.1.27.6-RXN (reaction.ecocyc.3.1.27.6-RXN), RXN0-6526 (reaction.ecocyc.RXN0-6526), RXN0-6527 (reaction.ecocyc.RXN0-6527).

## Annotation

FUNCTION: One of the few RNases that cleaves the phosphodiester bond between any two nucleotide. Shows a preference for cytidylic or guanylic acid.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.3.1.27.6-RXN|reaction.ecocyc.3.1.27.6-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6526|reaction.ecocyc.RXN0-6526]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6527|reaction.ecocyc.RXN0-6527]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0611|gene.b0611]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P21338`
- `KEGG:ecj:JW0603;eco:b0611;ecoc:C3026_03055;`
- `GeneID:949065;`
- `GO:GO:0003723; GO:0005737; GO:0006401; GO:0008847; GO:0016787; GO:0030288; GO:0033897`
- `EC:4.6.1.21`

## Notes

Ribonuclease I (RNase I) (EC 4.6.1.21) (Enterobacter ribonuclease)
