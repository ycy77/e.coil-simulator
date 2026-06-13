---
entity_id: "gene.b4087"
entity_type: "gene"
name: "alsA"
source_database: "NCBI RefSeq"
source_id: "gene-b4087"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4087"
  - "alsA"
---

# alsA

`gene.b4087`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4087`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

alsA (gene.b4087) is a gene entity. It encodes alsA (protein.P32721). Encoded protein function: FUNCTION: Part of the ABC transporter complex AlsBAC involved in D-allose import. Probably responsible for energy coupling to the transport system. {ECO:0000269|PubMed:9401019}. EcoCyc product frame: YJCW-MONOMER. EcoCyc synonyms: yjcW. Genomic coordinates: 4309448-4310980. EcoCyc protein note: alsA encodes the predicted ATP binding subunit of a D-allose ABC transporter . alsA contains fused ATP-binding cassette domains (ABC-ABC)

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32721|protein.P32721]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=alsA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013394,ECOCYC:EG11959,GeneID:948593`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4309448-4310980:-; feature_type=gene
