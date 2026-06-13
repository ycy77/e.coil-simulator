---
entity_id: "protein.P66948"
entity_type: "protein"
name: "bepA"
source_database: "UniProt"
source_id: "P66948"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000255|HAMAP-Rule:MF_00997, ECO:0000269|PubMed:22491786, ECO:0000269|PubMed:24003122}. Note=A significant amount of BepA is membrane-associated. This localization could result from interaction with the BAM complex."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "bepA yfgC b2494 JW2479"
---

# bepA

`protein.P66948`

## Static

- Type: `protein`
- Source: `UniProt:P66948`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000255|HAMAP-Rule:MF_00997, ECO:0000269|PubMed:22491786, ECO:0000269|PubMed:24003122}. Note=A significant amount of BepA is membrane-associated. This localization could result from interaction with the BAM complex.

## Enriched Summary

FUNCTION: Functions both as a chaperone and a metalloprotease. Maintains the integrity of the outer membrane by promoting either the assembly or the elimination of outer membrane proteins, depending on their folding state. Promotes disulfide rearrangement of LptD during its biogenesis, and proteolytic degradation of LptD and BamA when their proper assembly is compromised. May facilitate membrane attachment of LoiP under unfavorable conditions. {ECO:0000255|HAMAP-Rule:MF_00997, ECO:0000269|PubMed:22491786, ECO:0000269|PubMed:24003122}. BepA (formerly YfgC) is a periplasmic protein and a member of the M48 metalloprotease family ; BepA functions as a protease/chaperone with a role in maintaining outer membrane integrity . Purified BepA has low proteolytic activity in vitro which is absent in the presence of metal chelating reagents. BepA promotes the formation of correct disulfide bonds in EG11569-MONOMER "LptD". This activity is independent of its protease activity. The protease function of BepA serves to degrade LptD that fails to form an outer membrane translocon. BepA also cleaves BamA in a ΔsurA background . BepA degrades mutant LptD (LptD4213) that is stalled at later stages of the Bam-mediated assembly process; the periplasmic proteases BepA, G6470-MONOMER "YcaL" and CPLX0-2921 "DegP" degrade stalled LptD substrate at different stages in the OMP assembly process...

## Biological Role

Catalyzes 3.4.21.107-RXN (reaction.ecocyc.3.4.21.107-RXN).

## Annotation

FUNCTION: Functions both as a chaperone and a metalloprotease. Maintains the integrity of the outer membrane by promoting either the assembly or the elimination of outer membrane proteins, depending on their folding state. Promotes disulfide rearrangement of LptD during its biogenesis, and proteolytic degradation of LptD and BamA when their proper assembly is compromised. May facilitate membrane attachment of LoiP under unfavorable conditions. {ECO:0000255|HAMAP-Rule:MF_00997, ECO:0000269|PubMed:22491786, ECO:0000269|PubMed:24003122}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.3.4.21.107-RXN|reaction.ecocyc.3.4.21.107-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2494|gene.b2494]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P66948`
- `KEGG:ecj:JW2479;eco:b2494;ecoc:C3026_13835;`
- `GeneID:75204231;947029;`
- `GO:GO:0003756; GO:0004222; GO:0008270; GO:0016020; GO:0030288; GO:0043165; GO:0046872; GO:0051603`
- `EC:3.4.-.-`

## Notes

Beta-barrel assembly-enhancing protease (EC 3.4.-.-)
