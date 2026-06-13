---
entity_id: "protein.P15254"
entity_type: "protein"
name: "purL"
source_database: "UniProt"
source_id: "P15254"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00419, ECO:0000269|PubMed:2659070}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "purL purI b2557 JW2541"
---

# purL

`protein.P15254`

## Static

- Type: `protein`
- Source: `UniProt:P15254`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00419, ECO:0000269|PubMed:2659070}.

## Enriched Summary

FUNCTION: Phosphoribosylformylglycinamidine synthase involved in the purines biosynthetic pathway. Catalyzes the ATP-dependent conversion of formylglycinamide ribonucleotide (FGAR) and glutamine to yield formylglycinamidine ribonucleotide (FGAM) and glutamate. {ECO:0000255|HAMAP-Rule:MF_00419, ECO:0000269|PubMed:2659070}. PurL catalyzes the fourth step in the E. coli purine de novo biosynthesis pathway. It converts 5'-phosphoribosyl-N-formylglycineamide (FGAR) to 5-phosphoribosyl-N-formylglycineamidine (FGAM) in the presence of glutamine and ATP. It is the second glutamine amidotransferase in the pathway, the other being PurF. PurL is a large, 141 kDa polypeptide that was shown by genetic complementation tests to contain three different domains. The N-terminal Domain I contains a potential ATP binding motif, the C-terminal Domain III is similar to several glutamine amidotransferases, and Domain II contains elements observed in the triosephosphate isomerase family. Thus, PurL may have arisen from the fusion of at least three different gene families . The enzyme mechanism was studied using initial velocity, dead-end inhibition, and substrate/product exchange studies. A sequential mechanism was suggested in which glutamine binds first, followed by rapid equilibrium binding of MgATP, followed by binding of FGAR...

## Biological Role

Catalyzes FGAMSYN-RXN (reaction.ecocyc.FGAMSYN-RXN). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Phosphoribosylformylglycinamidine synthase involved in the purines biosynthetic pathway. Catalyzes the ATP-dependent conversion of formylglycinamide ribonucleotide (FGAR) and glutamine to yield formylglycinamidine ribonucleotide (FGAM) and glutamate. {ECO:0000255|HAMAP-Rule:MF_00419, ECO:0000269|PubMed:2659070}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.FGAMSYN-RXN|reaction.ecocyc.FGAMSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2557|gene.b2557]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P15254`
- `KEGG:ecj:JW2541;eco:b2557;ecoc:C3026_14155;`
- `GeneID:947032;`
- `GO:GO:0004642; GO:0005524; GO:0005737; GO:0005829; GO:0006164; GO:0006189; GO:0006541; GO:0016887; GO:0046872`
- `EC:6.3.5.3`

## Notes

Phosphoribosylformylglycinamidine synthase (FGAM synthase) (FGAMS) (EC 6.3.5.3) (Formylglycinamide ribonucleotide amidotransferase) (FGAR amidotransferase) (FGAR-AT)
