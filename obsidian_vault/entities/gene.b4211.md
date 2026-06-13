---
entity_id: "gene.b4211"
entity_type: "gene"
name: "qorB"
source_database: "NCBI RefSeq"
source_id: "gene-b4211"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4211"
  - "qorB"
---

# qorB

`gene.b4211`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4211`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

qorB (gene.b4211) is a gene entity. It encodes qorB (protein.P39315). Encoded protein function: FUNCTION: Quinone oxidoreductase that may play some additional role beyond quinone reduction. Potential redox sensor protein. Overexpression induces retardation of growth. {ECO:0000269|PubMed:18455185}. EcoCyc product frame: G7868-MONOMER. EcoCyc synonyms: ytfG. Genomic coordinates: 4433164-4434024. EcoCyc protein note: QorB is an NAD(P)H:quinone oxidoreductase. EPR and kinetic studies suggest that the enzyme catalyzes the two-electron reduction of quinones using a ping-pong mechanism. Crystal structures of the enzyme alone and in complex with NADPH have been solved . QorB shows very low flavin reductase activity and ferrous iron release activity in the presence of free FAD . A qorB mutant shows no significant growth phenotype, while overexpression of qorB leads to growth retardation and lowered expression of a number of proteins involved in carbon metabolism . The gene was identified by a computational analysis as a candidate for encoding resistance to the antiobiotic CPD-9195. Resistance was confirmed by wet-lab experiments that compared the minimum inhibitory concentration (MIC) of a knock-out strain to that of the wild-type strain . QorB: "NAD(P)H-dependent quinone oxidoreductase"

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39315|protein.P39315]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013773,ECOCYC:G7868,GeneID:948731`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4433164-4434024:-; feature_type=gene
