---
entity_id: "gene.b0841"
entity_type: "gene"
name: "ybjG"
source_database: "NCBI RefSeq"
source_id: "gene-b0841"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0841"
  - "ybjG"
---

# ybjG

`gene.b0841`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0841`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybjG (gene.b0841) is a gene entity. It encodes ybjG (protein.P75806). Encoded protein function: FUNCTION: Overexpression leads to increased undecaprenyl diphosphatase activity and to increased resistance to bacitracin. May have a preferred substrate other than undecaprenyl diphosphate in vivo. {ECO:0000269|PubMed:15778224}. EcoCyc product frame: G6439-MONOMER. Genomic coordinates: 882792-883388. EcoCyc protein note: YbjG is similar to the bacitracin resistance protein BcrC of Bacillus licheniformis. Disruption of ybjG causes increased bacitracin sensitivity, and overexpression causes increased resistance to bacitracin . Simultaneous inactivation of ybjG, EG11665 bacA, and EG10705 pgpB is lethal. Depletion of BacA in the triple mutant strain causes changes in cell morphology and lysis. Overexpression of ybjG, G7146 lpxT, bacA, or pgpB leads to increased undecaprenyl diphosphate (C55PP) phosphatase activity in crude membrane extracts. Expression of C55PP phosphatase activity from one of the three genes ybjG, bacA, and pgpB appears to be sufficient for synthesis of undecaprenyl phosphate and survival . bacA ybjG double and bacA ybjG lpxT triple deletion mutants are hypersensitive to the undecaprenyl phosphate biosynthesis inhibitor fosmidomycin . YbjG is an inner membrane protein with four transmembrane domains . The C terminus is located in the cytoplasm...

## Enriched Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco00552` Teichoic acid biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75806|protein.P75806]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002865,ECOCYC:G6439,GeneID:945450`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:882792-883388:-; feature_type=gene
