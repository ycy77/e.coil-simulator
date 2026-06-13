---
entity_id: "protein.P0AEW9"
entity_type: "protein"
name: "fruK"
source_database: "UniProt"
source_id: "P0AEW9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fruK fpk b2168 JW2155"
---

# fruK

`protein.P0AEW9`

## Static

- Type: `protein`
- Source: `UniProt:P0AEW9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the ATP-dependent phosphorylation of fructose-l-phosphate to fructose-l,6-bisphosphate (PubMed:10833389, Ref.6). Is specific for fructose-l-phosphate (Ref.6). GTP, UTP and CTP can also function as phosphoryl donors showing 60%, 20% and 10% of the activity of ATP (Ref.6). {ECO:0000269|PubMed:10833389, ECO:0000269|Ref.6}. 1-phosphofructokinase is essential for the utilization of fructose as a carbon source. The enzyme is highly specific for fructose-1-phosphate . FruK has some sequence similarity to the minor form of 6-phosphofructokinase (PfkB), but not the major form (PfkA) . FruK belongs to the ribokinase family of sugar kinases . A fruK mutant is unable to grow on fructose or fructose-1-phosphate as the sole source of carbon . A ΔfruK mutant results in increased lag phase when grown on preferred carbon sources, and increased growth delays on non-preferred carbon sources, such as glycerol . FruK can carry out the reverse reaction to form fructose-1-phosphate (F1P) from physiological concentrations of fructose-1,6-bisphosphate (FBP), thus creating the effector molecule of PD00521. FruK can also form higher-order heterocomplexes with Cra in crude cell extracts and in vitro with purified FruK . Review:

## Biological Role

Component of 1-phosphofructokinase (complex.ecocyc.1-PFK).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

FUNCTION: Catalyzes the ATP-dependent phosphorylation of fructose-l-phosphate to fructose-l,6-bisphosphate (PubMed:10833389, Ref.6). Is specific for fructose-l-phosphate (Ref.6). GTP, UTP and CTP can also function as phosphoryl donors showing 60%, 20% and 10% of the activity of ATP (Ref.6). {ECO:0000269|PubMed:10833389, ECO:0000269|Ref.6}.

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.1-PFK|complex.ecocyc.1-PFK]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2168|gene.b2168]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEW9`
- `KEGG:ecj:JW2155;eco:b2168;ecoc:C3026_12145;`
- `GeneID:75172296;75206421;946676;`
- `GO:GO:0005524; GO:0005829; GO:0006001; GO:0008443; GO:0008662`
- `EC:2.7.1.56`

## Notes

1-phosphofructokinase (EC 2.7.1.56) (Fructose 1-phosphate kinase) (Fru1PK)
