---
entity_id: "gene.b0915"
entity_type: "gene"
name: "lpxK"
source_database: "NCBI RefSeq"
source_id: "gene-b0915"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0915"
  - "lpxK"
---

# lpxK

`gene.b0915`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0915`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lpxK (gene.b0915) is a gene entity. It encodes lpxK (protein.P27300). Encoded protein function: FUNCTION: Transfers the gamma-phosphate of ATP to the 4'-position of a tetraacyldisaccharide 1-phosphate intermediate (termed DS-1-P) to form tetraacyldisaccharide 1,4'-bis-phosphate (lipid IVA). {ECO:0000269|PubMed:9268317, ECO:0000269|PubMed:9575203}. EcoCyc product frame: TETRAACYLDISACC4KIN-MONOMER. EcoCyc synonyms: ycaH. Genomic coordinates: 968366-969352. EcoCyc protein note: Tetraacyldisaccharide 4'-kinase (LpxK) catalyzes the sixth step in lipid A biosynthesis. LpxK transfers a phosphate from ATP to the 4' position of a tetraacyldisaccharide1-phosphate intermediate to form tetraacyldisaccharide 1,4'-bis-phosphate (lipid IVA). The reaction requires Mg2+ and is stimulated by phospholipids. Though it can function with all nucleotide triphosphates, the enzymatic reaction is most efficient with ATP . LpxK is an integral membrane protein, which contains predicted membrane-spanning segments at its N-terminus. Most of the LpxK sedimented with the membrane pellet rather than the cell free extract. lpxK is an essential gene, which cotranscribes with msbA . msbA is also an essential gene which codes for a transport protein that brings lipid A from the inner membrane to the outer membrane . LpxK from Aquifex aeolicus has been characterized...

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P27300|protein.P27300]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003115,ECOCYC:EG11409,GeneID:945526`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:968366-969352:+; feature_type=gene
