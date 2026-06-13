---
entity_id: "gene.b1232"
entity_type: "gene"
name: "purU"
source_database: "NCBI RefSeq"
source_id: "gene-b1232"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1232"
  - "purU"
---

# purU

`gene.b1232`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1232`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

purU (gene.b1232) is a gene entity. It encodes purU (protein.P37051). Encoded protein function: FUNCTION: Catalyzes the hydrolysis of 10-formyltetrahydrofolate (formyl-FH4) to formate and tetrahydrofolate (FH4). Provides the major source of formate for the PurT-dependent synthesis of 5'-phosphoribosyl-N-formylglycinamide (FGAR) during aerobic growth. Has a role in regulating the one-carbon pool. {ECO:0000255|HAMAP-Rule:MF_01927, ECO:0000269|PubMed:7868604}. EcoCyc product frame: FORMYLTHFDEFORMYL-MONOMER. EcoCyc synonyms: ychI, tgs. Genomic coordinates: 1287782-1288624.

## Enriched Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37051|protein.P37051]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004138,ECOCYC:EG11819,GeneID:945827`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1287782-1288624:-; feature_type=gene
