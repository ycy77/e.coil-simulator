---
entity_id: "gene.b2264"
entity_type: "gene"
name: "menD"
source_database: "NCBI RefSeq"
source_id: "gene-b2264"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2264"
  - "menD"
---

# menD

`gene.b2264`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2264`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

menD (gene.b2264) is a gene entity. It encodes menD (protein.P17109). Encoded protein function: FUNCTION: Catalyzes the thiamine diphosphate-dependent decarboxylation of 2-oxoglutarate and the subsequent addition of the resulting succinic semialdehyde-thiamine pyrophosphate anion to isochorismate to yield 2-succinyl-5-enolpyruvyl-6-hydroxy-3-cyclohexene-1-carboxylate (SEPHCHC). {ECO:0000255|HAMAP-Rule:MF_01659, ECO:0000269|PubMed:17760421}. EcoCyc product frame: MEND-MONOMER. Genomic coordinates: 2377589-2379259.

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P17109|protein.P17109]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007482,ECOCYC:EG10579,GeneID:946720`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2377589-2379259:-; feature_type=gene
