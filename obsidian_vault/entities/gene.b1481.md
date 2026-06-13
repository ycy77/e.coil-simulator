---
entity_id: "gene.b1481"
entity_type: "gene"
name: "bdm"
source_database: "NCBI RefSeq"
source_id: "gene-b1481"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1481"
  - "bdm"
---

# bdm

`gene.b1481`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1481`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bdm (gene.b1481) is a gene entity. It encodes bdm (protein.P76127). Encoded protein function: Protein bdm (Biofilm-dependent modulation protein) EcoCyc product frame: G6776-MONOMER. EcoCyc synonyms: yddX. Genomic coordinates: 1556065-1556280. EcoCyc protein note: Bdm appears to be involved in regulating flagellar biosynthesis . bdm is a member of the Rcs regulon . It was originally reported that expression of bdm is reduced within biofilms and decreased by high osmolarity . However, other studies agree that expression is increased by high osmolarity and that the increase is RcsB-dependent . Expression of bdm is also upregulated by acid treatment . In addition, overexpression of bdm from a multicopy plasmid leads to enhanced biofilm formation . bdm mRNA is degraded by CPLX0-3281; the sustained increase in bdm mRNA levels upon osmotic upshift requires downregulation of RNase III activity . Gene expression analysis of a bdm mutant compared to wild type shows downregulation of a number of genes involved in flagellar biosynthesis, chemotaxis and motility. A bdm deletion strain does not have a growth defect, but shows impaired motility . Bdm: "biofilm-dependent modulation"

## Biological Role

Activated by rcsB (protein.P0DMC7).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76127|protein.P76127]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0DMC7|protein.P0DMC7]] `RegulonDB` `S` - regulator=RcsB; target=bdm; function=+

## External IDs

- `Dbxref:ASAP:ABE-0004938,ECOCYC:G6776,GeneID:946041`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1556065-1556280:-; feature_type=gene
