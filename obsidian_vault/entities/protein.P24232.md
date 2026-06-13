---
entity_id: "protein.P24232"
entity_type: "protein"
name: "hmp"
source_database: "UniProt"
source_id: "P24232"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:7875569}. Note=Has also been found to localize into the periplasm, but spectral analysis revealed that biochemically active HMP is exclusively found in the cytoplasmic fraction."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hmp fsrB hmpA b2552 JW2536"
---

# hmp

`protein.P24232`

## Static

- Type: `protein`
- Source: `UniProt:P24232`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:7875569}. Note=Has also been found to localize into the periplasm, but spectral analysis revealed that biochemically active HMP is exclusively found in the cytoplasmic fraction.

## Enriched Summary

FUNCTION: Is involved in NO detoxification in an aerobic process, termed nitric oxide dioxygenase (NOD) reaction that utilizes O(2) and NAD(P)H to convert NO to nitrate, which protects the bacterium from various noxious nitrogen compounds. Therefore, plays a central role in the inducible response to nitrosative stress.; FUNCTION: In the presence of oxygen and NADH, HMP has NADH oxidase activity, which leads to the generation of superoxide and H(2)O(2), both in vitro and in vivo, and it has been suggested that HMP might act as an amplifier of superoxide stress. Under anaerobic conditions, HMP also exhibits nitric oxide reductase and FAD reductase activities. However, all these reactions are much lower than NOD activity.; FUNCTION: Various electron acceptors are also reduced by HMP in vitro, including dihydropterine, ferrisiderophores, ferric citrate, cytochrome c, nitrite, S-nitrosoglutathione, and alkylhydroperoxides. However, it is unknown if these reactions are of any biological significance in vivo. Hmp is a flavohemoglobin with multiple enzymatic activities in vitro; however, its nitric oxide dioxygenase (NOD) activity, which is also the major nitric oxide detoxification system in the cell, appears to be the physiologically relevant function...

## Biological Role

Catalyzes nitric oxide,NAD(P)H2:oxygen oxidoreductase (reaction.R05724), nitric oxide,NADPH2:oxygen oxidoreductase (reaction.R05725), 1.5.1.34-RXN (reaction.ecocyc.1.5.1.34-RXN), R621-RXN (reaction.ecocyc.R621-RXN). Bound by FAD (molecule.C00016), protoheme (molecule.ecocyc.PROTOHEME).

## Annotation

FUNCTION: Is involved in NO detoxification in an aerobic process, termed nitric oxide dioxygenase (NOD) reaction that utilizes O(2) and NAD(P)H to convert NO to nitrate, which protects the bacterium from various noxious nitrogen compounds. Therefore, plays a central role in the inducible response to nitrosative stress.; FUNCTION: In the presence of oxygen and NADH, HMP has NADH oxidase activity, which leads to the generation of superoxide and H(2)O(2), both in vitro and in vivo, and it has been suggested that HMP might act as an amplifier of superoxide stress. Under anaerobic conditions, HMP also exhibits nitric oxide reductase and FAD reductase activities. However, all these reactions are much lower than NOD activity.; FUNCTION: Various electron acceptors are also reduced by HMP in vitro, including dihydropterine, ferrisiderophores, ferric citrate, cytochrome c, nitrite, S-nitrosoglutathione, and alkylhydroperoxides. However, it is unknown if these reactions are of any biological significance in vivo.

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.R05724|reaction.R05724]] `KEGG` `database` - via EC:1.14.12.17
- `catalyzes` --> [[reaction.R05725|reaction.R05725]] `KEGG` `database` - via EC:1.14.12.17
- `catalyzes` --> [[reaction.ecocyc.1.5.1.34-RXN|reaction.ecocyc.1.5.1.34-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.R621-RXN|reaction.ecocyc.R621-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.PROTOHEME|molecule.ecocyc.PROTOHEME]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2552|gene.b2552]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P24232`
- `KEGG:ecj:JW2536;eco:b2552;ecoc:C3026_14130;`
- `GeneID:75206245;947018;`
- `GO:GO:0005344; GO:0005504; GO:0005737; GO:0008941; GO:0009636; GO:0019825; GO:0020037; GO:0032843; GO:0046210; GO:0046872; GO:0051409; GO:0071500; GO:0071949`
- `EC:1.14.12.17`

## Notes

Flavohemoprotein (Flavohemoglobin) (HMP) (Hemoglobin-like protein) (Nitric oxide dioxygenase) (NO oxygenase) (NOD) (EC 1.14.12.17)
