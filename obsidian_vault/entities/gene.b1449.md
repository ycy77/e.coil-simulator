---
entity_id: "gene.b1449"
entity_type: "gene"
name: "curA"
source_database: "NCBI RefSeq"
source_id: "gene-b1449"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1449"
  - "curA"
---

# curA

`gene.b1449`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1449`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

curA (gene.b1449) is a gene entity. It encodes curA (protein.P76113). Encoded protein function: FUNCTION: Catalyzes the metal-independent reduction of curcumin to dihydrocurcumin (DHC) as an intermediate product, followed by further reduction to tetrahydrocurcumin (THC) as an end product. It also acts on 3-octene-2-one, 3-hepten-2-one, resveratrol, and trans-2-octenal. {ECO:0000269|PubMed:21467222}. EcoCyc product frame: G6760-MONOMER. EcoCyc synonyms: yncB. Genomic coordinates: 1519027-1520064.

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76113|protein.P76113]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=curA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004834,ECOCYC:G6760,GeneID:946012`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1519027-1520064:+; feature_type=gene
