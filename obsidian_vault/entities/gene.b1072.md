---
entity_id: "gene.b1072"
entity_type: "gene"
name: "flgA"
source_database: "NCBI RefSeq"
source_id: "gene-b1072"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1072"
  - "flgA"
---

# flgA

`gene.b1072`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1072`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

flgA (gene.b1072) is a gene entity. It encodes flgA (protein.P75933). Encoded protein function: FUNCTION: Involved in the assembly process of the P-ring formation. It may associate with FlgF on the rod constituting a structure essential for the P-ring assembly or may act as a modulator protein for the P-ring assembly. EcoCyc product frame: G357-MONOMER. EcoCyc synonyms: flaU. Genomic coordinates: 1130204-1130863. EcoCyc protein note: FlgA and FlgI are required for the assembly of the flagellar P ring. Experiments with Salmonella typhimurium show FlgA is produced as a precursor and transported to the periplasm through the Sec pathway to assist in the assembly of the flagellar P ring. FlgA, which is normally unstable, has been shown to be stabilized by the presence of FlgI, suggesting an interaction exists between the two proteins. FlgA is predicted to act as a chaperone for polymerization of FlgI onto the P ring . Early studies in E. coli K-12 identified the flaU gene within the region I fla (flagella) genes (see ). Incomplete flagella structures are detected in mutants with defects in flaU . flgA mutants ('Ec:flgAi') are non-motile . For a description of flagellar gene nomenclature, including old (fla, flb) and new (flg, flh and fli) symbols, see . The 'pole-localizer' protein G7087-MONOMER TmaR protects and stabilizes flgA transcripts .

## Enriched Pathways

- `eco02040` Flagellar assembly (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75933|protein.P75933]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003637,ECOCYC:G357,GeneID:946300`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1130204-1130863:-; feature_type=gene
