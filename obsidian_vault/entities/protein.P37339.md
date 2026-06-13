---
entity_id: "protein.P37339"
entity_type: "protein"
name: "lhgD"
source_database: "UniProt"
source_id: "P37339"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:30498244}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lhgD lhgO ygaF b2660 JW2635"
---

# lhgD

`protein.P37339`

## Static

- Type: `protein`
- Source: `UniProt:P37339`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:30498244}.

## Enriched Summary

FUNCTION: Catalyzes the dehydrogenation of L-2-hydroxyglutarate (L2HG) to alpha-ketoglutarate and couples to the respiratory chain by feeding electrons from the reaction into the membrane quinone pool. Functions in a L-lysine degradation pathway that proceeds via cadaverine, glutarate and L-2-hydroxyglutarate. {ECO:0000269|PubMed:30498244}. L-2-hydroxyglutarate dehydrogenase (LhgD) is an electron transport chain-coupled dehydrogenase that feeds electrons from the reaction into the membrane quinone pool . LhgD contains an FAD cofactor which is not covalently attached, and whose reduction potential is relatively high at -25 mV . LhgD was initially thought to be an oxidase, i.e. using molecular oxygen for oxidation of L-2-hydroxyglutarate and producing hydrogen peroxide . LhgD is associated with the cytoplasmic membrane , and its activity is only found in the membrane fraction . lhgD is part of an operon whose expression is induced upon carbon starvation and in stationary phase . Review: LhgO: "L-2-hydroxyglutarate oxidase" LhgD: "L-2-hydroxyglutarate dehydrogenase

## Biological Role

Catalyzes RXN0-7319 (reaction.ecocyc.RXN0-7319). Bound by FAD (molecule.C00016).

## Enriched Pathways

- `eco00310` Lysine degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the dehydrogenation of L-2-hydroxyglutarate (L2HG) to alpha-ketoglutarate and couples to the respiratory chain by feeding electrons from the reaction into the membrane quinone pool. Functions in a L-lysine degradation pathway that proceeds via cadaverine, glutarate and L-2-hydroxyglutarate. {ECO:0000269|PubMed:30498244}.

## Pathways

- `eco00310` Lysine degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-7319|reaction.ecocyc.RXN0-7319]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2660|gene.b2660]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37339`
- `KEGG:ecj:JW2635;eco:b2660;ecoc:C3026_14665;`
- `GeneID:948069;`
- `GO:GO:0005737; GO:0005886; GO:0006554; GO:0019477; GO:0047545; GO:0050660; GO:0140696`
- `EC:1.1.5.13`

## Notes

L-2-hydroxyglutarate dehydrogenase (L2HG dehydrogenase) (EC 1.1.5.13) (L2HG:quinone oxidoreductase)
