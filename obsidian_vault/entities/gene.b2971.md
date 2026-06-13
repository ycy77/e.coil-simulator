---
entity_id: "gene.b2971"
entity_type: "gene"
name: "yghG"
source_database: "NCBI RefSeq"
source_id: "gene-b2971"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2971"
  - "yghG"
---

# yghG

`gene.b2971`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2971`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yghG (gene.b2971) is a gene entity. It encodes yghG (protein.Q46835). Encoded protein function: FUNCTION: Involved in a type II secretion system (T2SS, formerly general secretion pathway, GSP) for the export of folded proteins across the outer membrane. In a functional T2SS this subunit helps assemble the outer membrane channel. {ECO:0000305}. EcoCyc product frame: G7538-MONOMER. EcoCyc synonyms: gspSβ. Genomic coordinates: 3113067-3113477. EcoCyc protein note: YghG is a verified lipoprotein according to unpublished data by S. Matsuyama et al. (cited in ). In enterotoxigenic E. coli (ETEC) strain H10407 YghG (renamed GspSβ) is the outer membrane pilotin for a virulence-associated type II secretion system (T2SSβ) . YghG from E. coli K-12 MG1655 and ETEC H10407 are 99% identical over their entire length . Examination of the T2SSβ-encoding loci in various pathogenic and nonpathogenic E. coli strains indicates that the K-12 MG1655 strain carries remnants of the pathway but has experienced a deletion which removed a large internal region of the T2SSβ-encoding operon .

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46835|protein.Q46835]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yghG; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009748,ECOCYC:G7538,GeneID:947470`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3113067-3113477:-; feature_type=gene
