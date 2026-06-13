---
entity_id: "protein.P0AEP3"
entity_type: "protein"
name: "galU"
source_database: "UniProt"
source_id: "P0AEP3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "galU ychD b1236 JW1224"
---

# galU

`protein.P0AEP3`

## Static

- Type: `protein`
- Source: `UniProt:P0AEP3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: May play a role in stationary phase survival.

## Biological Role

Catalyzes UTP:alpha-D-glucose-1-phosphate uridylyltransferase (reaction.R00289). Component of UTP—glucose-1-phosphate uridylyltransferase (complex.ecocyc.CPLX0-8205).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

FUNCTION: May play a role in stationary phase survival.

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00289|reaction.R00289]] `KEGG` `database` - via EC:2.7.7.9
- `is_component_of` --> [[complex.ecocyc.CPLX0-8205|complex.ecocyc.CPLX0-8205]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b1236|gene.b1236]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEP3`
- `KEGG:ecj:JW1224;eco:b1236;ecoc:C3026_07270;`
- `GeneID:93775302;945730;`
- `GO:GO:0000287; GO:0003983; GO:0005829; GO:0006011; GO:0009242; GO:0009244; GO:0032991; GO:0033499; GO:0042802; GO:1900727`
- `EC:2.7.7.9`

## Notes

UTP--glucose-1-phosphate uridylyltransferase (EC 2.7.7.9) (Alpha-D-glucosyl-1-phosphate uridylyltransferase) (UDP-Glc PPase) (UDP-glucose pyrophosphorylase) (UDPGP) (Uridine diphosphoglucose pyrophosphorylase)
