---
entity_id: "gene.b2173"
entity_type: "gene"
name: "yeiR"
source_database: "NCBI RefSeq"
source_id: "gene-b2173"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2173"
  - "yeiR"
---

# yeiR

`gene.b2173`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2173`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yeiR (gene.b2173) is a gene entity. It encodes yeiR (protein.P33030). Encoded protein function: FUNCTION: Zinc chaperone that directly transfers zinc cofactor to target proteins, thereby activating them (By similarity). Zinc is transferred from the CXCC motif in the GTPase domain to the zinc binding site in target proteins in a process requiring GTP hydrolysis (By similarity). {ECO:0000250|UniProtKB:Q8VEH6}. EcoCyc product frame: EG12104-MONOMER. Genomic coordinates: 2267829-2268815. EcoCyc protein note: YeiR belongs to the G3E family of P-loop GTPases. The protein binds Zn2+ in vitro; metal binding leads to oligomerization and enhances its GTPase activity. A yeiR deletion mutant shows increased sensitivity to the metal chelator EDTA .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33030|protein.P33030]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007194,ECOCYC:EG12104,GeneID:946701`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2267829-2268815:+; feature_type=gene
