---
entity_id: "protein.P13009"
entity_type: "protein"
name: "metH"
source_database: "UniProt"
source_id: "P13009"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "metH b4019 JW3979"
---

# metH

`protein.P13009`

## Static

- Type: `protein`
- Source: `UniProt:P13009`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the transfer of a methyl group from methyl-cobalamin to homocysteine, yielding enzyme-bound cob(I)alamin and methionine. Subsequently, remethylates the cofactor using methyltetrahydrofolate. {ECO:0000269|PubMed:8652590, ECO:0000269|PubMed:9201956}. Cobalamin-dependent methionine synthase (MetH) is a large modular protein that catalyzes the transfer of a methyl group from 5-METHYL-THF-GLU-N 5-methyl-tetrahydrofolate to HOMO-CYS to form MET in the final step of the HOMOSER-METSYN-PWY pathway. The reaction can be catalyzed by either of two transmethylases, HOMOCYSMET-MONOMER MetE or MetH. MetH, described here, is dependent on COB-I-ALAMIN (vitamin B12) as a cofactor, whereas MetE is not. MetH can utilize either the mono- or triglutamate forms of folate, while MetE can use only the triglutamate form . MetE and MetH lack sequence similarity, suggesting that these proteins arose by convergent evolution . MetH is composed of four functionally distinct modules that are arranged linearly with single interdomain linkers. The N-terminal module binds homocysteine, while the second module binds methyl-tetrahydrofolate (methylTHF) . The third module binds the cobalamin cofactor ; the C-terminal module binds S-ADENOSYLMETHIONINE (AdoMet) and is necessary for the initial reductive methylation of the cobalamin cofactor...

## Biological Role

Catalyzes HOMOCYSMETB12-RXN (reaction.ecocyc.HOMOCYSMETB12-RXN). Bound by Zinc cation (molecule.C00038), Methylcobalamin (molecule.C06453).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00450` Selenocompound metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)
- `eco04980` Cobalamin transport and metabolism (KEGG)
- `eco04981` Folate transport and metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the transfer of a methyl group from methyl-cobalamin to homocysteine, yielding enzyme-bound cob(I)alamin and methionine. Subsequently, remethylates the cofactor using methyltetrahydrofolate. {ECO:0000269|PubMed:8652590, ECO:0000269|PubMed:9201956}.

## Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00450` Selenocompound metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)
- `eco04980` Cobalamin transport and metabolism (KEGG)
- `eco04981` Folate transport and metabolism (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.HOMOCYSMETB12-RXN|reaction.ecocyc.HOMOCYSMETB12-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C06453|molecule.C06453]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b4019|gene.b4019]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P13009`
- `KEGG:ecj:JW3979;eco:b4019;`
- `GeneID:75204159;948522;`
- `GO:GO:0005737; GO:0005829; GO:0008270; GO:0008705; GO:0009086; GO:0031419; GO:0032259; GO:0035999; GO:0046653; GO:0050667`
- `EC:2.1.1.13`

## Notes

Methionine synthase (EC 2.1.1.13) (5-methyltetrahydrofolate--homocysteine methyltransferase) (Methionine synthase, vitamin-B12-dependent) (MS)
