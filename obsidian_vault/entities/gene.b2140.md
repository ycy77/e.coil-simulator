---
entity_id: "gene.b2140"
entity_type: "gene"
name: "dusC"
source_database: "NCBI RefSeq"
source_id: "gene-b2140"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2140"
  - "dusC"
---

# dusC

`gene.b2140`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2140`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dusC (gene.b2140) is a gene entity. It encodes dusC (protein.P33371). Encoded protein function: FUNCTION: Catalyzes the synthesis of 5,6-dihydrouridine (D), a modified base found in the D-loop of most tRNAs, via the reduction of the C5-C6 double bond in target uridines. DusC specifically modifies U16 in tRNAs. {ECO:0000255|HAMAP-Rule:MF_02043, ECO:0000269|PubMed:11983710, ECO:0000269|PubMed:25902496}. EcoCyc product frame: EG12022-MONOMER. EcoCyc synonyms: yohI. Genomic coordinates: 2229438-2230385. EcoCyc protein note: EG11311-MONOMER (DusB) and DusC together account for about half of the 5,6-dihydrouridine modification observed in wild-type cellular tRNA, and EG11932-MONOMER (DusA) accounts for the other half . DusC specifically modifies U16 of the D loop in tRNAs. The site selectivity of the enzyme is conveyed by binding the tRNA substrate in a different orientation when compared to an enzyme that modifies U20, on the opposite side of the D loop . Crystal structures of DusC have been solved, showing an N-terminal catalytic TIM-barrel domain and a C-terminal tRNA binding domain . Crystal structures of DusC in complex with tRNAs elucidated the basis for modification site specificity of the enzyme...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33371|protein.P33371]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007074,ECOCYC:EG12022,GeneID:945458`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2229438-2230385:-; feature_type=gene
