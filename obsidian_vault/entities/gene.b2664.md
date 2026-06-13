---
entity_id: "gene.b2664"
entity_type: "gene"
name: "glaR"
source_database: "NCBI RefSeq"
source_id: "gene-b2664"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2664"
  - "glaR"
---

# glaR

`gene.b2664`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2664`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glaR (gene.b2664) is a gene entity. It encodes glaR (protein.P37338). Encoded protein function: FUNCTION: Negatively regulates the expression of the glaH-lhgD-gabDTP operon in a temporal manner during entry into stationary phase or during the first few hours of carbon starvation (PubMed:14731280, PubMed:30498244). Thereby is involved in the regulation of a L-lysine degradation pathway that proceeds via cadaverine, glutarate and L-2-hydroxyglutarate (PubMed:30498244). Binds to two primary and two secondary sites in the promoter region of the glaH operon with the consensus sequences TTGTN5TTTT and ATGTN5TTTT of the primary sites, each separated by six nucleotides (PubMed:30498244). {ECO:0000269|PubMed:14731280, ECO:0000269|PubMed:30498244}. EcoCyc product frame: EG12386-MONOMER. EcoCyc synonyms: ygaE, gabC, csiR. Genomic coordinates: 2795674-2796336. EcoCyc protein note: The transcription factor CsiR, for "Carbon starvation induced Regulator," was initially identified as a repressor that controls the transcription of genes involved in the degradation and transport of 4-aminobutyrate (GABA) for utilization as a source of nitrogen . However, CsiR does not appear to respond directly to the presence of GABA , and later reports suggested that it does not affect expression of gabDTP . CsiR represses transcription from the csiD promoter during stationary phase...

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37338|protein.P37338]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=glaR; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008765,ECOCYC:EG12386,GeneID:948055`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2795674-2796336:+; feature_type=gene
