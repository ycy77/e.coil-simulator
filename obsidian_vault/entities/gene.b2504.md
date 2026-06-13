---
entity_id: "gene.b2504"
entity_type: "gene"
name: "yfgG"
source_database: "NCBI RefSeq"
source_id: "gene-b2504"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2504"
  - "yfgG"
---

# yfgG

`gene.b2504`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2504`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfgG (gene.b2504) is a gene entity. It encodes yfgG (protein.P64545). Encoded protein function: Protein YfgG EcoCyc product frame: G7315-MONOMER. Genomic coordinates: 2629290-2629481. EcoCyc protein note: Both knockout and overexpression data suggest that YfgG is involved in tolerance to nickel and cobalt stress .

## Biological Role

Activated by rpoD (protein.P00579), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64545|protein.P64545]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=yfgG; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yfgG; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0008247,ECOCYC:G7315,GeneID:946980`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2629290-2629481:+; feature_type=gene
