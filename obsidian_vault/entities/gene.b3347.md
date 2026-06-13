---
entity_id: "gene.b3347"
entity_type: "gene"
name: "fkpA"
source_database: "NCBI RefSeq"
source_id: "gene-b3347"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3347"
  - "fkpA"
---

# fkpA

`gene.b3347`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3347`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fkpA (gene.b3347) is a gene entity. It encodes fkpA (protein.P45523). Encoded protein function: FUNCTION: PPIases accelerate the folding of proteins. It catalyzes the cis-trans isomerization of proline imidic peptide bonds in oligopeptides. EcoCyc product frame: G7716-MONOMER. EcoCyc synonyms: yzzS. Genomic coordinates: 3476607-3477419.

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45523|protein.P45523]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=fkpA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010938,ECOCYC:G7716,GeneID:947850`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3476607-3477419:-; feature_type=gene
