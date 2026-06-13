---
entity_id: "gene.b2012"
entity_type: "gene"
name: "tsuB"
source_database: "NCBI RefSeq"
source_id: "gene-b2012"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2012"
  - "tsuB"
---

# tsuB

`gene.b2012`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2012`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tsuB (gene.b2012) is a gene entity. It encodes tsuB (protein.P33014). Encoded protein function: FUNCTION: Involved in thiosulfate metabolism. {ECO:0000269|PubMed:32779574}. EcoCyc product frame: EG11894-MONOMER. EcoCyc synonyms: yeeD. Genomic coordinates: 2084226-2084453. EcoCyc protein note: TsuB shows sequence similarity to the sulfur transfer protein EG12216-MONOMER TusA; however, unlike TusA, TsuB does not appear to function in molybdenum cofactor assembly . TsuB is implicated in S2O3 metabolism; deletion of tsuB inhibits the ability of a ΔEG10183 cysA mutant to grow with thiosulfate as sole sulfur source . tsuB is a member of the PC00040 CysB regulon; TsuB is subject to post-transcriptional control by G7459-MONOMER RppH-dependent mRNA degradation; TsuB supports the preferential use of thiosulfate as a sulfur source in ΔrppH cells . TsuB is required for TsuA-mediated thiosulfate uptake in vivo and the two proteins may physically interact . Several genes described to be responsive to sulfur availability, including tsuB , were among the most strongly upregulated genes in two MG1655 lysogens carrying closely related Stx2a phages O104 and PA8 . This protein in E...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33014|protein.P33014]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006688,ECOCYC:EG11894,GeneID:946539`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2084226-2084453:-; feature_type=gene
