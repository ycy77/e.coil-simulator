---
entity_id: "gene.b4699"
entity_type: "gene"
name: "fnrS"
source_database: "NCBI RefSeq"
source_id: "gene-b4699"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4699"
  - "fnrS"
---

# fnrS

`gene.b4699`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4699`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fnrS (gene.b4699) is a gene entity. EcoCyc product frame: RNA0-349. EcoCyc synonyms: rydA. Genomic coordinates: 1409129-1409250.

## Biological Role

Activated by rpoD (protein.P00579), fnr (protein.P0A9E5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (5)

- `represses` --> [[gene.b0755|gene.b0755]] `RegulonDB` `S` - regulator=FnrS; target=gpmA; function=-
- `represses` --> [[gene.b1479|gene.b1479]] `RegulonDB` `S` - regulator=FnrS; target=maeA; function=-
- `represses` --> [[gene.b1656|gene.b1656]] `RegulonDB` `S` - regulator=FnrS; target=sodB; function=-
- `represses` --> [[gene.b2531|gene.b2531]] `RegulonDB` `S` - regulator=FnrS; target=iscR; function=-
- `represses` --> [[gene.b3755|gene.b3755]] `RegulonDB` `S` - regulator=FnrS; target=yieP; function=-

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=fnrS; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=fnrS; function=+

## External IDs

- `Dbxref:ECOCYC:G0-10677,GeneID:8764968`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:1409129-1409250:+; feature_type=gene
