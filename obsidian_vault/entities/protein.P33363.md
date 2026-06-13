---
entity_id: "protein.P33363"
entity_type: "protein"
name: "bglX"
source_database: "UniProt"
source_id: "P33363"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "bglX yohA b2132 JW2120"
---

# bglX

`protein.P33363`

## Static

- Type: `protein`
- Source: `UniProt:P33363`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm.

## Enriched Summary

Periplasmic beta-glucosidase (EC 3.2.1.21) (Beta-D-glucoside glucohydrolase) (Cellobiase) (Gentiobiase) bglX is predicted to encode a periplasmic β-glucosidase/β-galactosidase; the purified enzyme can hydrolyse artifical substrates (o-nitrophenyl-β-D-glucopyranoside, p-nitrophenyl-β-D-glucopyranoside, and o-nitrophenyl-β-D-galactopyranoside) with varying kinetics; it can also hydrolyse lactose (but not cellobiose, maltose or laminarin) . No obvious phenotype is associated with deletion or overexpression , and the physiological function of the enzyme remains uncertain. In the CAZy database, BglX is a Glycoside Hydrolase Family 3 (GH3) enzyme .

## Biological Role

Catalyzes cellobiose glucohydrolase (reaction.R00026), cellobiose glucohydrolase (reaction.R00306), 1,4-beta-D-glucan glucohydrolase (reaction.R02887), daidzein 7-O-glucoside glucohydrolase (reaction.R13051), genistein 7-O-beta-D-glucoside glucohydrolase (reaction.R13052), quercetin 3-O-glucoside glucohydrolase (reaction.R13065), naringenin 7-O-beta-D-glucoside glucohydrolase (reaction.R13081), BETAGALACTOSID-RXN (reaction.ecocyc.BETAGALACTOSID-RXN), and 3 more.

## Enriched Pathways

- `eco00460` Cyanoamino acid metabolism (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00946` Degradation of flavonoids (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

Periplasmic beta-glucosidase (EC 3.2.1.21) (Beta-D-glucoside glucohydrolase) (Cellobiase) (Gentiobiase)

## Pathways

- `eco00460` Cyanoamino acid metabolism (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00946` Degradation of flavonoids (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (11)

- `catalyzes` --> [[reaction.R00026|reaction.R00026]] `KEGG` `database` - via EC:3.2.1.21
- `catalyzes` --> [[reaction.R00306|reaction.R00306]] `KEGG` `database` - via EC:3.2.1.21
- `catalyzes` --> [[reaction.R02887|reaction.R02887]] `KEGG` `database` - via EC:3.2.1.21
- `catalyzes` --> [[reaction.R13051|reaction.R13051]] `KEGG` `database` - via EC:3.2.1.21
- `catalyzes` --> [[reaction.R13052|reaction.R13052]] `KEGG` `database` - via EC:3.2.1.21
- `catalyzes` --> [[reaction.R13065|reaction.R13065]] `KEGG` `database` - via EC:3.2.1.21
- `catalyzes` --> [[reaction.R13081|reaction.R13081]] `KEGG` `database` - via EC:3.2.1.21
- `catalyzes` --> [[reaction.ecocyc.BETAGALACTOSID-RXN|reaction.ecocyc.BETAGALACTOSID-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-14722|reaction.ecocyc.RXN-14722]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-24169|reaction.ecocyc.RXN-24169]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-24170|reaction.ecocyc.RXN-24170]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2132|gene.b2132]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33363`
- `KEGG:ecj:JW2120;eco:b2132;ecoc:C3026_11955;`
- `GeneID:946682;`
- `GO:GO:0008422; GO:0009251; GO:0015926; GO:0030288; GO:0042597`
- `EC:3.2.1.21`

## Notes

Periplasmic beta-glucosidase (EC 3.2.1.21) (Beta-D-glucoside glucohydrolase) (Cellobiase) (Gentiobiase)
