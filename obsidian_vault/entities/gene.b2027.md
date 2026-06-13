---
entity_id: "gene.b2027"
entity_type: "gene"
name: "wzzB"
source_database: "NCBI RefSeq"
source_id: "gene-b2027"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2027"
  - "wzzB"
---

# wzzB

`gene.b2027`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2027`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

wzzB (gene.b2027) is a gene entity. It encodes wzzB (protein.P76372). Encoded protein function: FUNCTION: Confers a modal distribution of chain length on the O-antigen component of lipopolysaccharide (LPS). Gives rise to a reduced number of short chain molecules and increases in numbers of longer molecules. EcoCyc product frame: G7090-MONOMER. EcoCyc synonyms: wzz, rol, cld. Genomic coordinates: 2097321-2098301. EcoCyc protein note: wzzB encodes the O-antigen co-polymerase (also called the O-antigen chain length regulator) of a Wzx/Wzy-dependent pathway of O-antigen synthesis; Wzz family proteins are required to regulate the length distribution of lipid-linked polysaccharides during polymerization at the periplasmic face of the inner membrane (see ). WzzB is a group 1a polysaccharide co-polymerase (PCP1a); E. coli K-12 also contains a group 1b PCP - EG11295-MONOMER WzzE - which regulates the length of enterobacterial common antigen (see ). E. coli K-12 is phenotypically rough and does not express O-antigen due to mutations in the rfb region; an engineered strain of E. coli K-12 with all rfb genes intact synthesizes CPD0-2249 O16 antigen . Early studies identified wzz genes (formerly rol for "regulator of O length" or cld for "chain length determinant") in O-antigen producing E. coli strains...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76372|protein.P76372]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006731,ECOCYC:G7090,GeneID:946553`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2097321-2098301:-; feature_type=gene
