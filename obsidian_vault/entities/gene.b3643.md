---
entity_id: "gene.b3643"
entity_type: "gene"
name: "rph"
source_database: "NCBI RefSeq"
source_id: "gene-b3643"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3643"
  - "rph"
---

# rph

`gene.b3643`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3643`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rph (gene.b3643) is a gene entity. It encodes rph (protein.P0CG19). Encoded protein function: FUNCTION: This an expressed but non-active exoribonuclease allele (PubMed:8501045). The catalytically inactive protein translated in strain K12 MG1655 inhibits the 5'-processing of primary pre-tRNAs with short (<5 nucleotide) leaders in a dominant-negative effect when RNA pyrophosphohydrolase (rppH) is also inactive; perhaps inactive Rph inhibits interaction with RNase P which is exacerbated when RppH cannot cleave the triphosphate of the primary transcript (PubMed:28808133). {ECO:0000269|PubMed:28808133, ECO:0000269|PubMed:8501045}. EcoCyc product frame: EG10863-MONOMER. Genomic coordinates: 3815863-3816549. EcoCyc protein note: In the E. coli K-12 strains MG1655 (represented in EcoCyc) and W3110, the rph gene contains a frameshift mutation (rph-1) resulting in a shortened open reading frame. As characterized in strain W3110, Rph is truncated at the C-terminus and lacks the weak poly(A) phosphorylase activity associated with RNase PH. The strains also show a pyrimidine starvation phenotype due to a PyrE deficiency that results from the polar effect of the rph frameshift mutation on the downstream pyrE gene ( and discussed in ). In the absence of the G7459-MONOMER RppH, the rph-1-encoded truncated RNase PH inhibits CPLX0-1382-mediated maturation of certain pre-tRNAs...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R07285|reaction.R07285]] `KEGG` `database` - via EC:2.7.7.56
- `encodes` --> [[protein.P0CG19|protein.P0CG19]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011909,ECOCYC:EG10863,GeneID:948156`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3815863-3816549:-; feature_type=gene
