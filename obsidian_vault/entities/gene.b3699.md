---
entity_id: "gene.b3699"
entity_type: "gene"
name: "gyrB"
source_database: "NCBI RefSeq"
source_id: "gene-b3699"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3699"
  - "gyrB"
---

# gyrB

`gene.b3699`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3699`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gyrB (gene.b3699) is a gene entity. It encodes gyrB (protein.P0AES6). Encoded protein function: FUNCTION: DNA gyrase negatively supercoils closed circular double-stranded DNA in an ATP-dependent manner to maintain chromosomes in an underwound state (PubMed:12051842, PubMed:12051843, PubMed:1323022, PubMed:18642932, PubMed:186775, PubMed:19060136, PubMed:19965760, PubMed:20356737, PubMed:20675723, PubMed:22457353, PubMed:23294697, PubMed:23352267, PubMed:24386374, PubMed:25202966, PubMed:25849408, PubMed:3031051, PubMed:7811004, PubMed:8248233, PubMed:8621650, PubMed:9657678). This makes better substrates for topoisomerase 4 (ParC and ParE) which is the main enzyme that unlinks newly replicated chromosomes in E.coli (PubMed:9334322). Gyrase catalyzes the interconversion of other topological isomers of double-stranded DNA rings, including catenanes (PubMed:22457352). Relaxes negatively supercoiled DNA in an ATP-independent manner (PubMed:337300). E.coli gyrase has higher supercoiling activity than other characterized bacterial gyrases; at comparable concentrations E.coli gyrase introduces more supercoils faster than M.tuberculosis gyrase, while M.tuberculosis gyrase has higher decatenation than supercoiling activity compared to E.coli (PubMed:22457352). E.coli makes 15% more negative supercoils in pBR322 plasmid DNA than S.typhimurium; the S...

## Biological Role

Repressed by fis (protein.P0A6R3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AES6|protein.P0AES6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=gyrB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012093,ECOCYC:EG10424,GeneID:948211`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3877705-3880119:-; feature_type=gene
