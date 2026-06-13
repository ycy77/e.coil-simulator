---
entity_id: "gene.b1081"
entity_type: "gene"
name: "flgJ"
source_database: "NCBI RefSeq"
source_id: "gene-b1081"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1081"
  - "flgJ"
---

# flgJ

`gene.b1081`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1081`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

flgJ (gene.b1081) is a gene entity. It encodes flgJ (protein.P75942). Encoded protein function: FUNCTION: Flagellum-specific muramidase which hydrolyzes the peptidoglycan layer to assemble the rod structure in the periplasmic space. {ECO:0000250}. EcoCyc product frame: G366-MONOMER. EcoCyc synonyms: flaZ. Genomic coordinates: 1137371-1138312. EcoCyc protein note: FlgJ has been largely characterized in Salmonella Typhimurium where it is a bifunctional, periplasmic protein required for flagella rod assembly and possessing endo β-N-acetylglucosaminidase activity; this latter activity is associated with the C-terminal region of the protein and may function to create holes in the peptidoglycan layer for flagella assembly . FlgJ from E. coli K-12 has 83% identity with FlgJ from Salmonella Typhimurium. The Keio collection flgJ mutant exhibits a 'low level' of resistance to lithium exposure . Early studies in E. coli K-12 identified the flaZ gene within the region I fla (flagella) genes (see ). flgJ mutants ('Ec:flgJi') are non-motile . For a description of flagellar gene nomenclature, including old (fla, flb) and new (flg, flh and fli) symbols, see .

## Enriched Pathways

- `eco02040` Flagellar assembly (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75942|protein.P75942]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003658,ECOCYC:G366,GeneID:947456`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1137371-1138312:+; feature_type=gene
