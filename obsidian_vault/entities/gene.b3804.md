---
entity_id: "gene.b3804"
entity_type: "gene"
name: "hemD"
source_database: "NCBI RefSeq"
source_id: "gene-b3804"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3804"
  - "hemD"
---

# hemD

`gene.b3804`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3804`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hemD (gene.b3804) is a gene entity. It encodes hemD (protein.P09126). Encoded protein function: FUNCTION: Catalyzes cyclization of the linear tetrapyrrole, hydroxymethylbilane, to the macrocyclic uroporphyrinogen III. {ECO:0000250}. EcoCyc product frame: UROGENIIISYN-MONOMER. Genomic coordinates: 3989088-3989828. EcoCyc protein note: Uroporphyrinogen III synthase catalyzes the cyclization of hydroxymethylbilane with inversion of ring D to form uroporphyrinogen III, the last common intermediate in the heme and corrin (B-12) pathways . Uroporphyrinogen III synthase forms a complex with hydroxymethylbilane synthase . The hemD gene which encodes uroporphyrinogen III synthase has been cloned, and the product has been overexpressed, purified and characterized . The hemD gene is adjacent to hemC and both genes appear to be transcribed by the same promoter . A group of hemin requiring mutants had defects in uroporphyrinogen III synthase .

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P09126|protein.P09126]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012425,ECOCYC:EG10430,GeneID:948587`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3989088-3989828:-; feature_type=gene
