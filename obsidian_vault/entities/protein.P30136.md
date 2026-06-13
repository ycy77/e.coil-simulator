---
entity_id: "protein.P30136"
entity_type: "protein"
name: "thiC"
source_database: "UniProt"
source_id: "P30136"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "thiC b3994 JW3958"
---

# thiC

`protein.P30136`

## Static

- Type: `protein`
- Source: `UniProt:P30136`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the synthesis of the hydroxymethylpyrimidine phosphate (HMP-P) moiety of thiamine from aminoimidazole ribotide (AIR) in a radical S-adenosyl-L-methionine (SAM)-dependent reaction. {ECO:0000305|PubMed:15292217, ECO:0000305|PubMed:15326535}. HMP-P synthase (ThiC) catalyzes the conversion of 5-aminoimidazole (AIR) into 4-amino-hydroxymethyl-2-methylpyrimidine phosphate (HMP-P) . ThiC was demonstrated to be a novel member of the radical S-adenosylmethionine (SAM) superfamily, also known as AdoMet superfamily . The role of the radical SAM proteins in the ThiC-catalyzed complex rearrangement reaction has been investigated . The labelling pattern of the conversion of AIR to HMP-P has been studied in detail, and potential reaction mechanisms were proposed. ThiC activity was enhanced by SAM and nicotinamide cofactors. SAM is neither used as a methyl donor, nor is it cleaved to the adenosyl radical; its role in the reaction is thus unclear. The reaction is dependent on the presence of an additional protein, which has not been identified yet . ThiC has been extensively studied in Salmonella enterica. ThiC contains a CXXCXXXXC motif, similar but not exactly the same as the motif found in all AdoMet enzymes. Mutational studies showed that replacement of any cysteine residues in the motif abolished thiamine biosynthesis...

## Biological Role

Catalyzes PYRIMSYN1-RXN (reaction.ecocyc.PYRIMSYN1-RXN). Bound by NADH (molecule.C00004), NADPH (molecule.C00005), a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7), NAD(P)H (molecule.ecocyc.NADH-P-OR-NOP).

## Enriched Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the synthesis of the hydroxymethylpyrimidine phosphate (HMP-P) moiety of thiamine from aminoimidazole ribotide (AIR) in a radical S-adenosyl-L-methionine (SAM)-dependent reaction. {ECO:0000305|PubMed:15292217, ECO:0000305|PubMed:15326535}.

## Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.PYRIMSYN1-RXN|reaction.ecocyc.PYRIMSYN1-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (5)

- `binds` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.NADH-P-OR-NOP|molecule.ecocyc.NADH-P-OR-NOP]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3994|gene.b3994]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P30136`
- `KEGG:ecj:JW3958;eco:b3994;ecoc:C3026_21575;`
- `GeneID:75205512;948492;`
- `GO:GO:0005829; GO:0006417; GO:0008270; GO:0009228; GO:0009229; GO:0045947; GO:0051539; GO:0070284`
- `EC:4.1.99.17`

## Notes

Phosphomethylpyrimidine synthase (EC 4.1.99.17) (Hydroxymethylpyrimidine phosphate synthase) (HMP-P synthase) (HMP-phosphate synthase) (HMPP synthase) (Thiamine biosynthesis protein ThiC)
