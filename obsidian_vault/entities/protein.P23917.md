---
entity_id: "protein.P23917"
entity_type: "protein"
name: "mak"
source_database: "UniProt"
source_id: "P23917"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mak yajF b0394 JW0385"
---

# mak

`protein.P23917`

## Static

- Type: `protein`
- Source: `UniProt:P23917`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the phosphorylation of fructose to fructose-6-P. Also has low level glucokinase activity in vitro. Is not able to phosphorylate D-ribose, D-mannitol, D-sorbitol, inositol, and L-threonine. {ECO:0000269|PubMed:11742072, ECO:0000269|PubMed:15157072}. In the absence of the usual PTS-mediated route of fructose uptake, a selected mutation that causes increased expression of Mak enables phosphorylation of fructose after its facilitated diffusion into the cell via a selected mutant allele of PTSG-MONOMER PtsG . The Mak enzyme appears to be identical to the previously reported mannokinase activity in E. coli. The enzyme was reported to be constitutively expressed and is able to phosphorylate mannose, fructose and to a lesser extent glucosamine, D-glucose and 2-deoxyglucose . Trace Mak activity is present in wild-type cells . Overexpression of mak rescues the glucose auxotrophy of a glucokinase mutant, and the Mak protein functions as a rudimentary glucokinase in vitro . When a glucokinase-deficient strain is placed under selective pressure for growth on glucose, a spontaneous point mutation appears to regenerate a σ70 consensus sequence in the predicted promoter region, leading to a 94-fold increase in the expression...

## Biological Role

Catalyzes ATP:D-fructose 6-phosphotransferase (reaction.R00760), FRUCTOKINASE-RXN (reaction.ecocyc.FRUCTOKINASE-RXN), MANNKIN-RXN (reaction.ecocyc.MANNKIN-RXN). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

FUNCTION: Catalyzes the phosphorylation of fructose to fructose-6-P. Also has low level glucokinase activity in vitro. Is not able to phosphorylate D-ribose, D-mannitol, D-sorbitol, inositol, and L-threonine. {ECO:0000269|PubMed:11742072, ECO:0000269|PubMed:15157072}.

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00760|reaction.R00760]] `KEGG` `database` - via EC:2.7.1.4
- `catalyzes` --> [[reaction.ecocyc.FRUCTOKINASE-RXN|reaction.ecocyc.FRUCTOKINASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.MANNKIN-RXN|reaction.ecocyc.MANNKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0394|gene.b0394]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P23917`
- `KEGG:ecj:JW0385;eco:b0394;ecoc:C3026_01920;`
- `GeneID:949086;`
- `GO:GO:0004396; GO:0005524; GO:0005829; GO:0008865; GO:0019158`
- `EC:2.7.1.4`

## Notes

Fructokinase (EC 2.7.1.4) (D-fructose kinase) (Manno(fructo)kinase)
