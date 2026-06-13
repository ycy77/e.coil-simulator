---
entity_id: "gene.b0348"
entity_type: "gene"
name: "mhpB"
source_database: "NCBI RefSeq"
source_id: "gene-b0348"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0348"
  - "mhpB"
---

# mhpB

`gene.b0348`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0348`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mhpB (gene.b0348) is a gene entity. It encodes mhpB (protein.P0ABR9). Encoded protein function: FUNCTION: Catalyzes the non-heme iron(II)-dependent oxidative cleavage of 2,3-dihydroxyphenylpropionic acid and 2,3-dihydroxicinnamic acid into 2-hydroxy-6-ketononadienedioate and 2-hydroxy-6-ketononatrienedioate, respectively. {ECO:0000269|PubMed:8399388, ECO:0000269|PubMed:8752345}. EcoCyc product frame: DHPDIOXYGEN-MONOMER. Genomic coordinates: 370277-371221.

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

- `encodes` --> [[protein.P0ABR9|protein.P0ABR9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=mhpB; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=mhpB; function=+
- `activates` <-- [[protein.P77569|protein.P77569]] `RegulonDB` `C` - regulator=MhpR; target=mhpB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001198,ECOCYC:M011,GeneID:945047`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:370277-371221:+; feature_type=gene
