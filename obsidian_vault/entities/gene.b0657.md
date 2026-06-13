---
entity_id: "gene.b0657"
entity_type: "gene"
name: "lnt"
source_database: "NCBI RefSeq"
source_id: "gene-b0657"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0657"
  - "lnt"
---

# lnt

`gene.b0657`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0657`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lnt (gene.b0657) is a gene entity. It encodes lnt (protein.P23930). Encoded protein function: FUNCTION: Catalyzes the phospholipid dependent N-acylation of the N-terminal cysteine of apolipoprotein, the last step in lipoprotein maturation (PubMed:2032623, PubMed:21676878, PubMed:28675161, PubMed:28885614). Utilizes a two-step reaction via a ping-pong mechanism (PubMed:21676878, PubMed:28675161). Lnt undergoes covalent modification in the presence of phospholipids, resulting in a thioester acyl-enzyme intermediate. It then transfers the acyl chain to the amine group of the N-terminal diacylglyceryl-modified cysteine of apolipoprotein, leading to the formation of mature triacylated lipoprotein (PubMed:21676878, PubMed:28675161). In vitro, can utilize the phospholipids phosphatidylethanolamine (PE), phosphatidylglycerol (PG), phosphatidic acid (PA) or cardiolipin (CL) (PubMed:2032623, PubMed:21676878). PE is the most efficient acyl donor (PubMed:21676878). {ECO:0000269|PubMed:2032623, ECO:0000269|PubMed:21676878, ECO:0000269|PubMed:28675161, ECO:0000269|PubMed:28885614, ECO:0000305|PubMed:8344936}. EcoCyc product frame: EG10168-MONOMER. EcoCyc synonyms: cutE. Genomic coordinates: 689343-690881...

## Biological Role

Activated by rpoH (protein.P0AGB3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23930|protein.P23930]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=lnt; function=+

## External IDs

- `Dbxref:ASAP:ABE-0002250,ECOCYC:EG10168,GeneID:946201`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:689343-690881:-; feature_type=gene
