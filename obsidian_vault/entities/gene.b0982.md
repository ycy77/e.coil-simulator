---
entity_id: "gene.b0982"
entity_type: "gene"
name: "etp"
source_database: "NCBI RefSeq"
source_id: "gene-b0982"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0982"
  - "etp"
---

# etp

`gene.b0982`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0982`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

etp (gene.b0982) is a gene entity. It encodes etp (protein.P0ACZ2). Encoded protein function: FUNCTION: Dephosphorylates etk. EcoCyc product frame: G6503-MONOMER. EcoCyc synonyms: yccY. Genomic coordinates: 1044230-1044676. EcoCyc protein note: Etk and Etp are a tyrosine kinase-tyrosine phosphatase pair. Etp can dephosphorylate the phosphotyrosine residues of Etk in vitro. In contrast to the related phosphatase, Wzb, Etp has minimal effect on biosynthesis of colanic acid . Mutations in etp lead to the accumulation of RpoH in an inactive phosphorylated form, and thus, decreased transcription of heat shock genes. etp mutant strains accumulate phosphoproteins including Etk, and display a temperature-sensitive growth phenotype at 43 °C . The operon encoding YmcD, YmcC, YmcB, YmcA, YccZ, Etp, and Etk was characterized in the enteropathogenic E. coli strain O127:H6. There, all seven gene products are required for the production of the G4C capsule polysaccharide . That operon may not be expressed in E. coli K-12, because the promoter region that was mapped in E. coli O127:H6 is inactivated in E. coli K-12 by the insertion of an IS1 element 15 bp upstream of the YmcD translation start site . Etp: "E. coli phosphotyrosine phosphatase"

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACZ2|protein.P0ACZ2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003312,ECOCYC:G6503,GeneID:945236`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1044230-1044676:-; feature_type=gene
