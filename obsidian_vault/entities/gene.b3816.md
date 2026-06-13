---
entity_id: "gene.b3816"
entity_type: "gene"
name: "corA"
source_database: "NCBI RefSeq"
source_id: "gene-b3816"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3816"
  - "corA"
---

# corA

`gene.b3816`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3816`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

corA (gene.b3816) is a gene entity. It encodes corA (protein.P0ABI4). Encoded protein function: FUNCTION: Mediates influx of magnesium ions. Can also mediate cobalt and manganese uptake (PubMed:780341). Alternates between open and closed states. Activated by low cytoplasmic Mg(2+) levels. Inactive when cytoplasmic Mg(2+) levels are high (By similarity). {ECO:0000250|UniProtKB:Q9WZ31, ECO:0000269|PubMed:780341}. EcoCyc product frame: CORA-MONOMER. Genomic coordinates: 4001426-4002376. EcoCyc protein note: CorA is an inner membrane magnesium ion transporter . Kinetic analyses indicate that CorA is a constitutive magnesium, cobalt and manganese ion transport protein . A plasmid expressing corA from E.coli can complement a Salmonella enterica corA mutation and restore uptake of Co2+ and Mg2+ . CorA is comprised of a large periplasmic domain and three membrane spanning helices . The purified periplasmic domain of CorA functions as a homotetramer and is able to bind magnesium, cobalt and nickel ions . The well characterised CorA homolog from Salmonella enterica (which has 98% amino acid identity with E. coli CorA) mediates Mg2+ - Mg2+ exchange in addition to the import of magnesium, cobalt and nickel ions . CorA is dependent on the Sec pathway for membrane integration

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABI4|protein.P0ABI4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012464,ECOCYC:EG11463,GeneID:948351`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4001426-4002376:+; feature_type=gene
