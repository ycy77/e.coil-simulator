---
entity_id: "protein.P27848"
entity_type: "protein"
name: "yigL"
source_database: "UniProt"
source_id: "P27848"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yigL b3826 JW5854"
---

# yigL

`protein.P27848`

## Static

- Type: `protein`
- Source: `UniProt:P27848`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Phosphosugar phosphatase that plays a crucial role in the sugar-phosphate stress response (PubMed:23582330, PubMed:23873911). Catalyzes the hydrolysis of phosphosugars, which are toxic and can inhibit growth at high concentrations, thus promoting their efflux (Probable). In addition, it exhibits strong activity against pyridoxine phosphate (PNP) and pyridoxal phosphate (PLP) (PubMed:39133002). It plays an important role in maintaining PNP and PLP homeostasis (PubMed:39133002). It may play a role when cells face high intracellular PNP levels (PubMed:39133002). Control of PNP levels is crucial because PNP has the potential to inhibit PLP-dependent enzymes and proteins (PubMed:39133002). YigL helps alleviate PNP toxicity by reducing intracellular PNP concentrations, and contributes significantly, in combination with YbhA, to PLP dephosphorylation (PubMed:39133002). It is therefore a primary enzyme in the regulation of vitamin B(6) metabolism (PubMed:39133002). Shows a broad substrate specificity in vitro, as it can hydrolyze a wide range of phosphorylated metabolites, including PLP, PNP, phosphosugars such as 2-deoxyglucose 6-phosphate (2bGLU6P) and beta-glucose 6-phosphate (bGlu6P), cytidine monophosphate (CMP), guanosine monophosphate (GMP), deoxyinosine monophosphate (dIMP) and acetyl-phosphate (PubMed:16990279, PubMed:39133002)...

## Biological Role

Catalyzes pyridoxal-5'-phosphate phosphohydrolase (reaction.R00173), sugar-phosphate phosphohydrolase (reaction.R00804), pyridoxine-5'-phosphate phosphohydrolase (reaction.R01911), 3.1.3.74-RXN (reaction.ecocyc.3.1.3.74-RXN), SUGAR-PHOSPHATASE-RXN (reaction.ecocyc.SUGAR-PHOSPHATASE-RXN). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00750` Vitamin B6 metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Phosphosugar phosphatase that plays a crucial role in the sugar-phosphate stress response (PubMed:23582330, PubMed:23873911). Catalyzes the hydrolysis of phosphosugars, which are toxic and can inhibit growth at high concentrations, thus promoting their efflux (Probable). In addition, it exhibits strong activity against pyridoxine phosphate (PNP) and pyridoxal phosphate (PLP) (PubMed:39133002). It plays an important role in maintaining PNP and PLP homeostasis (PubMed:39133002). It may play a role when cells face high intracellular PNP levels (PubMed:39133002). Control of PNP levels is crucial because PNP has the potential to inhibit PLP-dependent enzymes and proteins (PubMed:39133002). YigL helps alleviate PNP toxicity by reducing intracellular PNP concentrations, and contributes significantly, in combination with YbhA, to PLP dephosphorylation (PubMed:39133002). It is therefore a primary enzyme in the regulation of vitamin B(6) metabolism (PubMed:39133002). Shows a broad substrate specificity in vitro, as it can hydrolyze a wide range of phosphorylated metabolites, including PLP, PNP, phosphosugars such as 2-deoxyglucose 6-phosphate (2bGLU6P) and beta-glucose 6-phosphate (bGlu6P), cytidine monophosphate (CMP), guanosine monophosphate (GMP), deoxyinosine monophosphate (dIMP) and acetyl-phosphate (PubMed:16990279, PubMed:39133002). The catalytic efficiency toward PNP is comparable to that for the phosphosugars glucose 6-phosphate and 2-deoxyglucose 6-phosphate (PubMed:39133002). {ECO:0000269|PubMed:16990279, ECO:0000269|PubMed:23582330, ECO:0000269|PubMed:23873911, ECO:0000269|PubMed:39133002, ECO:0000305|PubMed:23873911}.

## Pathways

- `eco00750` Vitamin B6 metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.R00173|reaction.R00173]] `KEGG` `database` - via EC:3.1.3.74
- `catalyzes` --> [[reaction.R00804|reaction.R00804]] `KEGG` `database` - via EC:3.1.3.23
- `catalyzes` --> [[reaction.R01911|reaction.R01911]] `KEGG` `database` - via EC:3.1.3.74
- `catalyzes` --> [[reaction.ecocyc.3.1.3.74-RXN|reaction.ecocyc.3.1.3.74-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.SUGAR-PHOSPHATASE-RXN|reaction.ecocyc.SUGAR-PHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3826|gene.b3826]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P27848`
- `KEGG:ecj:JW5854;eco:b3826;ecoc:C3026_20705;`
- `GeneID:2847768;`
- `GO:GO:0000287; GO:0005829; GO:0006950; GO:0016791; GO:0033883; GO:0046872; GO:0050308`
- `EC:3.1.3.23; 3.1.3.74`

## Notes

Phosphosugar phosphatase YigL (EC 3.1.3.23) (Pyridoxal phosphate/pyridoxine phosphate phosphatase YigL) (PLP/PNP phosphatase YigL) (EC 3.1.3.74)
