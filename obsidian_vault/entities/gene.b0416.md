---
entity_id: "gene.b0416"
entity_type: "gene"
name: "nusB"
source_database: "NCBI RefSeq"
source_id: "gene-b0416"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0416"
  - "nusB"
---

# nusB

`gene.b0416`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0416`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nusB (gene.b0416) is a gene entity. It encodes nusB (protein.P0A780). Encoded protein function: FUNCTION: Part of the processive rRNA transcription and antitermination complex (rrnTAC). The complex forms an RNA-chaperone ring around the RNA exit tunnel of RNA polymerase (RNAP). It supports rapid transcription and antitermination of rRNA operons, cotranscriptional rRNA folding, and annealing of distal rRNA regions to allow correct ribosome biogenesis (PubMed:32871103). Involved in transcription antitermination. Required for transcription of ribosomal RNA (rRNA) genes. Binds specifically to the boxA antiterminator sequence of the ribosomal RNA (rrn) operons (PubMed:11884128, PubMed:14973028, PubMed:15716433, PubMed:16109710, PubMed:7045592, PubMed:7678781). The affinity of NusB for the boxA RNA sequence is significantly increased in the presence of the ribosomal protein S10 (PubMed:11884128, PubMed:16109710). NusB may serve as a loading factor that ensures efficient entry of S10 into the transcription complexes (PubMed:19111659). It also modulates the rrn boxA-mediated transcription elongation rates (PubMed:10383769). {ECO:0000269|PubMed:10383769, ECO:0000269|PubMed:11884128, ECO:0000269|PubMed:14973028, ECO:0000269|PubMed:15716433, ECO:0000269|PubMed:16109710, ECO:0000269|PubMed:19111659, ECO:0000269|PubMed:32871103, ECO:0000269|PubMed:7045592, ECO:0000269|PubMed:7678781}...

## Biological Role

Repressed by lrp (protein.P0ACJ0), nac (protein.Q47005). Activated by rpoH (protein.P0AGB3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A780|protein.P0A780]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=nusB; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=nusB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001447,ECOCYC:EG10666,GeneID:945054`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:435137-435556:+; feature_type=gene
