---
entity_id: "protein.P76316"
entity_type: "protein"
name: "dcyD"
source_database: "UniProt"
source_id: "P76316"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dcyD yedO b1919 JW5313"
---

# dcyD

`protein.P76316`

## Static

- Type: `protein`
- Source: `UniProt:P76316`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the alpha,beta-elimination reaction of D-cysteine and of several D-cysteine derivatives. It could be a defense mechanism against D-cysteine. Can also catalyze the degradation of 3-chloro-D-alanine. {ECO:0000255|HAMAP-Rule:MF_01045, ECO:0000269|PubMed:3908101}. D-cysteine desulfhydrase (DcyD) is involved in utilization of D-cysteine as a source of sulfur. The enzyme also protects the cell from growth inhibition caused by D-cysteine, which interferes with isoleucine, leucine, and valine biosynthesis via inhibition of THREDEHYDSYN-CPLX . DcyD has similarity to 1-aminocyclopropane-carboxylate deaminases, but does not exhibit activity toward this substrate . 3-Chloro-D-alanine is an effective antibacterial agent. Although the purified enzyme catalyzes the α,β elimination reaction with 3-chloro-D-alanine, the reaction does not appear to occur in vivo . Of the strains originally tested, the mutant W3110 ΔtrpED102/F'ΔtrpED102 contained the highest amount of D-cysteine desulfhydrase . A dcyD mutant exhibits decreased resistance to D-cysteine, while overexpression causes increased resistance to D-cysteine compared to wild type . Transcription of dcyD is induced under low sulfate conditions...

## Biological Role

Component of D-cysteine desulfhydrase, PLP-dependent / 3-chloro-D-alanine dehydrochlorinase (complex.ecocyc.DCYSDESULF-CPLX).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the alpha,beta-elimination reaction of D-cysteine and of several D-cysteine derivatives. It could be a defense mechanism against D-cysteine. Can also catalyze the degradation of 3-chloro-D-alanine. {ECO:0000255|HAMAP-Rule:MF_01045, ECO:0000269|PubMed:3908101}.

## Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.DCYSDESULF-CPLX|complex.ecocyc.DCYSDESULF-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1919|gene.b1919]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76316`
- `KEGG:ecj:JW5313;eco:b1919;ecoc:C3026_10890;`
- `GeneID:75172041;75205835;946831;`
- `GO:GO:0005829; GO:0006790; GO:0006791; GO:0010438; GO:0019148; GO:0019149; GO:0019447; GO:0030170; GO:0042803; GO:0046416`
- `EC:4.4.1.15`

## Notes

D-cysteine desulfhydrase (EC 4.4.1.15)
