---
entity_id: "gene.b4407"
entity_type: "gene"
name: "thiS"
source_database: "NCBI RefSeq"
source_id: "gene-b4407"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4407"
  - "thiS"
---

# thiS

`gene.b4407`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4407`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

thiS (gene.b4407) is a gene entity. It encodes thiS (protein.O32583). Encoded protein function: FUNCTION: Is the sulfur donor in the synthesis of the thiazole phosphate moiety of thiamine phosphate. {ECO:0000269|PubMed:9632726}. EcoCyc product frame: THIS-MONOMER. EcoCyc synonyms: thiG1. Genomic coordinates: 4192637-4192837. EcoCyc protein note: ThiS is a sulfur carrier protein that provides the sulfur source for the thiazole moiety in thiamine biosynthesis. In a reaction catalyzed by CPLX0-8558 ThiF, the C-terminal cysteine residue of ThiS is adenylated, yielding ThiS-COAMP . Sulfurylated-ThiI may then transfer its sulfur to ThiS-COAMP, releasing AMP and forming a covalent disulfide bond, ThiS-ThiI-disulfides intermediate. ThiS then appears to be transferred to ThiF, again forming a covalent disulfide bond, ThiS-ThiF-disulfides intermediate . However, it has not been experimentally determined when and how the disulfide bond is reduced to enable the final sulfur transfer to form thiazole. A solution structure of ThiS shows a ubiquitin-like fold . The crystal structure of the ThiS-ThiF protein complex shows a dimer of heterodimers, where the dimer interface is provided by ThiF. The ThiS C-terminus is located near the active site . Reviews: Note: indicates that is retracted.

## Enriched Pathways

- `eco04122` Sulfur relay system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.O32583|protein.O32583]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0023907,ECOCYC:G1,GeneID:2847702`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4192637-4192837:-; feature_type=gene
