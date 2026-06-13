---
entity_id: "gene.b0325"
entity_type: "gene"
name: "yahK"
source_database: "NCBI RefSeq"
source_id: "gene-b0325"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0325"
  - "yahK"
---

# yahK

`gene.b0325`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0325`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yahK (gene.b0325) is a gene entity. It encodes yahK (protein.P75691). Encoded protein function: FUNCTION: Catalyzes the reduction of a wide range of aldehydes into their corresponding alcohols. Has a strong preference for NADPH over NADH as the electron donor. Cannot use a ketone as substrate. Is a major source of NADPH-dependent aldehyde reductase activity in E.coli. The in vivo functions of YahK has yet to be determined. {ECO:0000269|PubMed:23093176}. EcoCyc product frame: G6190-MONOMER. Genomic coordinates: 342884-343933. EcoCyc protein note: YahK is a member of the zinc-containing medium-chain dehydrogenase/reductase family. The enzyme is a major source of NADPH-dependent aldehyde reductase activity in the cell. Catalytic activity of the purified enzyme was measured with a variety of aldehyde substrates . In a metabolically engineered strain, phenylacetaldehyde and 4-hydroxyphenylacetaldehyde are reduced to 2-phenylethanol and 2-(4-hydroxyphenyl)ethanol by the endogenous aldehyde reductases YqhD, YjgB, and YahK . In a different engineered strain LACTALD and CPD-358 were reduced to the corresponding forms of DL-12-Propanediol "propane-1,2-diol" . Conversely, a broad survey of aldehyde reductases showed that YahK was one of several endogenous aldehyde reductases that contribute to the degradation of desired aldehyde end products of metabolic engineering...

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75691|protein.P75691]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001113,ECOCYC:G6190,GeneID:944975`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:342884-343933:+; feature_type=gene
