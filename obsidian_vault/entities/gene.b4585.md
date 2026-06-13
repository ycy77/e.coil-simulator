---
entity_id: "gene.b4585"
entity_type: "gene"
name: "chiX"
source_database: "NCBI RefSeq"
source_id: "gene-b4585"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4585"
  - "chiX"
---

# chiX

`gene.b4585`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4585`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

chiX (gene.b4585) is a gene entity. EcoCyc product frame: RNA0-123. EcoCyc synonyms: sroB, rybC, micM. Genomic coordinates: 507204-507287.

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (5)

- `represses` --> [[gene.b0619|gene.b0619]] `RegulonDB` `S` - regulator=ChiX; target=dpiB; function=-
- `represses` --> [[gene.b0620|gene.b0620]] `RegulonDB` `S` - regulator=ChiX; target=dpiA; function=-
- `represses` --> [[gene.b0681|gene.b0681]] `RegulonDB` `S` - regulator=ChiX; target=chiP; function=-
- `represses` --> [[gene.b0682|gene.b0682]] `RegulonDB` `S` - regulator=ChiX; target=chiQ; function=-
- `represses` --> [[gene.b4808|gene.b4808]] `RegulonDB` `S` - regulator=ChiX; target=chiZ; function=-

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=chiX; function=+

## External IDs

- `Dbxref:ASAP:ABE-0285117,ECOCYC:G0-9382,GeneID:5061500`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:507204-507287:+; feature_type=gene
