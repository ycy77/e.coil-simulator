---
entity_id: "gene.b0951"
entity_type: "gene"
name: "pqiB"
source_database: "NCBI RefSeq"
source_id: "gene-b0951"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0951"
  - "pqiB"
---

# pqiB

`gene.b0951`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0951`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pqiB (gene.b0951) is a gene entity. It encodes pqiB (protein.P43671). Encoded protein function: FUNCTION: Forms a tunnel that spans the entire periplasmic space (PubMed:28388411). Could be implicated in lipid transport between the inner membrane and the outer membrane (PubMed:28388411). Binds phospholipids (PubMed:28388411). Required for outer membrane homeostasis (PubMed:28819315). Contributes to membrane integrity (PubMed:27795327). {ECO:0000269|PubMed:27795327, ECO:0000269|PubMed:28388411, ECO:0000269|PubMed:28819315}. EcoCyc product frame: G6491-MONOMER. EcoCyc synonyms: pqi5, pqi5B. Genomic coordinates: 1013259-1014899.

## Biological Role

Activated by rpoD (protein.P00579), soxS (protein.P0A9E2), marA (protein.P0ACH5), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P43671|protein.P43671]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=pqiB; function=+
- `activates` <-- [[protein.P0A9E2|protein.P0A9E2]] `RegulonDB` `C` - regulator=SoxS; target=pqiB; function=+
- `activates` <-- [[protein.P0ACH5|protein.P0ACH5]] `RegulonDB` `S` - regulator=MarA; target=pqiB; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=pqiB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0003221,ECOCYC:G6491,GeneID:945653`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1013259-1014899:+; feature_type=gene
