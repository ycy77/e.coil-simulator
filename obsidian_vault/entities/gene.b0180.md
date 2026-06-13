---
entity_id: "gene.b0180"
entity_type: "gene"
name: "fabZ"
source_database: "NCBI RefSeq"
source_id: "gene-b0180"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0180"
  - "fabZ"
---

# fabZ

`gene.b0180`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0180`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fabZ (gene.b0180) is a gene entity. It encodes fabZ (protein.P0A6Q6). Encoded protein function: FUNCTION: Involved in unsaturated fatty acids biosynthesis. Catalyzes the dehydration of short chain beta-hydroxyacyl-ACPs and long chain saturated and unsaturated beta-hydroxyacyl-ACPs. {ECO:0000269|PubMed:10629181, ECO:0000269|PubMed:7806516, ECO:0000269|PubMed:8910376}. EcoCyc product frame: FABZ-MONOMER. EcoCyc synonyms: sfhC21, sabA1, sefA, yaeA. Genomic coordinates: 202101-202556.

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Enriched Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00780` Biotin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6Q6|protein.P0A6Q6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=fabZ; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000613,ECOCYC:EG11284,GeneID:944888`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:202101-202556:+; feature_type=gene
