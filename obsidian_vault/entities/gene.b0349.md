---
entity_id: "gene.b0349"
entity_type: "gene"
name: "mhpC"
source_database: "NCBI RefSeq"
source_id: "gene-b0349"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0349"
  - "mhpC"
---

# mhpC

`gene.b0349`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0349`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mhpC (gene.b0349) is a gene entity. It encodes mhpC (protein.P77044). Encoded protein function: FUNCTION: Catalyzes the cleavage of the C5-C6 bond of 2-hydroxy-6-oxononadienedioate and 2-hydroxy-6-oxononatrienedioate, a dienol ring fission product of the bacterial meta-cleavage pathway for degradation of phenylpropionic acid. MhpC shows some selectivity for the carboxylate of the side chain. {ECO:0000269|PubMed:15663941, ECO:0000269|PubMed:9098055, ECO:0000269|PubMed:9315862}. EcoCyc product frame: MHPCHYDROL-MONOMER. Genomic coordinates: 371239-372105.

## Biological Role

Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), mhpR (protein.P77569).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01220` Degradation of aromatic compounds (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77044|protein.P77044]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=mhpC; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=mhpC; function=+
- `activates` <-- [[protein.P77569|protein.P77569]] `RegulonDB` `C` - regulator=MhpR; target=mhpC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001201,ECOCYC:M012,GeneID:944954`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:371239-372105:+; feature_type=gene
