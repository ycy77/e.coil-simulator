---
entity_id: "gene.b2059"
entity_type: "gene"
name: "wcaA"
source_database: "NCBI RefSeq"
source_id: "gene-b2059"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2059"
  - "wcaA"
---

# wcaA

`gene.b2059`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2059`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

wcaA (gene.b2059) is a gene entity. It encodes wcaA (protein.P77414). Encoded protein function: Putative colanic acid biosynthesis glycosyl transferase WcaA EcoCyc product frame: G7104-MONOMER. Genomic coordinates: 2132558-2133397. EcoCyc protein note: WcaA is a glucoronosyltransferase that catalyzes transfer of a glucoronate residue to the UPP-linked diacetylated tetrasaccharide during biosynthesis of the extracellular polysaccharide CPD-21504 "colanic acid" (CA) . wcaA is located within a cluster of genes that are responsible for production of CA; wcaA was predicted to encode a glycosyltransferase involved in CA biosynthesis . Nomenclature for genes involved in bacterial polysaccharide synthesis is discussed in .

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00543` Exopolysaccharide biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77414|protein.P77414]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=wcaA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006816,ECOCYC:G7104,GeneID:946570`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2132558-2133397:-; feature_type=gene
