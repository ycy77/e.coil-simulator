---
entity_id: "protein.P07024"
entity_type: "protein"
name: "ushA"
source_database: "UniProt"
source_id: "P07024"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm. Note=Exported from the cell, except a small proportion that is internally localized."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ushA b0480 JW0469"
---

# ushA

`protein.P07024`

## Static

- Type: `protein`
- Source: `UniProt:P07024`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm. Note=Exported from the cell, except a small proportion that is internally localized.

## Enriched Summary

FUNCTION: Degradation of external UDP-glucose to uridine monophosphate and glucose-1-phosphate, which can then be used by the cell. The ushA gene of E. coli encodes a bifunctional enzyme with 5'-nucleotidase and UDP-sugar hydrolase activities. It has relatively broad substrate specificity, hydrolyzing 5'-ribonucleotides and 5'-deoxyribonucleotides , bis(5'-nucleosidyl)polyphosphates , UDP sugars , and CDP-alcohols . It also hydrolyzes the synthetic substrates bis(p-nitrophenyl)phosphate and p-nitrophenyl phosphate . UshA localizes to the periplasm where it is able to catalyze the degradation of external UDP-glucose to uridine, glucose-1-phosphate and inorganic phosphate which are then utilized by the cell. The nucleoside diphosphate sugar hydrolase activity is specific for UDP sugars . The periplasmic location suggests a general role for this enzyme in utilization of extracellular nucleotides . UshA is also involved in the degradation of internally formed nucleotides during degradation of cellular RNA . ushA knockout mutants lack major 5'-nucleotidase activity. An ushA aphA double knockout mutant is unable to utilize purine nucleotides as the sole carbon source . In addition to its 5'-nucleotidase activity, UDP-sugar hydrolase activity, and dinucleoside polyphosphate hydrolase activity, UshA has a novel, highly efficient CDP-alcohol hydrolase activity. The E...

## Biological Role

Catalyzes adenosine 5'-monophosphate phosphohydrolase (reaction.R00183), UDP-glucose glucophosphohydrolase (reaction.R00287), cytidine-5'-monophosphate phosphohydrolase (reaction.R00511), 4-NITROPHENYLPHOSPHATASE-RXN (reaction.ecocyc.4-NITROPHENYLPHOSPHATASE-RXN), 5-NUCLEOTID-RXN (reaction.ecocyc.5-NUCLEOTID-RXN), BIS5-ADENOSYL-TRIPHOSPHATASE-RXN (reaction.ecocyc.BIS5-ADENOSYL-TRIPHOSPHATASE-RXN), RXN-18241 (reaction.ecocyc.RXN-18241), RXN0-3741 (reaction.ecocyc.RXN0-3741), and 1 more. Bound by Zinc cation (molecule.C00038).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: Degradation of external UDP-glucose to uridine monophosphate and glucose-1-phosphate, which can then be used by the cell.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (9)

- `catalyzes` --> [[reaction.R00183|reaction.R00183]] `KEGG` `database` - via EC:3.1.3.5
- `catalyzes` --> [[reaction.R00287|reaction.R00287]] `KEGG` `database` - via EC:3.6.1.45
- `catalyzes` --> [[reaction.R00511|reaction.R00511]] `KEGG` `database` - via EC:3.1.3.5
- `catalyzes` --> [[reaction.ecocyc.4-NITROPHENYLPHOSPHATASE-RXN|reaction.ecocyc.4-NITROPHENYLPHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.5-NUCLEOTID-RXN|reaction.ecocyc.5-NUCLEOTID-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.BIS5-ADENOSYL-TRIPHOSPHATASE-RXN|reaction.ecocyc.BIS5-ADENOSYL-TRIPHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-18241|reaction.ecocyc.RXN-18241]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-3741|reaction.ecocyc.RXN0-3741]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.UDPSUGARHYDRO-RXN|reaction.ecocyc.UDPSUGARHYDRO-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0480|gene.b0480]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P07024`
- `KEGG:ecj:JW0469;eco:b0480;ecoc:C3026_02360;`
- `GeneID:947331;`
- `GO:GO:0000166; GO:0008253; GO:0008768; GO:0009166; GO:0030288; GO:0046872`
- `EC:3.1.3.5; 3.6.1.45`

## Notes

Protein UshA [Includes: UDP-sugar hydrolase (EC 3.6.1.45) (UDP-sugar diphosphatase) (UDP-sugar pyrophosphatase); 5'-nucleotidase (5'-NT) (EC 3.1.3.5)]
