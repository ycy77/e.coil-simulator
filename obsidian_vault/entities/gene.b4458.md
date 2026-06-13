---
entity_id: "gene.b4458"
entity_type: "gene"
name: "oxyS"
source_database: "NCBI RefSeq"
source_id: "gene-b4458"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4458"
  - "oxyS"
---

# oxyS

`gene.b4458`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4458`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

oxyS (gene.b4458) is a gene entity. EcoCyc product frame: OXYS-RNA. Genomic coordinates: 4158278-4158394.

## Biological Role

Activated by oxyR (protein.P0ACQ4).

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (7)

- `activates` --> [[gene.b2528|gene.b2528]] `RegulonDB` `S` - regulator=OxyS; target=iscA; function=+
- `activates` --> [[gene.b2529|gene.b2529]] `RegulonDB` `S` - regulator=OxyS; target=iscU; function=+
- `activates` --> [[gene.b2530|gene.b2530]] `RegulonDB` `S` - regulator=OxyS; target=iscS; function=+
- `activates` --> [[gene.b2531|gene.b2531]] `RegulonDB` `S` - regulator=OxyS; target=iscR; function=+
- `represses` --> [[gene.b1891|gene.b1891]] `RegulonDB` `S` - regulator=OxyS; target=flhC; function=-
- `represses` --> [[gene.b1892|gene.b1892]] `RegulonDB` `S` - regulator=OxyS; target=flhD; function=-
- `represses` --> [[gene.b2175|gene.b2175]] `RegulonDB` `S` - regulator=OxyS; target=mepS; function=-

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACQ4|protein.P0ACQ4]] `RegulonDB` `S` - regulator=OxyR; target=oxyS; function=+

## External IDs

- `Dbxref:ASAP:ABE-0047276,ECOCYC:EG31116,GeneID:2847701`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:4158278-4158394:-; feature_type=gene
