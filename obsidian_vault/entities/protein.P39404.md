---
entity_id: "protein.P39404"
entity_type: "protein"
name: "bglJ"
source_database: "UniProt"
source_id: "P39404"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "bglJ yjjR b4366 JW5955"
---

# bglJ

`protein.P39404`

## Static

- Type: `protein`
- Source: `UniProt:P39404`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: A crytic transcriptional activator. When its expression is induced it relieves H-NS repression of the bgl operon. Acts independently of transcription factor LeuO. {ECO:0000269|PubMed:8725214}. BglJ is a positive DNA-binding transcriptional regulator of transport and utilization of the aromatic β-glucosides arbutin and salicin . The expression of the gene bglJ induces the bglGFB operon via unknown mechanisms. This suggests the possibility that BglJ controls, directly or indirectly, the expression of the bgl operon . BglJ is a protein that belongs to the LuxR/UhpA family of transcriptional regulators . It shows a potential helix-turn-helix motif in the carboxyl-terminal domain, which has 48% identity and 70% similarity to the corresponding domain of the RcsB protein . A negative correlation between cellular growth and the copy number of the proteins BglJ has been reported . BglJ was transcriptionally upregulated in iron limitation over iron excess at 21% and 63% of dissolved oxygen as determined by RNA-seq .

## Biological Role

Component of RcsB-BglJ DNA-binding transcriptional activator (complex.ecocyc.CPLX0-7916).

## Annotation

FUNCTION: A crytic transcriptional activator. When its expression is induced it relieves H-NS repression of the bgl operon. Acts independently of transcription factor LeuO. {ECO:0000269|PubMed:8725214}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7916|complex.ecocyc.CPLX0-7916]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4366|gene.b4366]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39404`
- `KEGG:ecj:JW5955;eco:b4366;ecoc:C3026_23585;`
- `GeneID:948889;`
- `GO:GO:0000976; GO:0003700; GO:0005667; GO:0006355; GO:0009314; GO:0043470; GO:0045893`

## Notes

Transcriptional activator protein BglJ
