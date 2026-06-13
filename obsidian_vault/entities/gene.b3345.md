---
entity_id: "gene.b3345"
entity_type: "gene"
name: "tusD"
source_database: "NCBI RefSeq"
source_id: "gene-b3345"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3345"
  - "tusD"
---

# tusD

`gene.b3345`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3345`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tusD (gene.b3345) is a gene entity. It encodes tusD (protein.P45532). Encoded protein function: FUNCTION: Part of a sulfur-relay system required for 2-thiolation of 5-methylaminomethyl-2-thiouridine (mnm(5)s(2)U) at tRNA wobble positions. Accepts sulfur from TusA and transfers it in turn to TusE. {ECO:0000269|PubMed:16387657}. EcoCyc product frame: G7714-MONOMER. EcoCyc synonyms: yheN. Genomic coordinates: 3475332-3475718. EcoCyc protein note: TusD is labeled by 35S sulfur during 2-thiouridine formation in vitro. The cysteine residue C78 appears to be responsible for accepting the activated sulfur . A tusD deletion mutant lacks the 2-thio modification of mnm5s2U in tRNA and has a severe growth defect . TusD: "tRNA 2-thiouridine synthesizing protein"

## Enriched Pathways

- `eco04122` Sulfur relay system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45532|protein.P45532]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010933,ECOCYC:G7714,GeneID:947852`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3475332-3475718:-; feature_type=gene
