---
entity_id: "protein.P33022"
entity_type: "protein"
name: "rihB"
source_database: "UniProt"
source_id: "P33022"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rihB yeiK b2162 JW2149"
---

# rihB

`protein.P33022`

## Static

- Type: `protein`
- Source: `UniProt:P33022`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Hydrolyzes cytidine or uridine to ribose and cytosine or uracil, respectively. Has a clear preference for cytidine over uridine. Strictly specific for ribonucleosides. Has a low but significant activity for the purine nucleoside xanthosine.

## Biological Role

Catalyzes cytidine ribohydrolase (reaction.R02137). Component of pyrimidine-specific ribonucleoside hydrolase RihB (complex.ecocyc.CPLX0-7904).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: Hydrolyzes cytidine or uridine to ribose and cytosine or uracil, respectively. Has a clear preference for cytidine over uridine. Strictly specific for ribonucleosides. Has a low but significant activity for the purine nucleoside xanthosine.

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R02137|reaction.R02137]] `KEGG` `database` - via EC:3.2.2.8
- `is_component_of` --> [[complex.ecocyc.CPLX0-7904|complex.ecocyc.CPLX0-7904]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b2162|gene.b2162]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33022`
- `KEGG:ecj:JW2149;eco:b2162;ecoc:C3026_12115;`
- `GeneID:946646;`
- `GO:GO:0005509; GO:0005829; GO:0006152; GO:0006206; GO:0008477; GO:0032991; GO:0042802; GO:0045437; GO:0046133; GO:0051289`
- `EC:3.2.2.8`

## Notes

Pyrimidine-specific ribonucleoside hydrolase RihB (EC 3.2.2.8) (Cytidine/uridine-specific hydrolase)
