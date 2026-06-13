---
entity_id: "protein.P33940"
entity_type: "protein"
name: "mqo"
source_database: "UniProt"
source_id: "P33940"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mqo yojH b2210 JW2198"
---

# mqo

`protein.P33940`

## Static

- Type: `protein`
- Source: `UniProt:P33940`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Malate:quinone oxidoreductase (EC 1.1.5.4) (MQO) (Malate dehydrogenase [quinone]) The mqo-encoded malate:quinone oxidoreductase (Mqo) is likely identical to the "malate oxidase" studied earlier . The membrane-associated enzyme catalyzes the oxidation of malate to oxaloacetate. Electrons are likely donated to the electron transfer chain at the quinone level. Contrary to earlier reports, Mqo and MALATE-DEHASE are active at the same time in the cell, although Mqo does not seem to play a significant physiological role in malate oxidation . Mqo activity is highest during exponential growth, decreases after the onset of stationary phase and is regulated by the carbon source . The ArcA-ArcB two-component system regulates mqo expression at the transcriptional level . An mqo deletion strain does not have an obvious growth defect, but mqo can partially substitute for the function of MALATE-DEHASE Mdh in an mdh mutant . Mqo: "malate:quinone oxidoreductase"

## Biological Role

Catalyzes (S)-malate:oxygen oxidoreductase (reaction.R00360), (S)-malate:quinone oxidoreductase (reaction.R00361), MALATE-DEHYDROGENASE-ACCEPTOR-RXN (reaction.ecocyc.MALATE-DEHYDROGENASE-ACCEPTOR-RXN). Bound by FAD (molecule.C00016).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

Malate:quinone oxidoreductase (EC 1.1.5.4) (MQO) (Malate dehydrogenase [quinone])

## Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00360|reaction.R00360]] `KEGG` `database` - via EC:1.1.5.4
- `catalyzes` --> [[reaction.R00361|reaction.R00361]] `KEGG` `database` - via EC:1.1.5.4
- `catalyzes` --> [[reaction.ecocyc.MALATE-DEHYDROGENASE-ACCEPTOR-RXN|reaction.ecocyc.MALATE-DEHYDROGENASE-ACCEPTOR-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2210|gene.b2210]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33940`
- `KEGG:ecj:JW2198;eco:b2210;ecoc:C3026_12350;`
- `GeneID:946702;`
- `GO:GO:0005737; GO:0005829; GO:0006099; GO:0008924; GO:0009898; GO:0050660`
- `EC:1.1.5.4`

## Notes

Malate:quinone oxidoreductase (EC 1.1.5.4) (MQO) (Malate dehydrogenase [quinone])
