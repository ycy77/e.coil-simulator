---
entity_id: "protein.P76034"
entity_type: "protein"
name: "yciT"
source_database: "UniProt"
source_id: "P76034"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yciT b1284 JW1276"
---

# yciT

`protein.P76034`

## Static

- Type: `protein`
- Source: `UniProt:P76034`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Uncharacterized HTH-type transcriptional regulator YciT YciT was predicted to be a DeoR-type transcription factor using the Hidden Markov Model . DNA binding was probed by chromatin immunoprecipitation assays (ChIP-exo) . Consensus binding motif of YciT was found to be palindromic and approximately 16 nt: NTTTCANNTNAAANNN . Gene expression profile analysis of the wild-type strain and a yciT knockout strain using RNA-seq showed differential expression of a set of genes also identified by ChIP-exo (between others), indicating they are the direct regulatory targets of this transcription factor . RNA-seq studies and mutant phenotype analysis showed that YciT is involved in the control of osmolarity in E. coli . The deletion of the yciT gene did not affect significantly the growth in glucose, fructose, or sorbitol; however, in glucose and fructose the stationary phase was reached at an OD600 slightly lower than that for the wild-type strain . YciT belongs to the DeoR family of transcriptional regulators. Expression of malK, malE, pepN and fadA was downregulated in the presence of YciT; the effect could be indirect . The YciT binding landscape was globally mapped in vivo by standardized ChIP-seq and quantitatively modeled using BoltzNet, a biophysically informed neural network that infers binding energy from sequence data...

## Annotation

Uncharacterized HTH-type transcriptional regulator YciT

## Outgoing Edges (4)

- `activates` --> [[gene.b0824|gene.b0824]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b4189|gene.b4189]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b0573|gene.b0573]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b4109|gene.b4109]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## Incoming Edges (1)

- `encodes` <-- [[gene.b1284|gene.b1284]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76034`
- `KEGG:ecj:JW1276;eco:b1284;ecoc:C3026_07535;`
- `GeneID:945869;`
- `GO:GO:0000987; GO:0005829; GO:0006355; GO:0006974; GO:0098531`

## Notes

Uncharacterized HTH-type transcriptional regulator YciT
