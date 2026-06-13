---
entity_id: "gene.b2162"
entity_type: "gene"
name: "rihB"
source_database: "NCBI RefSeq"
source_id: "gene-b2162"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2162"
  - "rihB"
---

# rihB

`gene.b2162`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2162`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rihB (gene.b2162) is a gene entity. It encodes rihB (protein.P33022). Encoded protein function: FUNCTION: Hydrolyzes cytidine or uridine to ribose and cytosine or uracil, respectively. Has a clear preference for cytidine over uridine. Strictly specific for ribonucleosides. Has a low but significant activity for the purine nucleoside xanthosine. EcoCyc product frame: EG12030-MONOMER. EcoCyc synonyms: yeiK. Genomic coordinates: 2254245-2255186.

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33022|protein.P33022]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rihB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007156,ECOCYC:EG12030,GeneID:946646`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2254245-2255186:-; feature_type=gene
