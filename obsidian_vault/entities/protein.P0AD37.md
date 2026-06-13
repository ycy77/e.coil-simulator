---
entity_id: "protein.P0AD37"
entity_type: "protein"
name: "yfeC"
source_database: "UniProt"
source_id: "P0AD37"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yfeC b2398 JW2393"
---

# yfeC

`protein.P0AD37`

## Static

- Type: `protein`
- Source: `UniProt:P0AD37`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Uncharacterized protein YfeC YfeC was initially identified as a putative transcription factor using a homology-based algorithm . DNA binding was probed by chromatin immunoprecipitation assays (ChIP-exo) . Gene expression profile analysis of the wild-type strain and a yfeC knockout strain using RNA-seq showed differential expression of a set of genes also identified by ChIP-exo (between others), indicating they are the direct regulatory targets . Some of these direct regulatory targets were upregulated and others were downregulated, indicating that YfeC is a dual regulator . Consensus binding motif analysis showed that the TFBSs of YfeC have TTC-rich inverted repeats separated by 6 nt . Based on SWISS-MODEL, YfeC was predicted to form homodimers . The yfeCD locus was predicted to encode a toxin/antitoxin pair . However, no evidence for this function was found . Levels of extracellular DNA are increased in a yfeC deletion strain grown in liquid culture . The transcription of the yfeC gene is affected by temperature, oxidative stress and glucose-lactose shift . The YfeC binding landscape was globally mapped in vivo by standardized ChIP-seq and quantitatively modeled using BoltzNet, a biophysically informed neural network that infers binding energy from sequence data...

## Annotation

Uncharacterized protein YfeC

## Outgoing Edges (6)

- `activates` --> [[gene.b2398|gene.b2398]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b2833|gene.b2833]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b2992|gene.b2992]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b3065|gene.b3065]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b3637|gene.b3637]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b3703|gene.b3703]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## Incoming Edges (1)

- `encodes` <-- [[gene.b2398|gene.b2398]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AD37`
- `KEGG:ecj:JW2393;eco:b2398;ecoc:C3026_13325;`
- `GeneID:946857;`

## Notes

Uncharacterized protein YfeC
