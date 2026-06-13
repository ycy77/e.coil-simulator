---
entity_id: "gene.b0634"
entity_type: "gene"
name: "mrdB"
source_database: "NCBI RefSeq"
source_id: "gene-b0634"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0634"
  - "mrdB"
---

# mrdB

`gene.b0634`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0634`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mrdB (gene.b0634) is a gene entity. It encodes mrdB (protein.P0ABG7). Encoded protein function: FUNCTION: Peptidoglycan polymerase that is essential for cell wall elongation (PubMed:27643381, PubMed:37620344). Also required for the maintenance of the rod cell shape (PubMed:2644207). Functions probably in conjunction with the penicillin-binding protein 2 (mrdA) (PubMed:2644207, PubMed:27643381, PubMed:37620344). {ECO:0000269|PubMed:2644207, ECO:0000269|PubMed:27643381, ECO:0000269|PubMed:37620344}. EcoCyc product frame: EG10607-MONOMER. EcoCyc synonyms: rodA. Genomic coordinates: 665201-666313. EcoCyc protein note: The SEDS family protein MrdB (also called RodA) is believed to be the primary peptidoglycan (PG) glycosyltransferase which functions together with its cognate transpeptidase EG10606-MONOMER "PBP2" (MrdA) to synthesize PG during cell elongation; MrdB-PBP2 are the SEDS-bPBP pair of the elongasome/Rod system. A model of SEDS-bPBP catalysed peptidoglycan synthesis has been generated based on the structural, biochemical, genetic, and computational analyses of a RodA-PBP2 fusion protein . MrdB displays EG10608-MONOMER "MreB"-like directional motion and has been implicated as the core glycosyltransferase of peptidoglycan synthesis during cell elongation...

## Enriched Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABG7|protein.P0ABG7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002173,ECOCYC:EG10607,GeneID:945238`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:665201-666313:-; feature_type=gene
