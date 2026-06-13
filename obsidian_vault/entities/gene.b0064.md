---
entity_id: "gene.b0064"
entity_type: "gene"
name: "araC"
source_database: "NCBI RefSeq"
source_id: "gene-b0064"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0064"
  - "araC"
---

# araC

`gene.b0064`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0064`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

araC (gene.b0064) is a gene entity. It encodes araC (protein.P0A9E0). Encoded protein function: FUNCTION: Transcription factor that regulates the expression of several genes involved in the transport and metabolism of L-arabinose (PubMed:1447222, PubMed:2231717, PubMed:2962192, PubMed:328165, PubMed:4362626, PubMed:6251457, PubMed:6319708). Functions both as a positive and a negative regulator (PubMed:328165, PubMed:6251457). In the presence of arabinose, activates the expression of the araBAD, araE, araFGH and araJ promoters (PubMed:1447222, PubMed:2231717, PubMed:2962192, PubMed:328165, PubMed:4362626, PubMed:6251457, PubMed:6319708). In the absence of arabinose, negatively regulates the araBAD operon (PubMed:6251457). Represses its own transcription (PubMed:328165). Acts by binding directly to DNA (PubMed:1447222, PubMed:2531226, PubMed:2962192, PubMed:4943786, PubMed:6251457). {ECO:0000269|PubMed:1447222, ECO:0000269|PubMed:2231717, ECO:0000269|PubMed:2531226, ECO:0000269|PubMed:2962192, ECO:0000269|PubMed:328165, ECO:0000269|PubMed:4362626, ECO:0000269|PubMed:4943786, ECO:0000269|PubMed:6251457, ECO:0000269|PubMed:6319708}. EcoCyc product frame: PD00242. Genomic coordinates: 70387-71265.

## Biological Role

Repressed by araC (protein.P0A9E0), xylR (protein.P0ACI3). Activated by rpoD (protein.P00579), araC (protein.P0A9E0), crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9E0|protein.P0A9E0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=araC; function=+
- `activates` <-- [[protein.P0A9E0|protein.P0A9E0]] `RegulonDB` `C` - regulator=AraC; target=araC; function=-+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=araC; function=+
- `represses` <-- [[protein.P0A9E0|protein.P0A9E0]] `RegulonDB` `C` - regulator=AraC; target=araC; function=-+
- `represses` <-- [[protein.P0ACI3|protein.P0ACI3]] `RegulonDB` `S` - regulator=XylR; target=araC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0000236,ECOCYC:EG10054,GeneID:944780`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:70387-71265:+; feature_type=gene
