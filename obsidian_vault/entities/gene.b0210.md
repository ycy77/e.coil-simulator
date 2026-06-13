---
entity_id: "gene.b0210"
entity_type: "gene"
name: "yafE"
source_database: "NCBI RefSeq"
source_id: "gene-b0210"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0210"
  - "yafE"
---

# yafE

`gene.b0210`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0210`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yafE (gene.b0210) is a gene entity. It encodes yafE (protein.P30866). Encoded protein function: Uncharacterized protein YafE EcoCyc product frame: EG11651-MONOMER. Genomic coordinates: 231926-232549. EcoCyc protein note: No information about this protein was found by a literature search conducted on August 1, 2014.

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoH (protein.P0AGB3), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P30866|protein.P30866]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=yafE; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yafE; function=-+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yafE; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0000702,ECOCYC:EG11651,GeneID:946197`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:231926-232549:+; feature_type=gene
