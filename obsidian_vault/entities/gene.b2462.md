---
entity_id: "gene.b2462"
entity_type: "gene"
name: "eutS"
source_database: "NCBI RefSeq"
source_id: "gene-b2462"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2462"
  - "eutS"
---

# eutS

`gene.b2462`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2462`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

eutS (gene.b2462) is a gene entity. It encodes eutS (protein.P63746). Encoded protein function: FUNCTION: A component of the bacterial microcompartment (BMC) shell dedicated to ethanolamine degradation. Its unusual hexameric shape may help form the BMC shell (Probable). Targets at least 2 proteins (EutC and EutE) to the interior of the BMC (By similarity). Proteins such as EutS containing circularly permuted BMC domains may play a key role in conferring heterogeneity and flexibility in this BMC (Probable). {ECO:0000250|UniProtKB:Q9ZFV7, ECO:0000305, ECO:0000305|PubMed:20044574}. EcoCyc product frame: G7292-MONOMER. EcoCyc synonyms: ypfE. Genomic coordinates: 2575470-2575805.

## Biological Role

Activated by ArgR-L-arginine DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-228), argR (protein.P0A6D0), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P63746|protein.P63746]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[complex.ecocyc.CPLX0-228|complex.ecocyc.CPLX0-228]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `S` - regulator=ArgR; target=eutS; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=eutS; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0008108,ECOCYC:G7292,GeneID:946936`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2575470-2575805:-; feature_type=gene
