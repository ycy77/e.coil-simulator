---
entity_id: "gene.b0603"
entity_type: "gene"
name: "citR"
source_database: "NCBI RefSeq"
source_id: "gene-b0603"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0603"
  - "citR"
---

# citR

`gene.b0603`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0603`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

citR (gene.b0603) is a gene entity. It encodes ybdO (protein.P77746). Encoded protein function: Uncharacterized HTH-type transcriptional regulator YbdO EcoCyc product frame: G6332-MONOMER. EcoCyc synonyms: ybdO. Genomic coordinates: 636716-637618. EcoCyc protein note: The LysR-type transcriptional regulator CitR, "Citrate utilization Regulator" is involved in citrate metabolism . And was predicted to regulate genes related to signaling and stress . CitR was found transcriptionally upregulated in the presence of threonine (Thr) in M9 medium . Genome-wide CitR binding sites were determined in vivo by the chromatin immunoprecipitation method combined with lambda exonuclease digestion (ChIP-exo) in glucose M9 minimal medium . The transcriptional response for the deletion of CitR was characterized by RNA-seq in M9 minimal medium supplemented by 7 mM l-threonine . Genes differentially expressed in the absence or presence of CitR encode proteins involved in citrate metabolism . By integrative analysis of ChIP-exo and RNA-seq data, it was determined that CitR is autoregulated, repressing the operon citR-ybdNM . The operon citR-ybdNM was found conserved in Enterobacteriaceae . CitR has an effect on growth at low pH in M9 medium supplemented with citrate...

## Biological Role

Repressed by ybdO (protein.P77746).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77746|protein.P77746]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P77746|protein.P77746]] `RegulonDB` `S` - regulator=CitR; target=citR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002077,ECOCYC:G6332,GeneID:945216`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:636716-637618:-; feature_type=gene
