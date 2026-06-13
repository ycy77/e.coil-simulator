---
entity_id: "gene.b1035"
entity_type: "gene"
name: "ycdY"
source_database: "NCBI RefSeq"
source_id: "gene-b1035"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1035"
  - "ycdY"
---

# ycdY

`gene.b1035`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1035`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ycdY (gene.b1035) is a gene entity. It encodes ycdY (protein.P75915). Encoded protein function: FUNCTION: Acts as a chaperone that increases YcdX activity, maybe by facilitating the correct insertion of the zinc ions into the catalytic site of YcdX. Involved in the swarming motility process. {ECO:0000269|PubMed:21965574}. EcoCyc product frame: G6541-MONOMER. Genomic coordinates: 1099640-1100194. EcoCyc protein note: YcdY is a member of an atypical subfamily of TorD chaperones . YcdY appears to enable maturation of YcdX, potentially by facilitating insertion of Zn2+ into the catalytic site of YcdX . Phylogenetic analysis of the NarJ subfamily of proteins suggests that YcdY has only recently evolved from DmsD . A ycdY mutant has a swarming defect . Review:

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75915|protein.P75915]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003511,ECOCYC:G6541,GeneID:945609`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1099640-1100194:+; feature_type=gene
