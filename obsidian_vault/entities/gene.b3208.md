---
entity_id: "gene.b3208"
entity_type: "gene"
name: "mtgA"
source_database: "NCBI RefSeq"
source_id: "gene-b3208"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3208"
  - "mtgA"
---

# mtgA

`gene.b3208`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3208`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mtgA (gene.b3208) is a gene entity. It encodes mtgA (protein.P46022). Encoded protein function: FUNCTION: Peptidoglycan polymerase that catalyzes glycan chain elongation from lipid-linked precursors (PubMed:18165305, PubMed:6368264, PubMed:8772200). May play a role in peptidoglycan assembly during cell division in collaboration with other cell division proteins (PubMed:18165305). {ECO:0000269|PubMed:18165305, ECO:0000269|PubMed:6368264, ECO:0000269|PubMed:8772200}. EcoCyc product frame: G7668-MONOMER. EcoCyc synonyms: mgt, yrbM. Genomic coordinates: 3349081-3349809. EcoCyc protein note: MtgA is a monofunctional murein glycosyltransferase involved in polymerization of lipid II molecules into glycan strands of peptidoglycan. GFP-MtgA fusions localize to the division site in mrcA(ts) mrcB mutants . Bacterial two-hybrid experiments reveal MtgA interacts with PBP3, FtsW, and FtsN . Assays for peptidoglycan synthesis activity revealed that MtgA has glycosyltransferase activity and polymerizes glycan strands with lipid II as substrate at an optimum pH of 6.0 to 6.5 . This differs from the optimum of 7.5 to 8.0 for PBP1B, which is the major bifunctional glycosyltransferase for peptidoglycan synthesis in E. coli . The glycan strands were then shown to act as substrate for lysozyme...

## Enriched Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P46022|protein.P46022]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010530,ECOCYC:G7668,GeneID:947728`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3349081-3349809:-; feature_type=gene
