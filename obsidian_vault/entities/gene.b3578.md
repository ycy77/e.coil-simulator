---
entity_id: "gene.b3578"
entity_type: "gene"
name: "yiaN"
source_database: "NCBI RefSeq"
source_id: "gene-b3578"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3578"
  - "yiaN"
---

# yiaN

`gene.b3578`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3578`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yiaN (gene.b3578) is a gene entity. It encodes yiaN (protein.P37675). Encoded protein function: FUNCTION: Part of the tripartite ATP-independent periplasmic (TRAP) transport system YiaMNO involved in the uptake of 2,3-diketo-L-gulonate. {ECO:0000269|PubMed:16385129}. EcoCyc product frame: EG12282-MONOMER. Genomic coordinates: 3744804-3746081. EcoCyc protein note: Based on sequence similarity, YiaN is a membrane-spanning component of the YiaMNO Binding protein-dependent Secondary (TRAP) Transporter .

## Biological Role

Repressed by plaR (protein.P37671). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), rpoE (protein.P0AGB6).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37675|protein.P37675]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yiaN; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=yiaN; function=+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=yiaN; function=+
- `represses` <-- [[protein.P37671|protein.P37671]] `RegulonDB` `C` - regulator=PlaR; target=yiaN; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011692,ECOCYC:EG12282,GeneID:948092`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3744804-3746081:+; feature_type=gene
