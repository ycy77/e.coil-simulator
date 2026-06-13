---
entity_id: "protein.P27859"
entity_type: "protein"
name: "tatD"
source_database: "UniProt"
source_id: "P27859"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00901, ECO:0000269|PubMed:10747959, ECO:0000269|PubMed:25114049}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tatD mttC yigW yigX b4483 JW5931"
---

# tatD

`protein.P27859`

## Static

- Type: `protein`
- Source: `UniProt:P27859`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00901, ECO:0000269|PubMed:10747959, ECO:0000269|PubMed:25114049}.

## Enriched Summary

FUNCTION: 3'-5' exonuclease that prefers single-stranded DNA and RNA. May play a role in the H(2)O(2)-induced DNA damage repair. {ECO:0000255|HAMAP-Rule:MF_00901, ECO:0000269|PubMed:10747959, ECO:0000269|PubMed:25114049}. TatD is a magnesium dependent 3' - 5' exonuclease with a preference for single strand DNA and RNA. A tatD knockout mutant is more sensitive to H2O2 than wild type. Purified TatD has efficient exonuclease activity on ssDNA containing a 3' terminal deaminated base (uracil or hypoxanthine). TatD may be involved in the repair of H2O2 induced DNA damage . Purified, crystallised TatD has a TIM barrel fold (an eight stranded α β barrel). The conserved residues Glu91, Glu201 and Asp 203 are involved in metal binding at the active site . TatD exhibits magnesium-dependent DNase activity . A tatD mutant shows increased RecA-GFP foci formation . Deletion of tatD has very little effect on growth . A tatD ycfH yjjV triple mutant does not exhibit phenotypes that would suggest involvement of the corresponding proteins in the Sec-independent Tat protein export system. Like a tatD deletion, TatD overproduction does not cause transport phenotypes . In a tatD mutant, mutant forms of Tat export system substrates were seen to accumulate instead of being degraded rapidly ; however, this result may have been due to inadvertent overexpression of the Tat export substrates...

## Biological Role

Catalyzes 3.1.11.1-RXN (reaction.ecocyc.3.1.11.1-RXN), 3'-exoribonuclease (reaction.ecocyc.RXN0-4223). Bound by Magnesium cation (molecule.C00305).

## Annotation

FUNCTION: 3'-5' exonuclease that prefers single-stranded DNA and RNA. May play a role in the H(2)O(2)-induced DNA damage repair. {ECO:0000255|HAMAP-Rule:MF_00901, ECO:0000269|PubMed:10747959, ECO:0000269|PubMed:25114049}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.3.1.11.1-RXN|reaction.ecocyc.3.1.11.1-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-4223|reaction.ecocyc.RXN0-4223]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b4483|gene.b4483]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P27859`
- `KEGG:ecj:JW5931;eco:b4483;ecoc:C3026_20770;`
- `GeneID:2847752;`
- `GO:GO:0000175; GO:0000287; GO:0004536; GO:0005737; GO:0005829; GO:0008310; GO:0042542; GO:0046872`
- `EC:3.1.11.-; 3.1.13.-`

## Notes

3'-5' ssDNA/RNA exonuclease TatD (EC 3.1.11.-) (EC 3.1.13.-) (DNase TatD)
