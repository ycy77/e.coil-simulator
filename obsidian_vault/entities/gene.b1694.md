---
entity_id: "gene.b1694"
entity_type: "gene"
name: "ydiF"
source_database: "NCBI RefSeq"
source_id: "gene-b1694"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1694"
  - "ydiF"
---

# ydiF

`gene.b1694`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1694`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydiF (gene.b1694) is a gene entity. It encodes ydiF (protein.P37766). Encoded protein function: FUNCTION: CoA transferase having broad substrate specificity for short-chain acyl-CoA thioesters with the activity decreasing when the length of the carboxylic acid chain exceeds four carbons. May play a role in short-chain fatty acid metabolism in E.coli. {ECO:0000250|UniProtKB:Q8X5X6}. EcoCyc product frame: EG12432-MONOMER. Genomic coordinates: 1775587-1777182. EcoCyc protein note: Based on sequence similarity, particularly with conserved motifs EXGXXG and GXGGF, YdiF is predicted to be an acetate CoA-transferase . YdiF not only catalyzes the formation of acetyl-CoA from acetate, it also catalyzes the conversion of lactyl-CoA from L-lactate both in vitro with purified YdiF and in vivo when overexpressed from a plasmid; the lactyl-CoA product is then used by EG12270-MONOMER . The enzyme from E. coli O157:H7 has broad substrate specificity for short-chain acyl-CoA thioesters. Crystal structures of the enzyme from E. coli O157:H7 have been solved; the enzyme is a homotetramer in a dimer of dimers configuration . The protein sequence of the O157:H7 enzyme (Q8X5X6) is 99% identical to that of the K-12 enzyme.

## Enriched Pathways

- `eco00627` Aminobenzoate degradation (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37766|protein.P37766]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005656,ECOCYC:EG12432,GeneID:946211`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1775587-1777182:+; feature_type=gene
