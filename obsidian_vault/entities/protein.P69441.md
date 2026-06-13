---
entity_id: "protein.P69441"
entity_type: "protein"
name: "adk"
source_database: "UniProt"
source_id: "P69441"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00235}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "adk dnaW plsA b0474 JW0463"
---

# adk

`protein.P69441`

## Static

- Type: `protein`
- Source: `UniProt:P69441`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00235}.

## Enriched Summary

FUNCTION: Catalyzes the reversible transfer of the terminal phosphate group between ATP and AMP. Plays an important role in cellular energy homeostasis and in adenine nucleotide metabolism. {ECO:0000255|HAMAP-Rule:MF_00235, ECO:0000269|PubMed:166976, ECO:0000269|PubMed:6243627}. Adenylate kinase is an essential enzyme required for the biosynthesis of purine ribonucleotides and has a key role in controlling the rate of cell growth . Adenylate kinase is a relatively small, monomeric protein that consists of three functionally relevant domains: the N-terminal nucleotide binding (NMPbind) domain that binds AMP, followed by the CORE domain that represents the bulk of the enzyme and encloses the LID domain that binds ATP. There are estimated to be approximately 10,000 molecules of adenylate kinase present in the cell . Adenylate kinase activity may be inhibited by interaction with the phosphorylated form of PTSH-MONOMER HPr and the ribosome . Various crystal and solution structures of the enzyme have been solved, and a reaction mechanism was proposed and refined. Based on new data showing activation of adenylate kinase by direct binding of Mg2+, a new kinetic model for the forward reaction involving a Mg2+-activated random bi-bi mechanism has been proposed. The requirement for binding of Mg2+ before binding of AMP to the enzyme explains the apparent competitive inhibition by AMP...

## Biological Role

Catalyzes ATP:AMP phosphotransferase (reaction.R00127), ADENYL-KIN-RXN (reaction.ecocyc.ADENYL-KIN-RXN), CDPKIN-RXN (reaction.ecocyc.CDPKIN-RXN), DCDPKIN-RXN (reaction.ecocyc.DCDPKIN-RXN), DGDPKIN-RXN (reaction.ecocyc.DGDPKIN-RXN), DTDPKIN-RXN (reaction.ecocyc.DTDPKIN-RXN), GDPKIN-RXN (reaction.ecocyc.GDPKIN-RXN), RXN-14074 (reaction.ecocyc.RXN-14074), and 1 more. Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00730` Thiamine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the reversible transfer of the terminal phosphate group between ATP and AMP. Plays an important role in cellular energy homeostasis and in adenine nucleotide metabolism. {ECO:0000255|HAMAP-Rule:MF_00235, ECO:0000269|PubMed:166976, ECO:0000269|PubMed:6243627}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00730` Thiamine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (9)

- `catalyzes` --> [[reaction.R00127|reaction.R00127]] `KEGG` `database` - via EC:2.7.4.3
- `catalyzes` --> [[reaction.ecocyc.ADENYL-KIN-RXN|reaction.ecocyc.ADENYL-KIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.CDPKIN-RXN|reaction.ecocyc.CDPKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.DCDPKIN-RXN|reaction.ecocyc.DCDPKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.DGDPKIN-RXN|reaction.ecocyc.DGDPKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.DTDPKIN-RXN|reaction.ecocyc.DTDPKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.GDPKIN-RXN|reaction.ecocyc.GDPKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-14074|reaction.ecocyc.RXN-14074]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.UDPKIN-RXN|reaction.ecocyc.UDPKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0474|gene.b0474]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69441`
- `KEGG:ecj:JW0463;eco:b0474;ecoc:C3026_02330;`
- `GeneID:75170492;945097;`
- `GO:GO:0000287; GO:0004017; GO:0004550; GO:0005524; GO:0005737; GO:0005829; GO:0006172; GO:0009123; GO:0009132; GO:0015951; GO:0016208; GO:0044209; GO:0046083`
- `EC:2.7.4.3`

## Notes

Adenylate kinase (AK) (EC 2.7.4.3) (ATP-AMP transphosphorylase) (ATP:AMP phosphotransferase) (Adenylate monophosphate kinase)
