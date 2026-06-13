---
entity_id: "gene.b3579"
entity_type: "gene"
name: "yiaO"
source_database: "NCBI RefSeq"
source_id: "gene-b3579"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3579"
  - "yiaO"
---

# yiaO

`gene.b3579`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3579`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yiaO (gene.b3579) is a gene entity. It encodes yiaO (protein.P37676). Encoded protein function: FUNCTION: Part of the tripartite ATP-independent periplasmic (TRAP) transport system YiaMNO involved in the uptake of 2,3-diketo-L-gulonate. This protein specifically binds 2,3-diketo-L-gulonate. Is not able to bind either L-ascorbate or dehydroascorbate. {ECO:0000269|PubMed:16385129}. EcoCyc product frame: EG12283-MONOMER. Genomic coordinates: 3746094-3747080. EcoCyc protein note: Based on sequence similarity, YiaO is the periplasmic solute-binding component of the YiaMNO Binding Protein-dependent Secondary (TRAP) transporter

## Biological Role

Repressed by plaR (protein.P37671). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), rpoE (protein.P0AGB6).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37676|protein.P37676]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yiaO; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=yiaO; function=+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=yiaO; function=+
- `represses` <-- [[protein.P37671|protein.P37671]] `RegulonDB` `C` - regulator=PlaR; target=yiaO; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011694,ECOCYC:EG12283,GeneID:948091`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3746094-3747080:+; feature_type=gene
