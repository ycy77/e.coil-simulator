---
entity_id: "gene.b2265"
entity_type: "gene"
name: "menF"
source_database: "NCBI RefSeq"
source_id: "gene-b2265"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2265"
  - "menF"
---

# menF

`gene.b2265`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2265`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

menF (gene.b2265) is a gene entity. It encodes menF (protein.P38051). Encoded protein function: FUNCTION: Catalyzes the conversion of chorismate to isochorismate. Can also catalyze the reverse reaction, but with a lower efficiency. {ECO:0000269|PubMed:17240978, ECO:0000269|PubMed:8764478, ECO:0000269|PubMed:9150206, ECO:0000269|PubMed:9795253}. EcoCyc product frame: MENF-MONOMER. EcoCyc synonyms: yfbA. Genomic coordinates: 2379348-2380643.

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01053` Biosynthesis of siderophore group nonribosomal peptides (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P38051|protein.P38051]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007485,ECOCYC:EG12362,GeneID:946712`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2379348-2380643:-; feature_type=gene
