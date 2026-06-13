---
entity_id: "gene.b2034"
entity_type: "gene"
name: "wbbI"
source_database: "NCBI RefSeq"
source_id: "gene-b2034"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2034"
  - "wbbI"
---

# wbbI

`gene.b2034`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2034`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

wbbI (gene.b2034) is a gene entity. It encodes wbbI (protein.P37749). Encoded protein function: FUNCTION: Involved in the transfer of galactofuranose (Galf) onto an alpha-D-gluco-configured acceptor substrate to form a beta-1,6-linkage. It uses n-octyl alpha-D-glucopyranoside as an acceptor substrate for the addition of galactofuranose from the donor substrate UDP-galactofuranose. It is not able to use beta-D-glucopyranoside isomers. {ECO:0000269|PubMed:17047874}. EcoCyc product frame: EG11983-MONOMER. EcoCyc synonyms: yefG. Genomic coordinates: 2105065-2106057. EcoCyc protein note: WbbI is a β-1,6-galactofuranosyltransferase that uses UDP-galactofuranose as the donor and has a modest preference for pyranoside acceptor substrates of the α-D-gluco configuration . When the rfb-50 mutation, an IS5 insertion in the gene encoding rhamnosyl transferase, wbbL, is complemented with a wild type wbbL gene, E. coli K-12 produces the O16 variant of O antigen, with a β-D-galactofuranosyl moiety in the repeating unit . For information on bacterial polysaccharide gene nomenclature see .

## Enriched Pathways

- `eco00542` O-Antigen repeat unit biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37749|protein.P37749]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006751,ECOCYC:EG11983,GeneID:947041`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2105065-2106057:-; feature_type=gene
