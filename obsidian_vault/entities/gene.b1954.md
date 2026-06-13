---
entity_id: "gene.b1954"
entity_type: "gene"
name: "dsrA"
source_database: "NCBI RefSeq"
source_id: "gene-b1954"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1954"
  - "dsrA"
---

# dsrA

`gene.b1954`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1954`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dsrA (gene.b1954) is a gene entity. EcoCyc product frame: DSRA-RNA. Genomic coordinates: 2025223-2025313.

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (9)

- `represses` --> [[gene.b0889|gene.b0889]] `RegulonDB` `S` - regulator=DsrA; target=lrp; function=-
- `represses` --> [[gene.b1237|gene.b1237]] `RegulonDB` `S` - regulator=DsrA; target=hns; function=-
- `represses` --> [[gene.b3748|gene.b3748]] `RegulonDB` `S` - regulator=DsrA; target=rbsD; function=-
- `represses` --> [[gene.b3749|gene.b3749]] `RegulonDB` `S` - regulator=DsrA; target=rbsA; function=-
- `represses` --> [[gene.b3750|gene.b3750]] `RegulonDB` `S` - regulator=DsrA; target=rbsC; function=-
- `represses` --> [[gene.b3751|gene.b3751]] `RegulonDB` `S` - regulator=DsrA; target=rbsB; function=-
- `represses` --> [[gene.b3752|gene.b3752]] `RegulonDB` `S` - regulator=DsrA; target=rbsK; function=-
- `represses` --> [[gene.b3753|gene.b3753]] `RegulonDB` `S` - regulator=DsrA; target=rbsR; function=-
- `represses` --> [[gene.b4804|gene.b4804]] `RegulonDB` `S` - regulator=DsrA; target=rbsZ; function=-

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=dsrA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006490,ECOCYC:G7047,GeneID:946470`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:2025223-2025313:-; feature_type=gene
