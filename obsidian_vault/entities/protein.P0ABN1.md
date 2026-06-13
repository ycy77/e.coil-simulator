---
entity_id: "protein.P0ABN1"
entity_type: "protein"
name: "dgkA"
source_database: "UniProt"
source_id: "P0ABN1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:217867, ECO:0000269|PubMed:2984194, ECO:0000269|PubMed:8071224}; Multi-pass membrane protein {ECO:0000255, ECO:0000269|PubMed:8071224}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dgkA dgk b4042 JW4002"
---

# dgkA

`protein.P0ABN1`

## Static

- Type: `protein`
- Source: `UniProt:P0ABN1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:217867, ECO:0000269|PubMed:2984194, ECO:0000269|PubMed:8071224}; Multi-pass membrane protein {ECO:0000255, ECO:0000269|PubMed:8071224}.

## Enriched Summary

FUNCTION: Catalyzes the ATP-dependent phosphorylation of sn-l,2-diacylglycerol (DAG) to phosphatidic acid (PubMed:218816, PubMed:2828054, PubMed:2984194, PubMed:3009449, PubMed:6277376, PubMed:6303781, PubMed:9305868). Involved in the recycling of diacylglycerol produced as a by-product during membrane-derived oligosaccharide (MDO) biosynthesis (PubMed:217867, PubMed:6305970). In vitro, phosphorylates various substrates, including sn-1,2-dioleoylglycerol, sn-1,2-dioctanoylglycerol, sn-1,2-dipalmitoylglycerol, sn-1,2-dipalmitate and ceramide (PubMed:218816, PubMed:2828054, PubMed:2984194, PubMed:3009449, PubMed:3021764). Catalyzes direct phosphoryl transfer from Mg-ATP to diacylglycerol and does not form an enzyme-phosphate intermediate (PubMed:9305868). {ECO:0000269|PubMed:217867, ECO:0000269|PubMed:218816, ECO:0000269|PubMed:2828054, ECO:0000269|PubMed:2984194, ECO:0000269|PubMed:3009449, ECO:0000269|PubMed:3021764, ECO:0000269|PubMed:6277376, ECO:0000269|PubMed:6303781, ECO:0000269|PubMed:6305970, ECO:0000269|PubMed:9305868}.

## Biological Role

Component of diacylglycerol kinase (complex.ecocyc.DIACYLGLYKIN-CPLX).

## Enriched Pathways

- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Catalyzes the ATP-dependent phosphorylation of sn-l,2-diacylglycerol (DAG) to phosphatidic acid (PubMed:218816, PubMed:2828054, PubMed:2984194, PubMed:3009449, PubMed:6277376, PubMed:6303781, PubMed:9305868). Involved in the recycling of diacylglycerol produced as a by-product during membrane-derived oligosaccharide (MDO) biosynthesis (PubMed:217867, PubMed:6305970). In vitro, phosphorylates various substrates, including sn-1,2-dioleoylglycerol, sn-1,2-dioctanoylglycerol, sn-1,2-dipalmitoylglycerol, sn-1,2-dipalmitate and ceramide (PubMed:218816, PubMed:2828054, PubMed:2984194, PubMed:3009449, PubMed:3021764). Catalyzes direct phosphoryl transfer from Mg-ATP to diacylglycerol and does not form an enzyme-phosphate intermediate (PubMed:9305868). {ECO:0000269|PubMed:217867, ECO:0000269|PubMed:218816, ECO:0000269|PubMed:2828054, ECO:0000269|PubMed:2984194, ECO:0000269|PubMed:3009449, ECO:0000269|PubMed:3021764, ECO:0000269|PubMed:6277376, ECO:0000269|PubMed:6303781, ECO:0000269|PubMed:6305970, ECO:0000269|PubMed:9305868}.

## Pathways

- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.DIACYLGLYKIN-CPLX|complex.ecocyc.DIACYLGLYKIN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b4042|gene.b4042]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABN1`
- `KEGG:ecj:JW4002;eco:b4042;ecoc:C3026_21845;`
- `GeneID:93777789;948543;`
- `GO:GO:0001727; GO:0004143; GO:0005524; GO:0005886; GO:0006654; GO:0009411; GO:0016020; GO:0042802; GO:0046872`
- `EC:2.7.1.107`

## Notes

Diacylglycerol kinase (DAGK) (EC 2.7.1.107) (Diglyceride kinase) (DGK)
