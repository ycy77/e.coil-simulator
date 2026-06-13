---
entity_id: "protein.P31677"
entity_type: "protein"
name: "otsA"
source_database: "UniProt"
source_id: "P31677"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "otsA b1896 JW5312"
---

# otsA

`protein.P31677`

## Static

- Type: `protein`
- Source: `UniProt:P31677`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the transfer of glucose from UDP-alpha-D-glucose (UDP-Glc) to D-glucose 6-phosphate (Glc-6-P) to form trehalose-6-phosphate. Acts with retention of the anomeric configuration of the UDP-sugar donor. Essential for viability of the cells at low temperatures and at elevated osmotic strength. {ECO:0000269|PubMed:12105274, ECO:0000269|PubMed:1310094, ECO:0000269|PubMed:20077550, ECO:0000269|PubMed:3131312}.

## Biological Role

Catalyzes UDP-glucose:D-glucose-6-phosphate 1-alpha-D-glucosyltransferase (reaction.R00836). Component of OtsA homodimer (complex.ecocyc.CPLX0-13742), trehalose-6-phosphate synthase (complex.ecocyc.CPLX0-13749).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Catalyzes the transfer of glucose from UDP-alpha-D-glucose (UDP-Glc) to D-glucose 6-phosphate (Glc-6-P) to form trehalose-6-phosphate. Acts with retention of the anomeric configuration of the UDP-sugar donor. Essential for viability of the cells at low temperatures and at elevated osmotic strength. {ECO:0000269|PubMed:12105274, ECO:0000269|PubMed:1310094, ECO:0000269|PubMed:20077550, ECO:0000269|PubMed:3131312}.

## Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00836|reaction.R00836]] `KEGG` `database` - via EC:2.4.1.15
- `is_component_of` --> [[complex.ecocyc.CPLX0-13742|complex.ecocyc.CPLX0-13742]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-13749|complex.ecocyc.CPLX0-13749]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b1896|gene.b1896]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31677`
- `KEGG:ecj:JW5312;eco:b1896;ecoc:C3026_10770;`
- `GeneID:93776199;946405;`
- `GO:GO:0003825; GO:0005992; GO:0006950; GO:0006970; GO:0006974; GO:0070417`
- `EC:2.4.1.15`

## Notes

Trehalose-6-phosphate synthase (TPS) (EC 2.4.1.15) (Alpha,alpha-trehalose-phosphate synthase [UDP-forming]) (Osmoregulatory trehalose synthesis protein A) (OtsA) (UDP-glucose-glucosephosphate glucosyltransferase)
