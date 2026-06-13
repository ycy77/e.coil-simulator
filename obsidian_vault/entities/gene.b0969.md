---
entity_id: "gene.b0969"
entity_type: "gene"
name: "tusE"
source_database: "NCBI RefSeq"
source_id: "gene-b0969"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0969"
  - "tusE"
---

# tusE

`gene.b0969`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0969`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tusE (gene.b0969) is a gene entity. It encodes tusE (protein.P0AB18). Encoded protein function: FUNCTION: Part of a sulfur-relay system required for 2-thiolation of 5-methylaminomethyl-2-thiouridine (mnm(5)s(2)U) at tRNA wobble positions. Could accept sulfur from TusD. {ECO:0000269|PubMed:16387657}. EcoCyc product frame: EG12876-MONOMER. EcoCyc synonyms: yccK. Genomic coordinates: 1030339-1030668. EcoCyc protein note: TusE functions as a sulfur mediator during synthesis of 2-thiouridine of the modified wobble base mnm5s2U in tRNA. TusE directly interacts with both the TusBCD complex and the MnmA-tRNA complex, but not with tRNA itself . TusE accepts the sulfur from the CPLX-3942 and transfers it to Cys199 of MnmA . 2-thiouridine formation in vitro is greatly enhanced in the presence of TusE. TusE is labeled by 35S sulfur during 2-thiouridine formation in vitro . A tusE deletion mutant lacks mnm5s2U, accumulates mnm5U and has a growth defect. The cysteine residue C108 is required for sulfur transfer . TusE: "tRNA 2-thiouridine synthesizing protein"

## Enriched Pathways

- `eco04122` Sulfur relay system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AB18|protein.P0AB18]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003278,ECOCYC:EG12876,GeneID:945023`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1030339-1030668:-; feature_type=gene
