---
entity_id: "gene.b1686"
entity_type: "gene"
name: "menI"
source_database: "NCBI RefSeq"
source_id: "gene-b1686"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1686"
  - "menI"
---

# menI

`gene.b1686`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1686`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

menI (gene.b1686) is a gene entity. It encodes menI (protein.P77781). Encoded protein function: FUNCTION: Catalyzes the hydrolysis of 1,4-dihydroxy-2-naphthoyl-CoA (DHNA-CoA) to 1,4-dihydroxy-2-naphthoate (DHNA). Also shows significant activity toward a wide range of acyl-CoA thioesters, and minimal activity toward benzoyl-holoEntB. {ECO:0000269|PubMed:15808744, ECO:0000269|PubMed:23564174, ECO:0000269|PubMed:24992697}. EcoCyc product frame: G6912-MONOMER. EcoCyc synonyms: ydiI. Genomic coordinates: 1765222-1765632.

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77781|protein.P77781]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005628,ECOCYC:G6912,GeneID:946190`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1765222-1765632:-; feature_type=gene
