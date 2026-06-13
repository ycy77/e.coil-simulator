---
entity_id: "gene.b2955"
entity_type: "gene"
name: "hemW"
source_database: "NCBI RefSeq"
source_id: "gene-b2955"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2955"
  - "hemW"
---

# hemW

`gene.b2955`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2955`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hemW (gene.b2955) is a gene entity. It encodes hemW (protein.P52062). Encoded protein function: FUNCTION: Probably acts as a heme chaperone, transferring heme to the NarI subunit of the respiratory enzyme nitrate reductase; transfer may be stimulated by NADH. Binds one molecule of heme per monomer, possibly covalently. Heme binding is not affected by either [4Fe-4S] or S-adenosyl-L-methionine (SAM)-binding. Does not have coproporphyrinogen III dehydrogenase activity in vitro (PubMed:29282292). Binds 1 [4Fe-4S] cluster. The cluster is coordinated with 3 cysteines and an exchangeable S-adenosyl-L-methionine (Probable). {ECO:0000269|PubMed:29282292, ECO:0000305|PubMed:29282292}. EcoCyc product frame: G7531-MONOMER. EcoCyc synonyms: yggW. Genomic coordinates: 3097267-3098403.

## Biological Role

Activated by rpoH (protein.P0AGB3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P52062|protein.P52062]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=hemW; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009694,ECOCYC:G7531,GeneID:947446`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3097267-3098403:+; feature_type=gene
