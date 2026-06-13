---
entity_id: "gene.b0990"
entity_type: "gene"
name: "cspG"
source_database: "NCBI RefSeq"
source_id: "gene-b0990"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0990"
  - "cspG"
---

# cspG

`gene.b0990`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0990`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cspG (gene.b0990) is a gene entity. It encodes cspG (protein.P0A978). Encoded protein function: Cold shock-like protein CspG (CPS-G) EcoCyc product frame: G6511-MONOMER. Genomic coordinates: 1051461-1051673. EcoCyc protein note: Expression of cspG is induced upon cold shock , and synthesis of the CspG protein in response to cold shock is not inhibited by the presence of the protein synthesis inhibitors kanamycin and chloramphenicol . Simultaneous deletion of the genes for four cold shock proteins, cspA, cspB, cspE, and cspG, causes cold sensitivity and a filamentous phenotype. Both phenotypes are suppressed by overexpression of any one member of the CspA family of proteins (except CspD, which is lethal when overexpressed) . The cold sensitivity of this mutant strain can also be suppressed by the S1 domain of polynucleotide phosphorylase; this might be explained by structural similarities between the proteins . cspG is most highly expressed in mid-log phase and is induced upon cold shock in MOPS defined minimal medium . An in-silico comparative study of evolution, structure and function was carried out for the 9 CspA family of proteins in E. coli K-12. Despite high homology (>70% amino acid sequence similarity), it was determined that 4 paralogous pairs could be identified and served as the focus for the comparative analyses: CspA/CspB, CspC/CspE, CspG/CspI and CspF/CspH...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A978|protein.P0A978]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003346,ECOCYC:G6511,GeneID:945591`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1051461-1051673:+; feature_type=gene
