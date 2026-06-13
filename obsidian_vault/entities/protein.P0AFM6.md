---
entity_id: "protein.P0AFM6"
entity_type: "protein"
name: "pspA"
source_database: "UniProt"
source_id: "P0AFM6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:19555453}. Cell inner membrane {ECO:0000269|PubMed:19555453}; Peripheral membrane protein {ECO:0000269|PubMed:19555453}; Cytoplasmic side {ECO:0000269|PubMed:19555453}. Note=Localizes at both cell poles and along the length of the cell."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pspA b1304 JW1297"
---

# pspA

`protein.P0AFM6`

## Static

- Type: `protein`
- Source: `UniProt:P0AFM6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:19555453}. Cell inner membrane {ECO:0000269|PubMed:19555453}; Peripheral membrane protein {ECO:0000269|PubMed:19555453}; Cytoplasmic side {ECO:0000269|PubMed:19555453}. Note=Localizes at both cell poles and along the length of the cell.

## Enriched Summary

FUNCTION: The phage shock protein (psp) operon (pspABCDE) may play a significant role in the competition for survival under nutrient- or energy-limited conditions. PspA negatively regulates expression of the pspABCDE promoter and of pspG through negative regulation of the psp-specific transcriptional activator PspF. Is also required for membrane integrity, efficient translocation and maintenance of the proton motive force. {ECO:0000269|PubMed:10629175, ECO:0000269|PubMed:15485810, ECO:0000269|PubMed:1712397, ECO:0000269|PubMed:19804784, ECO:0000269|PubMed:8598199}. PspA is a bifunctional protein, protecting membrane integrity under stress conditions and regulating EG12344-MONOMER PspF transcription factor activity. PspA was first identified as a highly expressed protein upon infection of E. coli with the filamentous phage f1. PspA is a bacterial member of the conserved ESCRT-III family of proteins which are involved in membrane remodelling and repair across all domains of life . Based on its heptad repeat motif, PspA was predicted to form a coiled-coil structure . Three-dimensional reconstruction of a homomultimeric PspA complex revealed a 9-fold rotationally symmetric ring; the nine domains are predicted to be composed of four individual PspA subunits . Native PspA forms large oligomeric scaffold-like structures that are detergent-sensitive...

## Biological Role

Component of PspABC complex (complex.ecocyc.CPLX0-10367).

## Annotation

FUNCTION: The phage shock protein (psp) operon (pspABCDE) may play a significant role in the competition for survival under nutrient- or energy-limited conditions. PspA negatively regulates expression of the pspABCDE promoter and of pspG through negative regulation of the psp-specific transcriptional activator PspF. Is also required for membrane integrity, efficient translocation and maintenance of the proton motive force. {ECO:0000269|PubMed:10629175, ECO:0000269|PubMed:15485810, ECO:0000269|PubMed:1712397, ECO:0000269|PubMed:19804784, ECO:0000269|PubMed:8598199}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-10367|complex.ecocyc.CPLX0-10367]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1304|gene.b1304]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFM6`
- `KEGG:ecj:JW1297;eco:b1304;ecoc:C3026_07650;`
- `GeneID:93775430;945887;`
- `GO:GO:0005543; GO:0005667; GO:0005829; GO:0005886; GO:0006355; GO:0009271; GO:0009408; GO:0042802; GO:0060187; GO:0080135`

## Notes

Phage shock protein A
