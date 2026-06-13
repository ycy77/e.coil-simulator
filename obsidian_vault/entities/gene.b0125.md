---
entity_id: "gene.b0125"
entity_type: "gene"
name: "hpt"
source_database: "NCBI RefSeq"
source_id: "gene-b0125"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0125"
  - "hpt"
---

# hpt

`gene.b0125`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0125`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hpt (gene.b0125) is a gene entity. It encodes hpt (protein.P0A9M2). Encoded protein function: FUNCTION: Purine salvage pathway enzyme which catalyzes the transfer of the ribosyl-5-phosphate group from 5-phospho-alpha-D-ribose 1-diphosphate (PRPP) to the N9 position of hypoxanthine to yield IMP (inosine 5'-monophosphate). To a lesser extent, can also act on guanine leading to GMP, but shows a highly less efficient activity with xanthine. {ECO:0000269|PubMed:12070315}. EcoCyc product frame: HYPOXANPRIBOSYLTRAN-MONOMER. Genomic coordinates: 141431-141967.

## Biological Role

Activated by rpoD (protein.P00579), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9M2|protein.P0A9M2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=hpt; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=hpt; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000440,ECOCYC:EG20098,GeneID:946624`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:141431-141967:+; feature_type=gene
