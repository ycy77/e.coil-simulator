---
entity_id: "gene.b4084"
entity_type: "gene"
name: "alsK"
source_database: "NCBI RefSeq"
source_id: "gene-b4084"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4084"
  - "alsK"
---

# alsK

`gene.b4084`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4084`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

alsK (gene.b4084) is a gene entity. It encodes alsK (protein.P32718). Encoded protein function: FUNCTION: Catalyzes the phosphorylation of D-allose to D-allose 6-phosphate. Also has low level glucokinase activity in vitro. {ECO:0000255|HAMAP-Rule:MF_00988, ECO:0000269|PubMed:17979299, ECO:0000269|PubMed:9401019}. EcoCyc product frame: EG11956-MONOMER. EcoCyc synonyms: yjcT. Genomic coordinates: 4306870-4307799. EcoCyc protein note: The alsK gene encodes a D-allose kinase. Its role in the degradation of D-allose is unclear; AlsK is not required for utilization of a D-allose carbon source; this effect may be due to the presence of other ambiguous sugar kinases within E. coli K-12 . Expression of alsK appears to be unaffected by allose . Overexpression of alsK rescues the auxotrophic phenotype of a glucokinase mutant . The low glucokinase activity of AlsK can be improved by experimental evolution . Als: "D-allose"

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32718|protein.P32718]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013380,ECOCYC:EG11956,GeneID:948596`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4306870-4307799:-; feature_type=gene
