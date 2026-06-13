---
entity_id: "protein.P30864"
entity_type: "protein"
name: "yafC"
source_database: "UniProt"
source_id: "P30864"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yafC b0208 JW0198"
---

# yafC

`protein.P30864`

## Static

- Type: `protein`
- Source: `UniProt:P30864`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Uncharacterized HTH-type transcriptional regulator YafC YafC, which contains a helix-turn-helix motif to bind DNA in its N-terminal domain, appears to belong to the LysR family of transcription factors (TFs), and it was predicted to regulate genes related to metabolism and chlorine resistance . YafC was confirmed as a TF through an integrated workflow comprised of computational prediction, knowledge-based classification, and experimental validation of candidate TFs at the genome scale . Compared to known global TFs, YafC exhibits some interesting regulatory features. First, it has more intragenic binding peaks and fewer peaks located within putative regulatory regions. Second, it has fewer binding peaks than global TFs, such as CRP, Lrp, Fnr, and ArcA. Third, it binds to more genes with putative functions. Finally, its expression level is lower relative to that of the majority of global TFs . The most common binding mode for YafC is downstream of the RNAP binding region . Upstream of the yafC gene, a sequence was found that could work as a transcriptional promoter, and the transcription of the yafC gene is affected by temperature . yafC insertion mutants were identified in a genetic screen for genes that are important for survival of exposure to ionizing radiation (IR). A yafC deletion mutant has a moderate decrease in IR survival...

## Annotation

Uncharacterized HTH-type transcriptional regulator YafC

## Outgoing Edges (1)

- `activates` --> [[gene.b2764|gene.b2764]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## Incoming Edges (1)

- `encodes` <-- [[gene.b0208|gene.b0208]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P30864`
- `KEGG:ecj:JW0198;eco:b0208;ecoc:C3026_00970;`
- `GeneID:947507;`
- `GO:GO:0000976; GO:0003700; GO:0006355; GO:0010212`

## Notes

Uncharacterized HTH-type transcriptional regulator YafC
