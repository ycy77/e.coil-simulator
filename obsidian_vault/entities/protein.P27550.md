---
entity_id: "protein.P27550"
entity_type: "protein"
name: "acs"
source_database: "UniProt"
source_id: "P27550"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "acs yfaC b4069 JW4030"
---

# acs

`protein.P27550`

## Static

- Type: `protein`
- Source: `UniProt:P27550`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the conversion of acetate into acetyl-CoA (AcCoA), an essential intermediate at the junction of anabolic and catabolic pathways. Acs undergoes a two-step reaction. In the first half reaction, Acs combines acetate with ATP to form acetyl-adenylate (AcAMP) intermediate. In the second half reaction, it can then transfer the acetyl group from AcAMP to the sulfhydryl group of CoA, forming the product AcCoA.; FUNCTION: Enables the cell to use acetate during aerobic growth to generate energy via the TCA cycle, and biosynthetic compounds via the glyoxylate shunt. Acetylates CheY, the response regulator involved in flagellar movement and chemotaxis. Acetyl-CoA synthetase (Acs) activates acetate to acetyl-CoA in an ATP-dependent manner . Acs activity constitutes one of two distinct pathways by which E. coli activates acetate to acetyl-CoA. The Acs pathway (PWY0-1313) functions in a mainly anabolic role, scavenging acetate present in the extracellular medium. Induction of acs expression functions as the metabolic switch activating this pathway . Genetic interactions suggest that Acs is acetylated and thereby inactivated through the action of G7350-MONOMER, and that G6577-MONOMER CobB catalyzes deacetylation of Acs . Acetylation of Acs by G7350-MONOMER has been shown in vitro . Acetylation of Acs can occur non-enzymatically by acetyl-phosphate...

## Biological Role

Catalyzes acetate:CoA ligase (AMP-forming) (reaction.R00235), acetyl adenylate:CoA acetyltransferase (reaction.R00236), ATP:acetate adenylyltransferase (reaction.R00316), ACETATE--COA-LIGASE-RXN (reaction.ecocyc.ACETATE--COA-LIGASE-RXN), PROPIONATE--COA-LIGASE-RXN (reaction.ecocyc.PROPIONATE--COA-LIGASE-RXN). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the conversion of acetate into acetyl-CoA (AcCoA), an essential intermediate at the junction of anabolic and catabolic pathways. Acs undergoes a two-step reaction. In the first half reaction, Acs combines acetate with ATP to form acetyl-adenylate (AcAMP) intermediate. In the second half reaction, it can then transfer the acetyl group from AcAMP to the sulfhydryl group of CoA, forming the product AcCoA.; FUNCTION: Enables the cell to use acetate during aerobic growth to generate energy via the TCA cycle, and biosynthetic compounds via the glyoxylate shunt. Acetylates CheY, the response regulator involved in flagellar movement and chemotaxis.

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.R00235|reaction.R00235]] `KEGG` `database` - via EC:6.2.1.1
- `catalyzes` --> [[reaction.R00236|reaction.R00236]] `KEGG` `database` - via EC:6.2.1.1
- `catalyzes` --> [[reaction.R00316|reaction.R00316]] `KEGG` `database` - via EC:6.2.1.1
- `catalyzes` --> [[reaction.ecocyc.ACETATE--COA-LIGASE-RXN|reaction.ecocyc.ACETATE--COA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.PROPIONATE--COA-LIGASE-RXN|reaction.ecocyc.PROPIONATE--COA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b4069|gene.b4069]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P27550`
- `KEGG:ecj:JW4030;eco:b4069;`
- `GeneID:75204212;948572;`
- `GO:GO:0003987; GO:0005524; GO:0005829; GO:0006085; GO:0006935; GO:0016208; GO:0018394; GO:0019427; GO:0033558; GO:0034421; GO:0045733; GO:0046872; GO:0050218`
- `EC:6.2.1.1`

## Notes

Acetyl-coenzyme A synthetase (AcCoA synthetase) (Acs) (EC 6.2.1.1) (Acetate--CoA ligase) (Acyl-activating enzyme)
