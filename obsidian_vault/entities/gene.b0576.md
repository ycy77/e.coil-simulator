---
entity_id: "gene.b0576"
entity_type: "gene"
name: "pheP"
source_database: "NCBI RefSeq"
source_id: "gene-b0576"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0576"
  - "pheP"
---

# pheP

`gene.b0576`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0576`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pheP (gene.b0576) is a gene entity. It encodes pheP (protein.P24207). Encoded protein function: FUNCTION: Permease that is involved in the active transport across the cytoplasmic membrane of phenylalanine (PubMed:10735864, PubMed:1711024, PubMed:8226700, PubMed:9791098). Can also transport tyrosine, but not tryptophan (PubMed:10735864). {ECO:0000269|PubMed:10735864, ECO:0000269|PubMed:1711024, ECO:0000269|PubMed:8226700, ECO:0000269|PubMed:9791098}. EcoCyc product frame: PHEP-MONOMER. Genomic coordinates: 601959-603335. EcoCyc protein note: PheP is a phenylalanine transporter that is a member of the Amino Acid-Polyamine-Organocation (APC) Superfamily of transporters . Complementation of a pheP mutant restored phenylalanine-specific transport activity, indicating that PheP is normally responsible for phenylalanine transport . Experiments with oxidative phosphorylation uncouplers and E. coli strains deficient in the F0F1-ATPase suggest that PheP-mediated transport is driven by the proton motive force . PheP probably functions as a phenylalanine/proton symporter. PheP shares sequence similarity with AroP, which is a general aromatic amino acid transport system, responsible for phenylalanine, tyrosine, and tryptophan transport . Hydropathy analysis and PhoA fusion suggests that PheP has a 12 transmembrane segment topology .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P24207|protein.P24207]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001976,ECOCYC:EG10708,GeneID:945199`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:601959-603335:+; feature_type=gene
