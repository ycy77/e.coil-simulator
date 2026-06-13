---
entity_id: "gene.b2054"
entity_type: "gene"
name: "wcaF"
source_database: "NCBI RefSeq"
source_id: "gene-b2054"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2054"
  - "wcaF"
---

# wcaF

`gene.b2054`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2054`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

wcaF (gene.b2054) is a gene entity. It encodes wcaF (protein.P0ACD2). Encoded protein function: Putative colanic acid biosynthesis acetyltransferase WcaF (EC 2.3.1.-) EcoCyc product frame: G7099-MONOMER. Genomic coordinates: 2128340-2128888. EcoCyc protein note: WcaF is the acetyltransferase that catalyzes acetylation of the fucosyl residue in the UPP-linked disaccharide during biosynthesis of the extracellular polysaccharide CPD-21504 "colanic acid" (CA) . wcaF is located within a cluster of genes that are responsible for production of CA; wcaF was predicted to encode an acetyltransferase responsible for O-acetylation of the first fucosyl group of the CA hexasaccharide . wcaF is required for the production of colanic acid in a CA+ strain of E. coli K-12; a wcaF mutant (CA+wcaF31::cam) has significantly reduced CA production and additionally shows impaired biofilm architecture . Repression of wcaF (using CRISPRi/dCas9) in K-12 MG1655 at the beginning of biofilm culturing significantly inhibits biofilm formation with minimal effect on growth; regulation of wcaF expression allows spatial control of biofilm formation . Expression of wcaF is higher in wild-type biofilms than in biofilms formed by an rpoS mutant . Nomenclature for genes involved in bacterial polysaccharide synthesis is discussed in .

## Biological Role

Activated by nac (protein.Q47005).

## Enriched Pathways

- `eco00543` Exopolysaccharide biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACD2|protein.P0ACD2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=wcaF; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006805,ECOCYC:G7099,GeneID:946578`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2128340-2128888:-; feature_type=gene
