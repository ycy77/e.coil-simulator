---
entity_id: "gene.b3879"
entity_type: "gene"
name: "yihR"
source_database: "NCBI RefSeq"
source_id: "gene-b3879"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3879"
  - "yihR"
---

# yihR

`gene.b3879`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3879`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yihR (gene.b3879) is a gene entity. It encodes yihR (protein.P32139). Encoded protein function: Uncharacterized protein YihR EcoCyc product frame: EG11844-MONOMER. EcoCyc synonyms: squR. Genomic coordinates: 4069475-4070401. EcoCyc protein note: YihR may be a sulfoquinovose mutarotase. The gene cluster encoding enzymes of the sulfoquinovose degradation pathway is conserved. The YihR homolog of Herbaspirillum seropedicaea was shown to have sulfoquinovose mutarotase activity . Note, however, that the best BLAST hit of the H. seropedicaea protein in the E. coli genome is G7338-MONOMER YphB rather than YihR. YihR appears to be involved in biofilm formation. A mutant with a deletion of yihR shows a significant decrease in biofilm formation . Expression of yihR increases 11-fold upon deletion of tqsA (which increases biofilm formation) , and is induced by growth on sulfoquinovose .

## Enriched Pathways

- `eco00566` Sulfoquinovose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32139|protein.P32139]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012669,ECOCYC:EG11844,GeneID:948375`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4069475-4070401:-; feature_type=gene
