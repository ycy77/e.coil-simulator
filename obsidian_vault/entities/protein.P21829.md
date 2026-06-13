---
entity_id: "protein.P21829"
entity_type: "protein"
name: "ybhA"
source_database: "UniProt"
source_id: "P21829"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ybhA b0766 JW0749"
---

# ybhA

`protein.P21829`

## Static

- Type: `protein`
- Source: `UniProt:P21829`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the dephosphorylation of pyridoxal-phosphate (PLP) (PubMed:15808744, PubMed:16990279, PubMed:39133002). Shows a broad substrate specificity in vitro, as it can hydrolyze a wide range of phosphorylated metabolites, including PLP, erythrose-4-phosphate (Ery4P), fructose-1,6-bis-phosphate (Fru1,6bisP), FMN, acetyl-phosphate, carbamoyl-phosphate, imido-di-phosphate and the artificial chromogenic susbtrate, p-nitrophenyl phosphate (pNPP) (PubMed:15808744, PubMed:16990279). Shows also weak activity with pyridoxine phosphate (PNP), but it plays only a minor role in PNP homeostasis (PubMed:39133002). {ECO:0000269|PubMed:15808744, ECO:0000269|PubMed:16990279, ECO:0000269|PubMed:39133002}. YbhA is a pyridoxal phosphate phosphatase that contributes to PLP homeostasis within the cell. Addition of pyridoxal to a wild-type strain grown in minimal medium leads to an extended lag phase, and cells accumulate PLP. Overexpression of YbhA alleviates this phenotype. Conversely, overexpression of YbhA in cells grown in minimal medium leads to a reduced growth rate and decreased levels of intracellular PLP; the growth defect can be rescued by addition of pyridoxal to the growth medium . The phosphatase activity of YbhA was first discovered in a high-throughput screen of purified proteins...

## Biological Role

Catalyzes pyridoxal-5'-phosphate phosphohydrolase (reaction.R00173), pyridoxine-5'-phosphate phosphohydrolase (reaction.R01911), 3.1.3.74-RXN (reaction.ecocyc.3.1.3.74-RXN), F16BDEPHOS-RXN (reaction.ecocyc.F16BDEPHOS-RXN). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00750` Vitamin B6 metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the dephosphorylation of pyridoxal-phosphate (PLP) (PubMed:15808744, PubMed:16990279, PubMed:39133002). Shows a broad substrate specificity in vitro, as it can hydrolyze a wide range of phosphorylated metabolites, including PLP, erythrose-4-phosphate (Ery4P), fructose-1,6-bis-phosphate (Fru1,6bisP), FMN, acetyl-phosphate, carbamoyl-phosphate, imido-di-phosphate and the artificial chromogenic susbtrate, p-nitrophenyl phosphate (pNPP) (PubMed:15808744, PubMed:16990279). Shows also weak activity with pyridoxine phosphate (PNP), but it plays only a minor role in PNP homeostasis (PubMed:39133002). {ECO:0000269|PubMed:15808744, ECO:0000269|PubMed:16990279, ECO:0000269|PubMed:39133002}.

## Pathways

- `eco00750` Vitamin B6 metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.R00173|reaction.R00173]] `KEGG` `database` - via EC:3.1.3.74
- `catalyzes` --> [[reaction.R01911|reaction.R01911]] `KEGG` `database` - via EC:3.1.3.74
- `catalyzes` --> [[reaction.ecocyc.3.1.3.74-RXN|reaction.ecocyc.3.1.3.74-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.F16BDEPHOS-RXN|reaction.ecocyc.F16BDEPHOS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0766|gene.b0766]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P21829`
- `KEGG:ecj:JW0749;eco:b0766;ecoc:C3026_03885;`
- `GeneID:945372;`
- `GO:GO:0000287; GO:0005829; GO:0016773; GO:0016791; GO:0032361; GO:0033883; GO:0050308`
- `EC:3.1.3.74`

## Notes

Pyridoxal phosphate phosphatase YbhA (PLP phosphatase) (EC 3.1.3.74)
