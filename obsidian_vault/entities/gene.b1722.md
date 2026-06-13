---
entity_id: "gene.b1722"
entity_type: "gene"
name: "ydiY"
source_database: "NCBI RefSeq"
source_id: "gene-b1722"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1722"
  - "ydiY"
---

# ydiY

`gene.b1722`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1722`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydiY (gene.b1722) is a gene entity. It encodes ydiY (protein.P76206). Encoded protein function: Uncharacterized protein YdiY EcoCyc product frame: G6928-MONOMER. Genomic coordinates: 1805325-1806083. EcoCyc protein note: Sequence similarity suggests that YdiY is a member of the Outer Membrane Receptor (OMR) family . Expression of YdiY is induced by acid .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76206|protein.P76206]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=ydiY; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005744,ECOCYC:G6928,GeneID:946218`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1805325-1806083:-; feature_type=gene
