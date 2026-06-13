---
entity_id: "gene.b0266"
entity_type: "gene"
name: "yagB"
source_database: "NCBI RefSeq"
source_id: "gene-b0266"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0266"
  - "yagB"
---

# yagB

`gene.b0266`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0266`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yagB (gene.b0266) is a gene entity. It encodes yagB (protein.P37008). Encoded protein function: FUNCTION: Putative antitoxin component of a type IV toxin-antitoxin (TA) system; its cognate toxin is unknown. {ECO:0000305}. EcoCyc product frame: EG12339-MONOMER. Genomic coordinates: 280385-280735. EcoCyc protein note: YagB belongs to the CbeA/YafW/YfjZ family of antitoxins that enhance the bundling of cytoskeleton proteins. No cognate toxin protein is encoded in the vicinity of yagB .

## Biological Role

Repressed by xynR (protein.P77300).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37008|protein.P37008]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P77300|protein.P77300]] `RegulonDB` `C` - regulator=XynR; target=yagB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0000912,ECOCYC:EG12339,GeneID:944944`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:280385-280735:-; feature_type=gene
