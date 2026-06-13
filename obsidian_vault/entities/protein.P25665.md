---
entity_id: "protein.P25665"
entity_type: "protein"
name: "metE"
source_database: "UniProt"
source_id: "P25665"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "metE b3829 JW3805"
---

# metE

`protein.P25665`

## Static

- Type: `protein`
- Source: `UniProt:P25665`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the transfer of a methyl group from 5-methyltetrahydrofolate to homocysteine resulting in methionine formation. {ECO:0000255|HAMAP-Rule:MF_00172}. In the absence of exogenously supplied vitamin B12 (cobalamin), E. coli MetE catalyzes the final step of de novo methionine biosynthesis. In the presence of the vitamin B12 cofactor, MetH functions in this reaction and synthesis of MetE is repressed (see pathway HOMOSER-METSYN-PWY). The metE and metH genes lack similarity in their deduced amino acid sequences, suggesting that these proteins arose by convergent evolution . MetE was shown to utilize only the triglutamate form of folate (5-methyltetrahydropteroyltri-L-glutamate) whereas MetH utilized either the monoglutamate (5-methyl-tetrahydrofolate) or the triglutamate forms of folate . Early studies utilized unpurified or partially purified enzyme . The enzyme was later purified from extracts of E. coli K-12 and characterized . The metE gene was cloned and expressed and the expression of MetE was shown to be repressed by methionine and vitamin B12 . Recombinant enzyme has also been purified and characterized . MetE contains zinc which is necessary for its activity. Cys643 and Cys726 have been identified as two of the zinc ligands and a third may be His641 . Evidence suggested that the sulfur of the homocysteine substrate binds directly to the zinc ion...

## Biological Role

Catalyzes 5-methyltetrahydropteroyltri-L-glutamate:L-homocysteine S-methyltransferase (reaction.R04405), HOMOCYSMET-RXN (reaction.ecocyc.HOMOCYSMET-RXN). Bound by Zinc cation (molecule.C00038).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00450` Selenocompound metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the transfer of a methyl group from 5-methyltetrahydrofolate to homocysteine resulting in methionine formation. {ECO:0000255|HAMAP-Rule:MF_00172}.

## Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00450` Selenocompound metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R04405|reaction.R04405]] `KEGG` `database` - via EC:2.1.1.14
- `catalyzes` --> [[reaction.ecocyc.HOMOCYSMET-RXN|reaction.ecocyc.HOMOCYSMET-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3829|gene.b3829]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P25665`
- `KEGG:ecj:JW3805;eco:b3829;ecoc:C3026_20720;`
- `GeneID:948323;`
- `GO:GO:0003871; GO:0005829; GO:0008270; GO:0008705; GO:0009086; GO:0032259; GO:0035999; GO:0050667`
- `EC:2.1.1.14`

## Notes

5-methyltetrahydropteroyltriglutamate--homocysteine methyltransferase (EC 2.1.1.14) (Cobalamin-independent methionine synthase) (Methionine synthase, vitamin-B12 independent isozyme)
