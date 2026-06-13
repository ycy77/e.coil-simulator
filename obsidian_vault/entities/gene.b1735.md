---
entity_id: "gene.b1735"
entity_type: "gene"
name: "chbR"
source_database: "NCBI RefSeq"
source_id: "gene-b1735"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1735"
  - "chbR"
---

# chbR

`gene.b1735`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1735`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

chbR (gene.b1735) is a gene entity. It encodes chbR (protein.P17410). Encoded protein function: FUNCTION: Dual-function repressor/activator of the chbBCARFG operon. In the absence of the inducing sugar chitobiose, together with NagC, represses the chbBCARFG operon for the uptake and metabolism of chitobiose. In association with Crp, and probably in the presence of chitobiose 6-phosphate, induces the transcription of the chbBCARFG operon. {ECO:0000269|PubMed:18028317}. EcoCyc product frame: EG10143-MONOMER. EcoCyc synonyms: celD. Genomic coordinates: 1818605-1819447.

## Biological Role

Repressed by nagC (protein.P0AF20), chbR (protein.P17410). Activated by crp (protein.P0ACJ8), chbR (protein.P17410).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P17410|protein.P17410]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=chbR; function=+
- `activates` <-- [[protein.P17410|protein.P17410]] `RegulonDB` `S` - regulator=ChbR; target=chbR; function=-+
- `represses` <-- [[protein.P0AF20|protein.P0AF20]] `RegulonDB` `S` - regulator=NagC; target=chbR; function=-
- `represses` <-- [[protein.P17410|protein.P17410]] `RegulonDB` `S` - regulator=ChbR; target=chbR; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0005790,ECOCYC:EG10143,GeneID:946247`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1818605-1819447:-; feature_type=gene
