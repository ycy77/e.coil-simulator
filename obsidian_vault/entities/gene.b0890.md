---
entity_id: "gene.b0890"
entity_type: "gene"
name: "ftsK"
source_database: "NCBI RefSeq"
source_id: "gene-b0890"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0890"
  - "ftsK"
---

# ftsK

`gene.b0890`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0890`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ftsK (gene.b0890) is a gene entity. It encodes ftsK (protein.P46889). Encoded protein function: FUNCTION: Essential cell division protein that coordinates cell division and chromosome segregation. The N-terminus is involved in assembly of the cell-division machinery. The C-terminus functions as a DNA motor that moves dsDNA in an ATP-dependent manner towards the dif recombination site, which is located within the replication terminus region. Translocation stops specifically at Xer-dif sites, where FtsK interacts with the Xer recombinase, allowing activation of chromosome unlinking by recombination. FtsK orienting polar sequences (KOPS) guide the direction of DNA translocation. FtsK can remove proteins from DNA as it translocates, but translocation stops specifically at XerCD-dif site, thereby preventing removal of XerC and XerD from dif. Stoppage of translocation is accompanied by a reduction in ATPase activity. Also stimulates topoisomerase 4 activity. Required for the targeting of FtsQ, FtsL and FtsI to the septum. {ECO:0000269|PubMed:11703663, ECO:0000269|PubMed:11832210, ECO:0000269|PubMed:15522074, ECO:0000269|PubMed:16553881, ECO:0000269|PubMed:18363794, ECO:0000269|PubMed:19246541, ECO:0000269|PubMed:19854947, ECO:0000269|PubMed:20081205, ECO:0000269|PubMed:21371996, ECO:0000269|PubMed:9723913, ECO:0000269|PubMed:9829960}. EcoCyc product frame: G6464-MONOMER...

## Biological Role

Repressed by lexA (protein.P0A7C2). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P46889|protein.P46889]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ftsK; function=+
- `represses` <-- [[protein.P0A7C2|protein.P0A7C2]] `RegulonDB` `S` - regulator=LexA; target=ftsK; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003027,ECOCYC:G6464,GeneID:945102`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:933224-937213:+; feature_type=gene
