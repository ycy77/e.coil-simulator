---
entity_id: "gene.b3095"
entity_type: "gene"
name: "yqjA"
source_database: "NCBI RefSeq"
source_id: "gene-b3095"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3095"
  - "yqjA"
---

# yqjA

`gene.b3095`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3095`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yqjA (gene.b3095) is a gene entity. It encodes yqjA (protein.P0AA63). Encoded protein function: FUNCTION: May be a membrane transporter required for proton motive force (PMF)-dependent drug efflux. Required, with YghB, for the proper export of certain periplasmic amidases and, possibly, other Tat substrates. May play a role in determining membrane lipid composition. {ECO:0000269|PubMed:18456815, ECO:0000269|PubMed:19880597, ECO:0000269|PubMed:24277026}. EcoCyc product frame: G7609-MONOMER. EcoCyc synonyms: ecfL. Genomic coordinates: 3247773-3248435. EcoCyc protein note: A yghB yqjA double null strain has a synthetic growth defect at elevated temperatures, forms chains of cells at permissive temperatures, and can be complemented by yghB, yqjA, yohD, or yabI expressed from a plasmid . The double and single mutants displayed altered phospholipid compositions . An E. coli ΔyqjA ΔyghB strain is hypersensitive to a number of structurally diverse drugs and dyes including ethidium bromide, methyl viologen, acriflavine, nalidixic acid and β-lactam antibiotics. A wild-type response is restored by expression of yqjA from a plasmid . Mutation of the membrane embedded acidic amino acids E39 (glutamic acid) or D51 (aspartic acid) in plasmid-expressed YqjA compromises its ability to restore wild-type resistance...

## Biological Role

Activated by rpoD (protein.P00579), cpxR (protein.P0AE88), rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AA63|protein.P0AA63]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yqjA; function=+
- `activates` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `S` - regulator=CpxR; target=yqjA; function=+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=yqjA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010181,ECOCYC:G7609,GeneID:947643`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3247773-3248435:+; feature_type=gene
