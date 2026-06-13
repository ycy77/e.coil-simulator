---
entity_id: "gene.b0801"
entity_type: "gene"
name: "hcxB"
source_database: "NCBI RefSeq"
source_id: "gene-b0801"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0801"
  - "hcxB"
---

# hcxB

`gene.b0801`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0801`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hcxB (gene.b0801) is a gene entity. It encodes hcxB (protein.P30178). Encoded protein function: FUNCTION: Catalyzes the NAD(P)H-dependent reduction of 2-oxoglutarate, phenylpyruvate and (4-hydroxyphenyl)pyruvate, leading to the respective 2-hydroxycarboxylate in vitro. Shows a preference for NADPH over NADH as a redox partner. Do not catalyze the reverse reactions. {ECO:0000269|PubMed:27941785}. EcoCyc product frame: EG11581-MONOMER. EcoCyc synonyms: ybiC. Genomic coordinates: 836351-837436. EcoCyc protein note: The hydroxycarboxylate dehydrogenase activity of HcxB was discovered in a large-scale metabolomics screen for enzymatic activities of uncharacterized proteins in E. coli . HcxB: "hydroxycarboxylic acid dehydrogenase B"

## Enriched Pathways

- `eco00350` Tyrosine metabolism (KEGG)
- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P30178|protein.P30178]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002738,ECOCYC:EG11581,GeneID:945412`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:836351-837436:+; feature_type=gene
