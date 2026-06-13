---
entity_id: "protein.P33221"
entity_type: "protein"
name: "purT"
source_database: "UniProt"
source_id: "P33221"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "purT b1849 JW1838"
---

# purT

`protein.P33221`

## Static

- Type: `protein`
- Source: `UniProt:P33221`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the de novo purine biosynthesis (PubMed:8117714, PubMed:8501063, PubMed:9184151). Catalyzes the transfer of formate to 5-phospho-ribosyl-glycinamide (GAR), producing 5-phospho-ribosyl-N-formylglycinamide (FGAR) (PubMed:8117714, PubMed:8501063, PubMed:9184151). Formate is provided by PurU via hydrolysis of 10-formyl-tetrahydrofolate (PubMed:8226647). PurT is also able to cleave acetyl phosphate and carbamoyl phosphate to produce ATP with acetate and carbamate, respectively (PubMed:8117714, PubMed:9184151). {ECO:0000269|PubMed:8117714, ECO:0000269|PubMed:8226647, ECO:0000269|PubMed:8501063, ECO:0000269|PubMed:9184151}. E. coli contains two different phosphoribosylglycinamide (GAR) transformylases, both of which can catalyze the third step in de novo purine biosynthesis. The transformylase encoded by purN utilizes 10-formyl-tetrahydrofolate as the formyl donor. The second transformylase encoded by purT utilizes formate, which is provided by PurU-catalyzed hydrolysis of 10-formyl-tetrahydrofolate . The existence of these two transformylase enzymes was determined by mutant studies. A strain containing a knockout insertion in purN did not result in purine auxotrophy . Only mutants defective in both purN and purT required exogenously added purine for growth . There is no significant homology between the two transformylases...

## Biological Role

Catalyzes formate:N1-(5-phospho-beta-D-ribosyl)glycinamide ligase (ADP-forming) (reaction.R06974), ACETATEKIN-RXN (reaction.ecocyc.ACETATEKIN-RXN), GARTRANSFORMYL2-RXN (reaction.ecocyc.GARTRANSFORMYL2-RXN). Bound by Cobalt ion (molecule.C00175), Magnesium cation (molecule.C00305), Mn2+ (molecule.ecocyc.MN_2).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Involved in the de novo purine biosynthesis (PubMed:8117714, PubMed:8501063, PubMed:9184151). Catalyzes the transfer of formate to 5-phospho-ribosyl-glycinamide (GAR), producing 5-phospho-ribosyl-N-formylglycinamide (FGAR) (PubMed:8117714, PubMed:8501063, PubMed:9184151). Formate is provided by PurU via hydrolysis of 10-formyl-tetrahydrofolate (PubMed:8226647). PurT is also able to cleave acetyl phosphate and carbamoyl phosphate to produce ATP with acetate and carbamate, respectively (PubMed:8117714, PubMed:9184151). {ECO:0000269|PubMed:8117714, ECO:0000269|PubMed:8226647, ECO:0000269|PubMed:8501063, ECO:0000269|PubMed:9184151}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R06974|reaction.R06974]] `KEGG` `database` - via EC:6.3.1.21
- `catalyzes` --> [[reaction.ecocyc.ACETATEKIN-RXN|reaction.ecocyc.ACETATEKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.GARTRANSFORMYL2-RXN|reaction.ecocyc.GARTRANSFORMYL2-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (4)

- `binds` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b1849|gene.b1849]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33221`
- `KEGG:ecj:JW1838;eco:b1849;ecoc:C3026_10535;`
- `GeneID:93776116;946368;`
- `GO:GO:0000287; GO:0004644; GO:0005524; GO:0005829; GO:0006189; GO:0008776; GO:0043815`
- `EC:6.3.1.21`

## Notes

Formate-dependent phosphoribosylglycinamide formyltransferase (EC 6.3.1.21) (5'-phosphoribosylglycinamide transformylase 2) (Formate-dependent GAR transformylase) (GAR transformylase 2) (GART 2) (GAR transformylase T) (Non-folate glycinamide ribonucleotide transformylase) (Phosphoribosylglycinamide formyltransferase 2)
