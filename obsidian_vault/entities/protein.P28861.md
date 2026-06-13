---
entity_id: "protein.P28861"
entity_type: "protein"
name: "fpr"
source_database: "UniProt"
source_id: "P28861"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:7961651}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fpr mvrA b3924 JW3895"
---

# fpr

`protein.P28861`

## Static

- Type: `protein`
- Source: `UniProt:P28861`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:7961651}.

## Enriched Summary

FUNCTION: Transports electrons between flavodoxin or ferredoxin and NADPH (PubMed:12234497, PubMed:21306142, PubMed:8449868, PubMed:9839946). Reduces flavodoxin 1, flavodoxin 2 and ferredoxin, ferredoxin being the kinetically and thermodynamically preferred partner (PubMed:12234497). Required for the activation of several enzymes such as pyruvate formate-lyase, anaerobic ribonucleotide reductase and cobalamin-dependent methionine synthase (PubMed:7042345, PubMed:8267617). {ECO:0000269|PubMed:12234497, ECO:0000269|PubMed:21306142, ECO:0000269|PubMed:7042345, ECO:0000269|PubMed:8267617, ECO:0000269|PubMed:8449868, ECO:0000269|PubMed:9839946}. Flavodoxin/ferredoxin-NADP+ reductase (Fpr) participates in chains of redox reactions; it contains a noncovalently bound FAD cofactor that facilitates the reversible electron transfer between NADP(H) and ferredoxins or flavodoxins. Fpr is involved in the activation of anaerobic ribonucleoside reductase , pyruvate-formate lyase (PFL) , methionine synthase and biotin synthase . Ferredoxin can not substitute for flavodoxin as an electron donor for activation of PFL and methionine synthase . Because an fpr mutant has no growth defect on rich or minimal medium under aerobic or anaerobic growth conditions, a second flavodoxin reductase activity, likely G6701-MONOMER, is able to fulfill Fpr's role in activating these enzymes...

## Biological Role

Catalyzes flavodoxin:NADP+ oxidoreductase (reaction.R11485), FLAVONADPREDUCT-RXN (reaction.ecocyc.FLAVONADPREDUCT-RXN), RXN-17897 (reaction.ecocyc.RXN-17897). Bound by FAD (molecule.C00016).

## Annotation

FUNCTION: Transports electrons between flavodoxin or ferredoxin and NADPH (PubMed:12234497, PubMed:21306142, PubMed:8449868, PubMed:9839946). Reduces flavodoxin 1, flavodoxin 2 and ferredoxin, ferredoxin being the kinetically and thermodynamically preferred partner (PubMed:12234497). Required for the activation of several enzymes such as pyruvate formate-lyase, anaerobic ribonucleotide reductase and cobalamin-dependent methionine synthase (PubMed:7042345, PubMed:8267617). {ECO:0000269|PubMed:12234497, ECO:0000269|PubMed:21306142, ECO:0000269|PubMed:7042345, ECO:0000269|PubMed:8267617, ECO:0000269|PubMed:8449868, ECO:0000269|PubMed:9839946}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R11485|reaction.R11485]] `KEGG` `database` - via EC:1.19.1.1
- `catalyzes` --> [[reaction.ecocyc.FLAVONADPREDUCT-RXN|reaction.ecocyc.FLAVONADPREDUCT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17897|reaction.ecocyc.RXN-17897]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3924|gene.b3924]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P28861`
- `KEGG:ecj:JW3895;eco:b3924;`
- `GeneID:948414;`
- `GO:GO:0000303; GO:0004324; GO:0005829; GO:0009410; GO:0016226; GO:0034599; GO:0042167; GO:0071949`
- `EC:1.18.1.2; 1.19.1.1`

## Notes

Flavodoxin/ferredoxin--NADP reductase (EC 1.18.1.2) (EC 1.19.1.1) (Ferredoxin (flavodoxin):NADP(+) oxidoreductase) (Ferredoxin--NADP reductase) (FNR) (Flavodoxin--NADP reductase) (FLDR) (Methyl viologen resistance protein A) (dA1)
