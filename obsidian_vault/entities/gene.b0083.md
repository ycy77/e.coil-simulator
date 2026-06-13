---
entity_id: "gene.b0083"
entity_type: "gene"
name: "ftsL"
source_database: "NCBI RefSeq"
source_id: "gene-b0083"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0083"
  - "ftsL"
---

# ftsL

`gene.b0083`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0083`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ftsL (gene.b0083) is a gene entity. It encodes ftsL (protein.P0AEN4). Encoded protein function: FUNCTION: Essential cell division protein. May link together the upstream cell division proteins, which are predominantly cytoplasmic, with the downstream cell division proteins, which are predominantly periplasmic. Can also mediate Zn(2+)-sensitivity probably by increasing the permeability of the inner membrane. {ECO:0000255|HAMAP-Rule:MF_00910, ECO:0000269|PubMed:10613870, ECO:0000269|PubMed:19233928, ECO:0000269|PubMed:21708137}. EcoCyc product frame: EG11086-MONOMER. EcoCyc synonyms: mraR, yabD. Genomic coordinates: 91032-91397. EcoCyc protein note: FtsL is an essential cell division protein that is present in very small amounts of approximately 25 molecules per cell . Localization of FtsL to the septal ring is dependent on FtsZ, FtsA, ZipA, FtsK and FtsQ, but not FtsI . Conversely, FtsL is required for localization of FtsI to the Z ring . Although the hierarchy of dependency in the assembly of cell division proteins is largely linear, results have shown that assembly of the cell division machinery is complex . FtsL is an integral membrane protein with a small N-terminal cytoplasmic domain and a large periplasmic domain...

## Biological Role

Repressed by pdhR (protein.P0ACL9), mraZ (protein.P22186).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEN4|protein.P0AEN4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0ACL9|protein.P0ACL9]] `RegulonDB` `S` - regulator=PdhR; target=ftsL; function=-
- `represses` <-- [[protein.P22186|protein.P22186]] `RegulonDB` `C` - regulator=MraZ; target=ftsL; function=-

## External IDs

- `Dbxref:ASAP:ABE-0000306,ECOCYC:EG11086,GeneID:944803`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:91032-91397:+; feature_type=gene
