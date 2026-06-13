---
entity_id: "gene.b4698"
entity_type: "gene"
name: "mgrR"
source_database: "NCBI RefSeq"
source_id: "gene-b4698"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4698"
  - "mgrR"
---

# mgrR

`gene.b4698`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4698`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mgrR (gene.b4698) is a gene entity. EcoCyc product frame: RNA0-348. Genomic coordinates: 1622817-1622914.

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Annotation

NCBI RefSeq gene feature

## Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Outgoing Edges (1)

- `represses` --> [[gene.b4062|gene.b4062]] `RegulonDB` `S` - regulator=MgrR; target=soxS; function=-

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=mgrR; function=+

## External IDs

- `Dbxref:ASAP:ABE-0285266,ECOCYC:G0-10671,GeneID:8764967`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:1622817-1622914:-; feature_type=gene
