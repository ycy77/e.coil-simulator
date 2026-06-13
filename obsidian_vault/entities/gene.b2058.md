---
entity_id: "gene.b2058"
entity_type: "gene"
name: "wcaB"
source_database: "NCBI RefSeq"
source_id: "gene-b2058"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2058"
  - "wcaB"
---

# wcaB

`gene.b2058`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2058`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

wcaB (gene.b2058) is a gene entity. It encodes wcaB (protein.P0ACC9). Encoded protein function: Putative colanic acid biosynthesis acetyltransferase WcaB (EC 2.3.1.-) EcoCyc product frame: G7103-MONOMER. Genomic coordinates: 2132067-2132555. EcoCyc protein note: WcaB is the acetyltransferase that catalyzes acetylation of the galactosyl residue in the UPP-linked tetrasaccharide during biosynthesis of the extracellular polysaccharide CPD-21504 "colanic acid" (CA) . wcaB is located within a cluster of genes that are responsible for production of CA; wcaB was predicted to encode an acetyltransferase responsible for O-acetylation of the first fucosyl group of the CA hexasaccharide . wcaB is not expressed when cells are cultured aerobically in rich medium at 37°C . Nomenclature for genes involved in bacterial polysaccharide synthesis is discussed in .(There may be confusion in the literature between wcaB and EG10161 cpsB .)

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00543` Exopolysaccharide biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACC9|protein.P0ACC9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=wcaB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006813,ECOCYC:G7103,GeneID:946573`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2132067-2132555:-; feature_type=gene
