---
entity_id: "protein.P77171"
entity_type: "protein"
name: "ydcI"
source_database: "UniProt"
source_id: "P77171"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ydcI b1422 JW5226"
---

# ydcI

`protein.P77171`

## Static

- Type: `protein`
- Source: `UniProt:P77171`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Transcription factor involved in pH homeostasis and acetate metabolism (PubMed:30137486). It is required to maintain physiological activity at acidic/alkaline conditions (PubMed:30137486). It is also involved in regulating the carbon flux in the TCA cycle (PubMed:30137486). It affects, direct or indirectly, the expression of about 60 genes (PubMed:32419108). The vast majority (almost all) of the genes of the YdcI regulon in both log and stationary are small genes (less than 800 bp) encoding small proteins, sRNA or pseudogenes (PubMed:32419108). The transcriptional factor binding sites (TFBS) of YdcI enclose AT-rich inverted repeats separated by 7-nt (PubMed:30137486). {ECO:0000269|PubMed:30137486, ECO:0000269|PubMed:32419108}. Based on results with purified YdcI protein with a DNA probe in a gel shift assay, YdcI was shown to be a DNA-binding transcriptional repressor which negatively regulates its own expression in Salmonella enterica serovar Typhimurium . YdcI was confirmed as a TF through an integrated workflow comprised of computational prediction, knowledge-based classification, and experimental validation of candidate TFs at the genome scale . YdcI is involved in pH homeostasis and acetate metabolism...

## Annotation

FUNCTION: Transcription factor involved in pH homeostasis and acetate metabolism (PubMed:30137486). It is required to maintain physiological activity at acidic/alkaline conditions (PubMed:30137486). It is also involved in regulating the carbon flux in the TCA cycle (PubMed:30137486). It affects, direct or indirectly, the expression of about 60 genes (PubMed:32419108). The vast majority (almost all) of the genes of the YdcI regulon in both log and stationary are small genes (less than 800 bp) encoding small proteins, sRNA or pseudogenes (PubMed:32419108). The transcriptional factor binding sites (TFBS) of YdcI enclose AT-rich inverted repeats separated by 7-nt (PubMed:30137486). {ECO:0000269|PubMed:30137486, ECO:0000269|PubMed:32419108}.

## Outgoing Edges (3)

- `activates` --> [[gene.b0382|gene.b0382]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1493|gene.b1493]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1892|gene.b1892]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## Incoming Edges (1)

- `encodes` <-- [[gene.b1422|gene.b1422]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77171`
- `KEGG:ecj:JW5226;eco:b1422;ecoc:C3026_08280;`
- `GeneID:948865;`
- `GO:GO:0003677; GO:0003700; GO:0005829; GO:0006355; GO:0043565; GO:0045892`

## Notes

HTH-type transcriptional regulator YdcI
