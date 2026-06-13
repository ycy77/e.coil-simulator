---
entity_id: "gene.b3825"
entity_type: "gene"
name: "pldB"
source_database: "NCBI RefSeq"
source_id: "gene-b3825"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3825"
  - "pldB"
---

# pldB

`gene.b3825`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3825`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pldB (gene.b3825) is a gene entity. It encodes pldB (protein.P07000). Encoded protein function: Lysophospholipase L2 (EC 3.1.1.5) (Lecithinase B) EcoCyc product frame: EG10739-MONOMER. Genomic coordinates: 4009170-4010192. EcoCyc protein note: Lysophospholipase L2 (PldB) hydrolyzes the acyl-ester bond of acyl-lysophospholipids. The most effective substrates of the purified enzyme in vitro are 2-acyl glycerophosphoethanolamine and 2-acyl glycerophosphocholine; the 1-acyl versions of each compound are hydrolyzed somewhat less effectively. Purified PldB can also transfer an acyl group from acyl-lysophospholipids to phosphatidylglycerol to yield acyl phosphatidylglycerol; the enzyme is more active with 2-acyl donors (2-acyl glycerophosphoethanolamine and 2-acyl glycerophosphocholine) than 1-acyl donors . PldB does not contain an obvious signal sequence or transmembrane domain and is thought to be associated with the cytoplasmic side of the inner membrane . Mutants with altered lysophospholipase activity have been isolated . PldB: "phospholipid degradation B"

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P07000|protein.P07000]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012494,ECOCYC:EG10739,GeneID:948314`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4009170-4010192:+; feature_type=gene
