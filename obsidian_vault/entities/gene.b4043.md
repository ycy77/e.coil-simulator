---
entity_id: "gene.b4043"
entity_type: "gene"
name: "lexA"
source_database: "NCBI RefSeq"
source_id: "gene-b4043"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4043"
  - "lexA"
---

# lexA

`gene.b4043`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4043`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lexA (gene.b4043) is a gene entity. It encodes lexA (protein.P0A7C2). Encoded protein function: FUNCTION: Represses a number of genes involved in the response to DNA damage (SOS response), including recA and lexA. Binds to the 16 bp palindromic sequence 5'-CTGTATATATATACAG-3'. In the presence of single-stranded DNA, RecA interacts with LexA causing an autocatalytic cleavage which disrupts the DNA-binding part of LexA, leading to derepression of the SOS regulon and eventually DNA repair. Implicated in hydroxy radical-mediated cell death induced by hydroxyurea treatment (PubMed:20005847). The SOS response controls an apoptotic-like death (ALD) induced (in the absence of the mazE-mazF toxin-antitoxin module) in response to DNA damaging agents that is mediated by RecA and LexA (PubMed:22412352). Genetic interactions among priB, dam, lexA, nagC, polA, rdgB, rdgB, rep and uup link the PriA-PriB replication restart pathway to DNA double-strand break repair (PubMed:36326440). {ECO:0000255|HAMAP-Rule:MF_00015, ECO:0000269|PubMed:20005847, ECO:0000269|PubMed:22412352, ECO:0000269|PubMed:36326440, ECO:0000269|PubMed:7027255, ECO:0000269|PubMed:7027256}. EcoCyc product frame: PD00205. EcoCyc synonyms: exrA, spr, tsl, umuA. Genomic coordinates: 4257115-4257723.

## Biological Role

Repressed by lexA (protein.P0A7C2). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7C2|protein.P0A7C2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=lexA; function=+
- `represses` <-- [[protein.P0A7C2|protein.P0A7C2]] `RegulonDB` `C` - regulator=LexA; target=lexA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013241,ECOCYC:EG10533,GeneID:948544`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4257115-4257723:+; feature_type=gene
