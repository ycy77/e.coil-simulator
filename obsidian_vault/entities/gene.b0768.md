---
entity_id: "gene.b0768"
entity_type: "gene"
name: "ybhD"
source_database: "NCBI RefSeq"
source_id: "gene-b0768"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0768"
  - "ybhD"
---

# ybhD

`gene.b0768`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0768`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybhD (gene.b0768) is a gene entity. It encodes ybhD (protein.P52696). Encoded protein function: Uncharacterized HTH-type transcriptional regulator YbhD EcoCyc product frame: G6398-MONOMER. Genomic coordinates: 799622-800575. EcoCyc protein note: YbhD was predicted to be a LysR-type transcription factor ; it contains a helix-turn-helix DNA-binding motif in its N-terminal domain and is probably involved in regulation of L-malate utilization . However, the effect of YbhD on the transcription of any gene has not yet been demonstrated . YbhD DNA-binding activity was probed in vivo in glucose M9 minimal medium by the chromatin immunoprecipitation method combined with lambda exonuclease digestion (ChIP-exo) . YbhD was found transcriptionally upregulated in the presence of threonine (Thr) in M9 medium . The transcriptional response for the deletion of YbdH has been characterized by RNA-seq in M9 minimal medium supplemented with 7 mM l-threonine . In the YbdH knockout strain, the gene ybhH, which is adjacent and divergently oriented from ybhD, was strongly upregulated. It was then proposed that YbdH negatively regulates it; however, binding was not detected under the growth conditions used in ChIP-exo studies . A YbhD knockout strain is able to grow in M9 minimal medium with glycerol only when L-malate is supplemented...

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P52696|protein.P52696]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=ybhD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0002613,ECOCYC:G6398,GeneID:944869`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:799622-800575:-; feature_type=gene
