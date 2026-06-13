---
entity_id: "gene.b2668"
entity_type: "gene"
name: "ygaP"
source_database: "NCBI RefSeq"
source_id: "gene-b2668"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2668"
  - "ygaP"
---

# ygaP

`gene.b2668`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2668`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ygaP (gene.b2668) is a gene entity. It encodes ygaP (protein.P55734). Encoded protein function: FUNCTION: Transferase that catalyzes the transfer of sulfur from thiosulfate to cyanide to form thiocyanate (PubMed:24958726, PubMed:25204500). May have a role in the detoxification of cyanide to the less toxic thiocyanate (PubMed:24958726). May also be involved, directly or indirectly, in the transport of the thiocyanate produced across the membrane from the cytoplasm to the periplasm (PubMed:24958726). {ECO:0000269|PubMed:24958726, ECO:0000269|PubMed:25204500}. EcoCyc product frame: G7398-MONOMER. Genomic coordinates: 2797520-2798044.

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P55734|protein.P55734]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ygaP; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0008786,ECOCYC:G7398,GeneID:947135`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2797520-2798044:+; feature_type=gene
