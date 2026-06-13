---
entity_id: "gene.b2419"
entity_type: "gene"
name: "yfeK"
source_database: "NCBI RefSeq"
source_id: "gene-b2419"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2419"
  - "yfeK"
---

# yfeK

`gene.b2419`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2419`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfeK (gene.b2419) is a gene entity. It encodes yfeK (protein.Q47702). Encoded protein function: Uncharacterized protein YfeK EcoCyc product frame: G7260-MONOMER. Genomic coordinates: 2537342-2537716. EcoCyc protein note: yfeK mRNA abundance is downregulated by the small RNAs MicA and RybB .

## Biological Role

Activated by rpoE (protein.P0AGB6), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q47702|protein.Q47702]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=yfeK; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yfeK; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007977,ECOCYC:G7260,GeneID:946876`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2537342-2537716:+; feature_type=gene
