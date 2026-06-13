---
entity_id: "gene.b4350"
entity_type: "gene"
name: "hsdR"
source_database: "NCBI RefSeq"
source_id: "gene-b4350"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4350"
  - "hsdR"
---

# hsdR

`gene.b4350`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4350`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hsdR (gene.b4350) is a gene entity. It encodes hsdR (protein.P08956). Encoded protein function: FUNCTION: The subtype A restriction (R) subunit of a type I restriction enzyme that recognizes 5'-AACN(6)GTGC-3' and cleaves a random distance away. The R subunit is required for both endonuclease and ATPase activities but not for modification (PubMed:12654995, PubMed:4868368, PubMed:6255295, PubMed:9033396). Has endonucleolytic activity that requires Mg(2+), ATP and S-adenosyl-L-methionine (SAM); ATP can be replaced by dATP, no tested molecule could substitute for SAM. Generates double-stranded DNA with no nicks, by cutting one strand then the other within a few seconds. Cleaves only non-methylated DNA, hemi-methylated and fully methylated DNA are not substrates (PubMed:4868368, PubMed:9033396). After locating a non-methylated recognition site, the enzyme complex serves as a molecular motor that translocates DNA in an ATP-dependent manner until a collision occurs that triggers cleavage (PubMed:6248234). {ECO:0000269|PubMed:4868368, ECO:0000269|PubMed:6248234, ECO:0000269|PubMed:6255295, ECO:0000269|PubMed:9033396, ECO:0000303|PubMed:12654995}. EcoCyc product frame: EG10459-MONOMER. EcoCyc synonyms: hsp, hsr. Genomic coordinates: 4583249-4586761. EcoCyc protein note: HsdR is the restriction endonuclease component of the EcoKI restriction-modification system .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P08956|protein.P08956]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0014264,ECOCYC:EG10459,GeneID:948878`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4583249-4586761:-; feature_type=gene
