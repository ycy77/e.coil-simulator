---
entity_id: "gene.b2492"
entity_type: "gene"
name: "focB"
source_database: "NCBI RefSeq"
source_id: "gene-b2492"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2492"
  - "focB"
---

# focB

`gene.b2492`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2492`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

focB (gene.b2492) is a gene entity. It encodes focB (protein.P77733). Encoded protein function: FUNCTION: Involved in the bidirectional transport of formate during mixed-acid fermentation. {ECO:0000269|PubMed:30247527}. EcoCyc product frame: FOCB-MONOMER. Genomic coordinates: 2613934-2614782. EcoCyc protein note: focB is located in an operon (hyfABCDEFGHIR-focB) with genes encoding a putative hydrogenase complex; the FocB protein contains 6 predicted membrane helices and has 50% sequence identity with the formate channel CPLX0-7843 "FocA"; FocB is predicted to import formate for use in a formate hydrogenlyase pathway involving the hyf encoded hydrogenase . FocB activity and the direction of formate translocation is affected by electron donor identity and external pH; in the absence of CPLX0-7843 "FocA" and FocB an unidentifed system serves to transport formate . FocB and FocA are implicated in the maintenance of ion gradients during fermentation . FocB is a member of the FNT family of formate and nitrite transporters .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77733|protein.P77733]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008206,ECOCYC:G7309,GeneID:949032`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2613934-2614782:+; feature_type=gene
