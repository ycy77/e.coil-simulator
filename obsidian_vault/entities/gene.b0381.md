---
entity_id: "gene.b0381"
entity_type: "gene"
name: "ddlA"
source_database: "NCBI RefSeq"
source_id: "gene-b0381"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0381"
  - "ddlA"
---

# ddlA

`gene.b0381`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0381`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ddlA (gene.b0381) is a gene entity. It encodes ddlA (protein.P0A6J8). Encoded protein function: FUNCTION: Cell wall formation. EcoCyc product frame: DALADALALIGA-MONOMER. Genomic coordinates: 399829-400923. EcoCyc protein note: DdlA is one of two D-alanine—D-alanine ligases in E. coli . D-alanine—D-alanine ligase, along with alanine racemase, makes up the D-alanine branch of peptidoglycan biosynthesis. The enzyme combines two molecules of D-alanine to form D-alanyl-D-alanine, which is then added to the growing cell wall precursor. D-alanine—D-alanine ligase is an antibacterial drug target; it was long known to be the target of D-cycloserine . The Keio collection ddlA mutant is 8-fold more sensitive to X-ray radiation than wild type .

## Biological Role

Repressed by hns (protein.P0ACF8), nac (protein.Q47005).

## Enriched Pathways

- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01502` Vancomycin resistance (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6J8|protein.P0A6J8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=ddlA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0001309,ECOCYC:EG10213,GeneID:945313`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:399829-400923:-; feature_type=gene
