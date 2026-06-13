---
entity_id: "gene.b2669"
entity_type: "gene"
name: "stpA"
source_database: "NCBI RefSeq"
source_id: "gene-b2669"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2669"
  - "stpA"
---

# stpA

`gene.b2669`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2669`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

stpA (gene.b2669) is a gene entity. It encodes stpA (protein.P0ACG1). Encoded protein function: FUNCTION: A DNA-binding protein that acts in a fashion similar to H-NS protein upon overexpression, represses a number of genes including the cryptic blg operon, hns, papB and the proU locus (PubMed:8890170). A subset of H-NS/StpA-regulated genes also require Hha for repression; Hha and Cnu (YdgT) increases the number of genes DNA bound by H-NS/StpA and may also modulate the oligomerization of the H-NS/StpA-complex (PubMed:23543115). Repression can be inhibited by dominant-negative mutants of StpA or H-NS (PubMed:8755860). {ECO:0000269|PubMed:23543115, ECO:0000269|PubMed:8755860, ECO:0000269|PubMed:8890170}.; FUNCTION: (Microbial infection) Originally isolated as a suppressor of a splicing defect of the thymidylate synthase (td) gene from bacteriophage T4 (PubMed:1480493). Acts as an RNA chaperone, accelerating splicing of viral pre-mRNA. Binds preferentially to unstructured over structured RNA; does not have a detectable high-affinity RNA-binding site in the pre-mRNA. There do not seem to be any specific RNA targets in transcribed E.coli DNA (PubMed:17267410). {ECO:0000269|PubMed:1480493, ECO:0000269|PubMed:17267410}. EcoCyc product frame: EG11554-MONOMER. EcoCyc synonyms: hnsB. Genomic coordinates: 2798091-2798495...

## Biological Role

Repressed by ArgR-L-arginine DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-228), argR (protein.P0A6D0), hns (protein.P0ACF8). Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACG1|protein.P0ACG1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `C` - regulator=Lrp; target=stpA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[complex.ecocyc.CPLX0-228|complex.ecocyc.CPLX0-228]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `S` - regulator=ArgR; target=stpA; function=-
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=stpA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008788,ECOCYC:EG11554,GeneID:947130`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2798091-2798495:-; feature_type=gene
