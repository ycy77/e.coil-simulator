---
entity_id: "protein.P77746"
entity_type: "protein"
name: "ybdO"
source_database: "UniProt"
source_id: "P77746"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ybdO b0603 JW0596"
---

# ybdO

`protein.P77746`

## Static

- Type: `protein`
- Source: `UniProt:P77746`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Uncharacterized HTH-type transcriptional regulator YbdO The LysR-type transcriptional regulator CitR, "Citrate utilization Regulator" is involved in citrate metabolism . And was predicted to regulate genes related to signaling and stress . CitR was found transcriptionally upregulated in the presence of threonine (Thr) in M9 medium . Genome-wide CitR binding sites were determined in vivo by the chromatin immunoprecipitation method combined with lambda exonuclease digestion (ChIP-exo) in glucose M9 minimal medium . The transcriptional response for the deletion of CitR was characterized by RNA-seq in M9 minimal medium supplemented by 7 mM l-threonine . Genes differentially expressed in the absence or presence of CitR encode proteins involved in citrate metabolism . By integrative analysis of ChIP-exo and RNA-seq data, it was determined that CitR is autoregulated, repressing the operon citR-ybdNM . The operon citR-ybdNM was found conserved in Enterobacteriaceae . CitR has an effect on growth at low pH in M9 medium supplemented with citrate . A CitR knockout mutant showed decreased growth when glycolate was used as carbon source, and also during microaerobic utilization of formate as carbon source . In this strain, the transcription of the gene lrhA was substantially decreased compared with the wild type strain . CitR is a paralog of YbeF with 30% identity...

## Annotation

Uncharacterized HTH-type transcriptional regulator YbdO

## Outgoing Edges (3)

- `represses` --> [[gene.b0601|gene.b0601]] `RegulonDB` `S` - regulator=CitR; target=ybdM; function=-
- `represses` --> [[gene.b0602|gene.b0602]] `RegulonDB` `S` - regulator=CitR; target=ybdN; function=-
- `represses` --> [[gene.b0603|gene.b0603]] `RegulonDB` `S` - regulator=CitR; target=citR; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b0603|gene.b0603]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77746`
- `KEGG:ecj:JW0596;eco:b0603;ecoc:C3026_03015;`
- `GeneID:945216;`
- `GO:GO:0003677; GO:0003700; GO:0006355`

## Notes

Uncharacterized HTH-type transcriptional regulator YbdO
