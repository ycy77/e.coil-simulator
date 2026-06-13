---
entity_id: "gene.b4052"
entity_type: "gene"
name: "dnaB"
source_database: "NCBI RefSeq"
source_id: "gene-b4052"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4052"
  - "dnaB"
---

# dnaB

`gene.b4052`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4052`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dnaB (gene.b4052) is a gene entity. It encodes dnaB (protein.P0ACB0). Encoded protein function: FUNCTION: The main replicative DNA helicase, it participates in initiation and elongation during chromosome replication. Travels ahead of the DNA replisome, separating dsDNA into templates for DNA synthesis. A processive ATP-dependent 5'-3' DNA helicase that acts on preformed replication forks (have single-stranded (ss)DNA tails) (PubMed:3007474). ATP is the best nucleotide for helicase activity; GTP, CTP, dCTP and dATP are poor substitutes (PubMed:3007474). Participates with DNA primase DnaG in primer RNA (pRNA) synthesis during initiation of DNA replication (PubMed:7532169). Has DNA-dependent ATPase activity (PubMed:7532169). Is loaded onto ssDNA via the action of DnaC; ssDNA binds to the central pore in the DnaB(6):DnaC(6) complex, making contacts with both subunits (PubMed:30797687). Required for restart of stalled replication forks, which reloads the DnaB replicative helicase on sites other than the origin of replication (PubMed:6454139, PubMed:8663104, PubMed:8663105). {ECO:0000269|PubMed:3007474, ECO:0000269|PubMed:30797687, ECO:0000269|PubMed:7532169}.; FUNCTION: Deletion or mutations in this gene were selected in directed evolution experiments for resistance to intense ionizing radiation (3000 Gy) (PubMed:24596148). {ECO:0000269|PubMed:24596148}...

## Enriched Pathways

- `eco03030` DNA replication (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACB0|protein.P0ACB0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013269,ECOCYC:EG10236,GeneID:948555`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4264314-4265729:+; feature_type=gene
