---
entity_id: "gene.b2050"
entity_type: "gene"
name: "wcaI"
source_database: "NCBI RefSeq"
source_id: "gene-b2050"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2050"
  - "wcaI"
---

# wcaI

`gene.b2050`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2050`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

wcaI (gene.b2050) is a gene entity. It encodes wcaI (protein.P32057). Encoded protein function: Putative colanic acid biosynthesis glycosyl transferase WcaI EcoCyc product frame: EG11790-MONOMER. EcoCyc synonyms: yefD. Genomic coordinates: 2124523-2125746. EcoCyc protein note: WcaI is the fucosyltransferase that catalyzes the transfer of unmodified fucose to CPD-12773 UPP-Glc in the biosynthesis of the extracellular polysaccharide CPD-21504 colanic acid (CA) . wcaI is located within a cluster of genes that are responsible for production of CA; wcaI was predicted to encode a glycosyl transferase involved in the process . Expression of wcaI is higher in wild-type biofilms than in biofilms formed by an rpoS mutant . The Keio collection wcaI mutant is sensitive to lithium (<90% growth at 200mM Li) . Nomenclature for genes involved in bacterial polysaccharide synthesis is discussed in .

## Enriched Pathways

- `eco00543` Exopolysaccharide biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32057|protein.P32057]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006794,ECOCYC:EG11790,GeneID:946588`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2124523-2125746:-; feature_type=gene
