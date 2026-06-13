---
entity_id: "protein.P30011"
entity_type: "protein"
name: "nadC"
source_database: "UniProt"
source_id: "P30011"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nadC b0109 JW0105"
---

# nadC

`protein.P30011`

## Static

- Type: `protein`
- Source: `UniProt:P30011`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the catabolism of quinolinic acid (QA). {ECO:0000269|PubMed:8561507}. Quinolinate phosphoribosyltransferase (NadC) catalyzes the third step in the de novo biosynthesis of NAD from L-aspartate . nadC mutants excrete quinolinate . NadC: "NAD biosynthesis"

## Biological Role

Component of quinolinate phosphoribosyltransferase (decarboxylating) (complex.ecocyc.QUINOPRIBOTRANS-CPLX).

## Enriched Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Involved in the catabolism of quinolinic acid (QA). {ECO:0000269|PubMed:8561507}.

## Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.QUINOPRIBOTRANS-CPLX|complex.ecocyc.QUINOPRIBOTRANS-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0109|gene.b0109]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P30011`
- `KEGG:ecj:JW0105;eco:b0109;ecoc:C3026_00450;`
- `GeneID:948869;`
- `GO:GO:0004514; GO:0005737; GO:0005829; GO:0009435; GO:0034213; GO:0034628`
- `EC:2.4.2.19`

## Notes

Nicotinate-nucleotide pyrophosphorylase [carboxylating] (EC 2.4.2.19) (Quinolinate phosphoribosyltransferase [decarboxylating]) (QAPRTase)
