---
entity_id: "gene.b1784"
entity_type: "gene"
name: "yeaH"
source_database: "NCBI RefSeq"
source_id: "gene-b1784"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1784"
  - "yeaH"
---

# yeaH

`gene.b1784`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1784`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yeaH (gene.b1784) is a gene entity. It encodes yeaH (protein.P76235). Encoded protein function: FUNCTION: May play a role in the adaptation to sustained nitrogen starvation. {ECO:0000269|PubMed:26621053}. EcoCyc product frame: G6970-MONOMER. Genomic coordinates: 1868955-1870238. EcoCyc protein note: YeaH plays a role in the adaptation to sustained nitrogen starvation . The CPLX0-1461-dependent RYEB-RNA was found to downregulate the translation of G6969-MONOMER and YeaH under long term (24 hrs) N-starved conditions. Recovery from N-starvation has a shorter lag time in ΔyeaG, ΔyeaH and ΔyeaGΔyeaH mutants, whereas a longer lag time was observed in ΔsdsR mutants; thus, SdsR translational downregulation of YeaG and YeaH allows for optimal recovery from N-starvation .

## Biological Role

Repressed by sdsR (gene.b4433).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76235|protein.P76235]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[gene.b4433|gene.b4433]] `RegulonDB` `S` - regulator=SdsR; target=yeaH; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005938,ECOCYC:G6970,GeneID:946296`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1868955-1870238:+; feature_type=gene
