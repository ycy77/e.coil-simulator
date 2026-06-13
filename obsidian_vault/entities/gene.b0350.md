---
entity_id: "gene.b0350"
entity_type: "gene"
name: "mhpD"
source_database: "NCBI RefSeq"
source_id: "gene-b0350"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0350"
  - "mhpD"
---

# mhpD

`gene.b0350`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0350`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mhpD (gene.b0350) is a gene entity. It encodes mhpD (protein.P77608). Encoded protein function: FUNCTION: Catalyzes the conversion of 2-hydroxypentadienoic acid (enolic form of 2-oxopent-4-enoate) to 4-hydroxy-2-ketopentanoic acid. {ECO:0000269|PubMed:9492273}. EcoCyc product frame: MHPDHYDROL-MONOMER. EcoCyc synonyms: mhpS. Genomic coordinates: 372115-372924.

## Biological Role

Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), mhpR (protein.P77569).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00621` Dioxin degradation (KEGG)
- `eco00622` Xylene degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01220` Degradation of aromatic compounds (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77608|protein.P77608]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=mhpD; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=mhpD; function=+
- `activates` <-- [[protein.P77569|protein.P77569]] `RegulonDB` `C` - regulator=MhpR; target=mhpD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001205,ECOCYC:M013,GeneID:944768`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:372115-372924:+; feature_type=gene
