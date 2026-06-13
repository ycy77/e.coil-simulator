---
entity_id: "gene.b0068"
entity_type: "gene"
name: "thiB"
source_database: "NCBI RefSeq"
source_id: "gene-b0068"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0068"
  - "thiB"
---

# thiB

`gene.b0068`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0068`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

thiB (gene.b0068) is a gene entity. It encodes thiB (protein.P31550). Encoded protein function: FUNCTION: Part of the ABC transporter complex ThiBPQ involved in thiamine import (PubMed:12175925). Binds thiamine, thiamine phosphate and thiamine diphosphate with high affinity (PubMed:12182833, PubMed:18177053). {ECO:0000269|PubMed:12175925, ECO:0000269|PubMed:12182833, ECO:0000269|PubMed:18177053}. EcoCyc product frame: SFUA-MONOMER. EcoCyc synonyms: yabL, sfuA, tbpA. Genomic coordinates: 74497-75480. EcoCyc protein note: thiB encodes the periplasmic, substrate binding protein of an ATP-dependent thiamin uptake system. Purified ThiB binds thiamine and its phosphate esters - thiamine phosphate and thiamine diphosphate . Purified ThiB binds thiamine with a 1:1 stoichiometry and with high affinity; KD = 0.8 µM . The crystal structure of ThiB consists of two domains linked by a flexible hinge region of two crossovers; thiamine phosphate binds in a cleft located between the two domains . Purified ThiB binds thiamine, thiamine phosphate and thiamine diphosphate with high affinity (KD = 3.8 nM, 2.3 nM and 7.4 nM respectively)...

## Biological Role

Repressed by sgrR (protein.P33595).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31550|protein.P31550]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P33595|protein.P33595]] `RegulonDB` `C` - regulator=SgrR; target=thiB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0000249,ECOCYC:EG11574,GeneID:946306`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:74497-75480:-; feature_type=gene
