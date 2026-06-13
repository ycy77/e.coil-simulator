---
entity_id: "protein.P00864"
entity_type: "protein"
name: "ppc"
source_database: "UniProt"
source_id: "P00864"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ppc glu b3956 JW3928"
---

# ppc

`protein.P00864`

## Static

- Type: `protein`
- Source: `UniProt:P00864`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Forms oxaloacetate, a four-carbon dicarboxylic acid source for the tricarboxylic acid cycle. Phosphoenolpyruvate carboxylase (Ppc) is an anaplerotic enzyme that replenishes oxaloacetate in the tricarboxylic acid cycle. The carboxylation of phosphoenolpyruvate (PEP) to form oxaloacetate and Pi proceeds in two steps: formation of carboxyphosphate and the enolate form of pyruvate, followed by carboxylation of the enolate and release of phosphate and oxaloacetate. Ppc activity is allosterically regulated by many kinds of effectors that interact with several distinct binding sites. The in vivo concentrations of the various regulators differ depending on the growth conditions, resulting in different levels of enzyme activity . The primary activator was thought to be acetyl-CoA; fructose-1,6-bisphosphate (FBP) and GTP can act synergistically with acetyl-CoA . A mechanism for synergistic activaton of the enzyme by different effectors was proposed . In a proteome-wide screen, Ppc was found to bind citrate, ATP, and FBP. Citrate inhibits Ppc activity in vitro; the presence of FBP or acetyl-CoA had no effect on the inhibition...

## Biological Role

Catalyzes phosphate:oxaloacetate carboxy-lyase (adding phosphate;phosphoenolpyruvate-forming) (reaction.R00345). Component of phosphoenolpyruvate carboxylase (complex.ecocyc.PEPCARBOX-CPLX).

## Enriched Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

FUNCTION: Forms oxaloacetate, a four-carbon dicarboxylic acid source for the tricarboxylic acid cycle.

## Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00345|reaction.R00345]] `KEGG` `database` - via EC:4.1.1.31
- `is_component_of` --> [[complex.ecocyc.PEPCARBOX-CPLX|complex.ecocyc.PEPCARBOX-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b3956|gene.b3956]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00864`
- `KEGG:ecj:JW3928;eco:b3956;ecoc:C3026_21375;`
- `GeneID:948457;`
- `GO:GO:0000287; GO:0005829; GO:0006094; GO:0006099; GO:0006107; GO:0008964; GO:0015977; GO:0042802; GO:0051289`
- `EC:4.1.1.31`

## Notes

Phosphoenolpyruvate carboxylase (PEPC) (PEPCase) (EC 4.1.1.31)
