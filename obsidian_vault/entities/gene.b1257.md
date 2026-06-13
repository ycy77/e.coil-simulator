---
entity_id: "gene.b1257"
entity_type: "gene"
name: "yciE"
source_database: "NCBI RefSeq"
source_id: "gene-b1257"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1257"
  - "yciE"
---

# yciE

`gene.b1257`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1257`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yciE (gene.b1257) is a gene entity. It encodes yciE (protein.P21363). Encoded protein function: Protein YciE EcoCyc product frame: EG11125-MONOMER. Genomic coordinates: 1314718-1315224. EcoCyc protein note: Expression of YciE is induced under osmotic stress imposed by NaCl in both aerobic and anaerobic conditions and repressed by H-NS . The yciGFE locus is expressed poorly . A preliminary X-ray crystallographic analysis of YciE has been performed .

## Biological Role

Repressed by hns (protein.P0ACF8). Activated by mcbR (protein.P76114).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P21363|protein.P21363]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P76114|protein.P76114]] `RegulonDB` `S` - regulator=McbR; target=yciE; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `C` - regulator=H-NS; target=yciE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004212,ECOCYC:EG11125,GeneID:946871`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1314718-1315224:-; feature_type=gene
