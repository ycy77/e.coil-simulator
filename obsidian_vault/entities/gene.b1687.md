---
entity_id: "gene.b1687"
entity_type: "gene"
name: "ydiJ"
source_database: "NCBI RefSeq"
source_id: "gene-b1687"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1687"
  - "ydiJ"
---

# ydiJ

`gene.b1687`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1687`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydiJ (gene.b1687) is a gene entity. It encodes ydiJ (protein.P77748). Encoded protein function: FUNCTION: Catalyzes the oxidation of D-2-hydroxyglutarate (D-2-HGA) to 2-oxoglutarate. Appears to be the only D2HGDH in E.coli, providing the way to recycle D-2-HGA produced during L-serine synthesis by SerA, by converting it back to 2-oxoglutarate. The physiological molecule that functions as the primary electron acceptor during D-2-HGA oxidation by YdiJ in E.coli is unknown. Shows strict substrate specificity towards D-2-HGA, since it has no detectable activity on L-2-hydroxyglutarate, L-malate, D-malate, L-lactate, D-lactate, L-tartrate, D-tartrate, L-glycerate, D-glycerate, glutarate, or pyruvate. {ECO:0000269|PubMed:36144368}. EcoCyc product frame: G6913-MONOMER. Genomic coordinates: 1765629-1768685.

## Enriched Pathways

- `eco00310` Lysine degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77748|protein.P77748]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005632,ECOCYC:G6913,GeneID:946189`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1765629-1768685:-; feature_type=gene
