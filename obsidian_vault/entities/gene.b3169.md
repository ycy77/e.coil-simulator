---
entity_id: "gene.b3169"
entity_type: "gene"
name: "nusA"
source_database: "NCBI RefSeq"
source_id: "gene-b3169"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3169"
  - "nusA"
---

# nusA

`gene.b3169`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3169`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nusA (gene.b3169) is a gene entity. It encodes nusA (protein.P0AFF6). Encoded protein function: FUNCTION: Part of the processive rRNA transcription and antitermination complex (rrnTAC). The complex forms an RNA-chaperone ring around the RNA exit tunnel of RNA polymerase (RNAP). It supports rapid transcription and antitermination of rRNA operons, cotranscriptional rRNA folding, and annealing of distal rRNA regions to allow correct ribosome biogenesis (PubMed:32871103). Participates in both transcription termination and antitermination. Involved in a variety of cellular termination and antitermination processes, such as Rho-dependent transcriptional termination and intrinsic termination (PubMed:31020314). Domain AR2 interacts with a large number of other proteins and may serve as a platform to recruit these factors for transcriptional regulation (PubMed:31127279). Involved in phage lambda N-mediated transcriptional antitermination. Also important for coordinating the cellular responses to DNA damage by coupling the processes of nucleotide excision repair and translesion synthesis to transcription...

## Biological Role

Repressed by argR (protein.P0A6D0), crp (protein.P0ACJ8), nac (protein.Q47005). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFF6|protein.P0AFF6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nusA; function=+
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `S` - regulator=ArgR; target=nusA; function=-
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=nusA; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=nusA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010413,ECOCYC:EG10665,GeneID:947682`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3316039-3317526:-; feature_type=gene
