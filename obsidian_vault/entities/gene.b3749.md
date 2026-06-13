---
entity_id: "gene.b3749"
entity_type: "gene"
name: "rbsA"
source_database: "NCBI RefSeq"
source_id: "gene-b3749"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3749"
  - "rbsA"
---

# rbsA

`gene.b3749`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3749`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rbsA (gene.b3749) is a gene entity. It encodes rbsA (protein.P04983). Encoded protein function: FUNCTION: Part of the ABC transporter complex RbsABC involved in ribose import. Responsible for energy coupling to the transport system. {ECO:0000255|HAMAP-Rule:MF_01716, ECO:0000269|PubMed:25533465, ECO:0000269|PubMed:6327617, ECO:0000269|PubMed:8762140}. EcoCyc product frame: RBSA-MONOMER. EcoCyc synonyms: rbsT, rbsP. Genomic coordinates: 3933778-3935283. EcoCyc protein note: RbsA is the ATP-binding subunit of a high affinity ribose uptake system; RbsA contains a signature motifs conserved in ATP-binding cassette (ABC) proteins; RbsA contains an ABC-ABC domain

## Biological Role

Repressed by dsrA (gene.b1954), rbsR (protein.P0ACQ0).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P04983|protein.P04983]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[gene.b1954|gene.b1954]] `RegulonDB` `S` - regulator=DsrA; target=rbsA; function=-
- `represses` <-- [[protein.P0ACQ0|protein.P0ACQ0]] `RegulonDB` `C` - regulator=RbsR; target=rbsA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012259,ECOCYC:EG10814,GeneID:948264`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3933778-3935283:+; feature_type=gene
