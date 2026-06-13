---
entity_id: "protein.P77615"
entity_type: "protein"
name: "ycjW"
source_database: "UniProt"
source_id: "P77615"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ycjW b1320 JW1313"
---

# ycjW

`protein.P77615`

## Static

- Type: `protein`
- Source: `UniProt:P77615`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Transcriptional regulator that represses the expression of genes involved in carbohydrate metabolism (PubMed:31253770). Binds DNA near ycjM and ycjU and regulates expression of the operon ycjMNOPQRSTUV-ompG (PubMed:31253770). {ECO:0000269|PubMed:31253770}. YcjW is a transcriptional regulator involved in the control of carbohydrate metabolism genes . ycjW was identified in a screen for genes that reduce the lethal effects of stress. A ycjW insertion mutant is more sensitive than wild type to mitomycin C . YcjW was predicted to be a GalR-type transcription factor using the Hidden Markov Model . YcjW DNA-binding activity was probed in vivo in glucose M9 minimal medium through chromatin immunoprecipitation assays (ChIP-exo) . Consensus binding motif of YcjW was found to be palindromic and approximately 14 nt: TGGNANCGGTNCCA . However, the effect YcjW on the transcription of any gene has not yet been demonstrated . Upstream of the ycjW gene, a sequence was found that could work as a transcriptional promoter . YcjW was transcriptionally upregulated in iron limitation over iron excess at 63% dissolved oxygen as determined by RNA-seq . The YcjW binding landscape was globally mapped in vivo by standardized ChIP-seq and quantitatively modeled using BoltzNet, a biophysically informed neural network that infers binding energy from sequence data...

## Annotation

FUNCTION: Transcriptional regulator that represses the expression of genes involved in carbohydrate metabolism (PubMed:31253770). Binds DNA near ycjM and ycjU and regulates expression of the operon ycjMNOPQRSTUV-ompG (PubMed:31253770). {ECO:0000269|PubMed:31253770}.

## Outgoing Edges (10)

- `represses` --> [[gene.b1309|gene.b1309]] `RegulonDB` `S` - regulator=YcjW; target=ycjM; function=-
- `represses` --> [[gene.b1310|gene.b1310]] `RegulonDB` `S` - regulator=YcjW; target=ycjN; function=-
- `represses` --> [[gene.b1311|gene.b1311]] `RegulonDB` `S` - regulator=YcjW; target=ycjO; function=-
- `represses` --> [[gene.b1312|gene.b1312]] `RegulonDB` `S` - regulator=YcjW; target=ycjP; function=-
- `represses` --> [[gene.b1313|gene.b1313]] `RegulonDB` `S` - regulator=YcjW; target=ycjQ; function=-
- `represses` --> [[gene.b1314|gene.b1314]] `RegulonDB` `S` - regulator=YcjW; target=ycjR; function=-
- `represses` --> [[gene.b1315|gene.b1315]] `RegulonDB` `S` - regulator=YcjW; target=ycjS; function=-
- `represses` --> [[gene.b1316|gene.b1316]] `RegulonDB` `S` - regulator=YcjW; target=ycjT; function=-
- `represses` --> [[gene.b1317|gene.b1317]] `RegulonDB` `S` - regulator=YcjW; target=ycjU; function=-
- `represses` --> [[gene.b1319|gene.b1319]] `RegulonDB` `S` - regulator=YcjW; target=ompG; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b1320|gene.b1320]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77615`
- `KEGG:ecj:JW1313;eco:b1320;ecoc:C3026_07730;`
- `GeneID:945875;`
- `GO:GO:0000976; GO:0003700; GO:0006351; GO:0006355; GO:0006974; GO:0045892`

## Notes

HTH-type transcriptional repressor YcjW
