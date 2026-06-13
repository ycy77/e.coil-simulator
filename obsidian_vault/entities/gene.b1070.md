---
entity_id: "gene.b1070"
entity_type: "gene"
name: "flgN"
source_database: "NCBI RefSeq"
source_id: "gene-b1070"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1070"
  - "flgN"
---

# flgN

`gene.b1070`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1070`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

flgN (gene.b1070) is a gene entity. It encodes flgN (protein.P43533). Encoded protein function: FUNCTION: Required for the efficient initiation of filament assembly. {ECO:0000250}. EcoCyc product frame: G6562-MONOMER. Genomic coordinates: 1129414-1129830. EcoCyc protein note: FliT, along with FliS and FlgN, are cytoplasmic, substrate-specific chaperones of the flagellar export system. They share several similarities with other type III cytoplasmic chaperone family members . Affinity blot analysis showed that FlgN binds in vitro to hook-filament junction proteins FlgK and FlgL suggesting that FlgN may act as a chaperone which aids in the export and prevents premature aggregation of the FlgK and FlgL hook-filament junction proteins . Gel filtration chromatography indicate that FlgN exists as a homodimer in the cytosol and that these homodimers bind to monomers of FlgK and FlgL to form heterotrimeric chaperone-substrate complexes .

## Biological Role

Repressed by csgD (protein.P52106).

## Enriched Pathways

- `eco02040` Flagellar assembly (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P43533|protein.P43533]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P52106|protein.P52106]] `RegulonDB` `S` - regulator=CsgD; target=flgN; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003632,ECOCYC:G6562,GeneID:945634`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1129414-1129830:-; feature_type=gene
