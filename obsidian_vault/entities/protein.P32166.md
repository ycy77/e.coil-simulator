---
entity_id: "protein.P32166"
entity_type: "protein"
name: "menA"
source_database: "UniProt"
source_id: "P32166"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01937, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01937, ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "menA yiiW b3930 JW3901"
---

# menA

`protein.P32166`

## Static

- Type: `protein`
- Source: `UniProt:P32166`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01937, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01937, ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Conversion of 1,4-dihydroxy-2-naphthoate (DHNA) to demethylmenaquinone (DMK). Attaches octaprenylpyrophosphate, a membrane-bound 40-carbon side chain to DHNA. The conversion of DHNA to DMK proceeds in three stages: the removal of the carboxyl group of DHNA as CO(2), the attachment of the isoprenoid side chain, and a quinol-to-quinone oxidation, which is thought to be spontaneous. {ECO:0000269|PubMed:9573170}. 1,4-dihydroxy-2-naphthoate octaprenyltransferase (MenA) catalyzes the transfer of an octaprenyl side chain to DHNA, the reaction in menaquinone biosynthesis where the pathway becomes associated with the membrane . Site-directed mutagenesis of predicted active site residues confirmed their importance for catalytic activity. A reaction mechanism has been proposed . MenA is an inner membrane protein with nine predicted transmembrane domains. The C-terminus is located in the periplasm . A menA mutant accumulates 1,4-dihydroxy-2-naphthoate in the culture supernatant . menA transposon insertion mutants have increased resistance to the plant essential oils thymol and menthol . Review:

## Biological Role

Catalyzes DMK-RXN (reaction.ecocyc.DMK-RXN). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Conversion of 1,4-dihydroxy-2-naphthoate (DHNA) to demethylmenaquinone (DMK). Attaches octaprenylpyrophosphate, a membrane-bound 40-carbon side chain to DHNA. The conversion of DHNA to DMK proceeds in three stages: the removal of the carboxyl group of DHNA as CO(2), the attachment of the isoprenoid side chain, and a quinol-to-quinone oxidation, which is thought to be spontaneous. {ECO:0000269|PubMed:9573170}.

## Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.DMK-RXN|reaction.ecocyc.DMK-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3930|gene.b3930]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P32166`
- `KEGG:ecj:JW3901;eco:b3930;ecoc:C3026_21240;`
- `GeneID:75169372;75204603;948418;`
- `GO:GO:0000287; GO:0004659; GO:0005886; GO:0006744; GO:0009234; GO:0016020; GO:0042371; GO:0046428`
- `EC:2.5.1.74`

## Notes

1,4-dihydroxy-2-naphthoate octaprenyltransferase (DHNA-octaprenyltransferase) (EC 2.5.1.74)
