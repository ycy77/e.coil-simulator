---
entity_id: "gene.b1379"
entity_type: "gene"
name: "hslJ"
source_database: "NCBI RefSeq"
source_id: "gene-b1379"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1379"
  - "hslJ"
---

# hslJ

`gene.b1379`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1379`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hslJ (gene.b1379) is a gene entity. It encodes hslJ (protein.P52644). Encoded protein function: Heat shock protein HslJ EcoCyc product frame: G6702-MONOMER. EcoCyc synonyms: ydbI. Genomic coordinates: 1441321-1441743. EcoCyc protein note: hslJ is a member of the CysB regulon; CysB is a direct repressor of hslJ transcription; hslJ is also subject to (possibly indirect) autogenous negative repression . hslJ is implicated in the increased resistance to Novobiocin that occurs in cysB- mutants. Inactivation of hslJ (hslJ::lacZ or hslJ::ΩKan) in a cysB- background results in decreased resistance to the antibiotic Novobiocin (compared to the cysB- parent strain); overexpression of hslJ from a low copy number plasmid increases Novobiocin resistance in both a cysB- and cysB+ background . HslJ is a lipoprotein ; HslJ is predicted to be a membrane protein hslJ expression is induced by heat shock (7 mins at 50 °C) . Expression of a hslJ::lacZ gene fusion (in a cysB- strain) is not induced by heat shock - maximal expression occurs at 37 °C; no heat shock promoters are identified in the upstream region of hslJ

## Biological Role

Repressed by cysB (protein.P0A9F3). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P52644|protein.P52644]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=hslJ; function=+
- `represses` <-- [[protein.P0A9F3|protein.P0A9F3]] `RegulonDB` `S` - regulator=CysB; target=hslJ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004616,ECOCYC:G6702,GeneID:946525`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1441321-1441743:-; feature_type=gene
