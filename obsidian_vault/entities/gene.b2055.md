---
entity_id: "gene.b2055"
entity_type: "gene"
name: "wcaE"
source_database: "NCBI RefSeq"
source_id: "gene-b2055"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2055"
  - "wcaE"
---

# wcaE

`gene.b2055`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2055`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

wcaE (gene.b2055) is a gene entity. It encodes wcaE (protein.P71239). Encoded protein function: Putative colanic acid biosynthesis glycosyl transferase WcaE EcoCyc product frame: G7100-MONOMER. Genomic coordinates: 2128904-2129650. EcoCyc protein note: wcaE is located within a cluster of genes that are responsible for production of CPD-21504 "colanic acid" (CA); wcaE was predicted to encode a glycosyltransferase involved in CA biosynthesis . WcaE was later shown to be a fucosyltransferase that catalyzes transfer of a fucosyl residue to the UPP-linked acetylated disaccharide during biosynthesis of the extracellular polysaccharide CPD-21504 "colanic acid" . The Keio collection wcaE mutant is sensitive to lithium (<90% growth at 100mM Li) . Nomenclature for genes involved in bacterial polysaccharide synthesis is discussed in .

## Biological Role

Activated by nac (protein.Q47005).

## Enriched Pathways

- `eco00543` Exopolysaccharide biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P71239|protein.P71239]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=wcaE; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006807,ECOCYC:G7100,GeneID:946543`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2128904-2129650:-; feature_type=gene
