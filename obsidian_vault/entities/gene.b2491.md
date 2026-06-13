---
entity_id: "gene.b2491"
entity_type: "gene"
name: "hyfR"
source_database: "NCBI RefSeq"
source_id: "gene-b2491"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2491"
  - "hyfR"
---

# hyfR

`gene.b2491`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2491`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hyfR (gene.b2491) is a gene entity. It encodes hyfR (protein.P71229). Encoded protein function: FUNCTION: A transcriptional activator of its own operon; when overexpressed operon expression is strongly enhanced by low pH (under pH 6.0), strongly inhibited by O(2) but only weakly stimulated by fumarate (PubMed:12426353, PubMed:14702328). Expression in situ is very weak (PubMed:12426353, PubMed:14702328). {ECO:0000269|PubMed:12426353, ECO:0000269|PubMed:14702328, ECO:0000305|PubMed:9387241}. EcoCyc product frame: G7308-MONOMER. Genomic coordinates: 2611900-2613912. EcoCyc protein note: HyfR , "hydrogenase four regulator," controls the expression of genes responsible for the proton-translocating formate hydrogenase system and for formate transport under anaerobiosis, low pH, and post-exponential growth conditions . As a member of the group of σ54-dependent transcriptional regulators, HyfR contains three domains: the sensory domain, located in the N terminus; the central domain, involved in open complex formation, ATP hydrolysis, and interaction with σ54, and the C-terminal domain, which contains a helix-turn-helix motif for DNA binding . An iron-sulfur cluster and a metal cofactor (possibly a similar metal or formate) have been proposed as the signals sensed by HyfR . HyfR shows 46% identity to FhlA, a member of the same group...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P71229|protein.P71229]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008204,ECOCYC:G7308,GeneID:948886`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2611900-2613912:+; feature_type=gene
