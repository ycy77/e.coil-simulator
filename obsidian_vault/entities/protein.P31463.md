---
entity_id: "protein.P31463"
entity_type: "protein"
name: "yidZ"
source_database: "UniProt"
source_id: "P31463"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yidZ b3711 JW3689"
---

# yidZ

`protein.P31463`

## Static

- Type: `protein`
- Source: `UniProt:P31463`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in anaerobic NO protection. YidZ was predicted to be a LysR-type transcription factor using the Hidden Markov Model . DNA binding was found by chromatin immunoprecipitation assays (ChIP-exo) . Gene expression profile analysis of the wild-type strain and a yidZ knockout strain using RNA-seq showed differential expression of a set of genes also identified by ChIP-exo, indicating they are the direct regulatory targets . RNA-seq studies showed that in a yidZ knockout strain, genes associated with carbohydrate transport and metabolism were upregulated while genes involved in acid stress response and amino acid transport and metabolism were downregulated with respect to the wild-type strain . Based on SWISS-MODEL, YidZ could form dimers or tetramers . Levels of yidZ mRNA are increased in cells treated with NO under anaerobic growth conditions. An E. coli strain lacking a functional yidZ gene is more sensitive to NO than wild type . The YidZ binding landscape was globally mapped in vivo by standardized ChIP-seq and quantitatively modeled using BoltzNet, a biophysically informed neural network that infers binding energy from sequence data . The resulting ChIP-seq binding regions are available in RegulonDB (Galagan collection), and the corresponding energy matrix and genomic binding profiles can be accessed at boltznet.bu.edu .

## Annotation

FUNCTION: Involved in anaerobic NO protection.

## Outgoing Edges (4)

- `represses` --> [[gene.b0189|gene.b0189]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b3748|gene.b3748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b3775|gene.b3775]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b4034|gene.b4034]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## Incoming Edges (1)

- `encodes` <-- [[gene.b3711|gene.b3711]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31463`
- `KEGG:ecj:JW3689;eco:b3711;ecoc:C3026_20120;`
- `GeneID:948227;`
- `GO:GO:0003677; GO:0003700; GO:0006351; GO:0006355`

## Notes

HTH-type transcriptional regulator YidZ
