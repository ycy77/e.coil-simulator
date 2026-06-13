---
entity_id: "gene.b0889"
entity_type: "gene"
name: "lrp"
source_database: "NCBI RefSeq"
source_id: "gene-b0889"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0889"
  - "lrp"
---

# lrp

`gene.b0889`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0889`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lrp (gene.b0889) is a gene entity. It encodes lrp (protein.P0ACJ0). Encoded protein function: FUNCTION: Mediates a global response to leucine. Exogenous leucine affects the expression of a number of different operons; lrp mediates this effect for at least some of these operons. For example it is regulator of the branched-chain amino acid transport genes. EcoCyc product frame: PD00353. EcoCyc synonyms: rblA, oppI, mbf, lstR, alsB, ihb, livR, lrs. Genomic coordinates: 932595-933089. EcoCyc protein note: Lrp, "Leucine-responsive regulatory protein," is a dual transcriptional regulator for at least 10% of the genes in Escherichia coli . These genes are involved in amino acid biosynthesis and catabolism, nutrient transport, pili synthesis, and other cellular functions, including 1-carbon metabolism . In addition, Lrp affects nearly three-fourths of the genes induced upon entry into stationary phase . Lrp might also play a topological role in dynamic DNA packaging . Using a machine learning framework that integrates and analyzes data from 10 different sources, it was determined that Lrp is involved in antibiotic resistance in E. coli, and this was confirmed in Salmonella enterica . Lrp can act as a repressor or activator for its target genes...

## Biological Role

Repressed by ArgR-L-arginine DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-228), dsrA (gene.b1954), micF (gene.b4439), gcvB (gene.b4443), argR (protein.P0A6D0), hns (protein.P0ACF8), lrp (protein.P0ACJ0), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACJ0|protein.P0ACJ0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (8)

- `represses` <-- [[complex.ecocyc.CPLX0-228|complex.ecocyc.CPLX0-228]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[gene.b1954|gene.b1954]] `RegulonDB` `S` - regulator=DsrA; target=lrp; function=-
- `represses` <-- [[gene.b4439|gene.b4439]] `RegulonDB` `S` - regulator=MicF; target=lrp; function=-
- `represses` <-- [[gene.b4443|gene.b4443]] `RegulonDB` `S` - regulator=GcvB; target=lrp; function=-
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `S` - regulator=ArgR; target=lrp; function=-
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=lrp; function=-
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `S` - regulator=Lrp; target=lrp; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=lrp; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003023,ECOCYC:EG10547,GeneID:949051`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:932595-933089:+; feature_type=gene
