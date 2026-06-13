---
entity_id: "protein.P00393"
entity_type: "protein"
name: "ndh"
source_database: "UniProt"
source_id: "P00393"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:10664466, ECO:0000269|PubMed:2679883, ECO:0000269|PubMed:6362717, ECO:0000269|PubMed:6784762, ECO:0000269|PubMed:7009604, ECO:0000269|PubMed:7020757}; Peripheral membrane protein {ECO:0000269|PubMed:10664466, ECO:0000305|PubMed:12176061}; Cytoplasmic side {ECO:0000305|PubMed:12176061}. Note=Membrane-bound (PubMed:10664466). Interaction with the membrane is probably mediated by amphipathic helices and electrostatic interactions (PubMed:15581635). Copurifies with phospholipids (PubMed:6362717, PubMed:7020757). {ECO:0000269|PubMed:10664466, ECO:0000269|PubMed:15581635, ECO:0000269|PubMed:6362717, ECO:0000269|PubMed:7020757}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ndh b1109 JW1095"
---

# ndh

`protein.P00393`

## Static

- Type: `protein`
- Source: `UniProt:P00393`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:10664466, ECO:0000269|PubMed:2679883, ECO:0000269|PubMed:6362717, ECO:0000269|PubMed:6784762, ECO:0000269|PubMed:7009604, ECO:0000269|PubMed:7020757}; Peripheral membrane protein {ECO:0000269|PubMed:10664466, ECO:0000305|PubMed:12176061}; Cytoplasmic side {ECO:0000305|PubMed:12176061}. Note=Membrane-bound (PubMed:10664466). Interaction with the membrane is probably mediated by amphipathic helices and electrostatic interactions (PubMed:15581635). Copurifies with phospholipids (PubMed:6362717, PubMed:7020757). {ECO:0000269|PubMed:10664466, ECO:0000269|PubMed:15581635, ECO:0000269|PubMed:6362717, ECO:0000269|PubMed:7020757}.

## Enriched Summary

FUNCTION: Alternative, nonproton pumping NADH:quinone oxidoreductase that delivers electrons to the respiratory chain by oxidation of NADH and reduction of quinones (PubMed:10664466, PubMed:2679883, PubMed:3122832, PubMed:6362717, PubMed:6784762, PubMed:7009604, PubMed:7020757). Utilizes NADH exclusively, and electron flow from NADH to ubiquinone does not generate an electrochemical gradient (PubMed:2679883, PubMed:3122832). {ECO:0000269|PubMed:10664466, ECO:0000269|PubMed:2679883, ECO:0000269|PubMed:3122832, ECO:0000269|PubMed:6362717, ECO:0000269|PubMed:6784762, ECO:0000269|PubMed:7009604, ECO:0000269|PubMed:7020757}.; FUNCTION: It may also contribute to copper homeostasis and bacterial oxidative protection (PubMed:10510271, PubMed:16759635, PubMed:21390523, PubMed:7487066). Shows cupric reductase activity, and catalyzes the reduction of Cu(2+) to Cu(+) with NADH as electron donor (PubMed:10510271). Exhibits Cu(2+) reductase activity in the presence of either FAD or quinone, but is unable to reduce Fe(3+) (PubMed:10510271). Contains thiolate-bound copper (PubMed:12176061). {ECO:0000269|PubMed:10510271, ECO:0000269|PubMed:12176061, ECO:0000269|PubMed:16759635, ECO:0000269|PubMed:21390523, ECO:0000269|PubMed:7487066}...

## Biological Role

Catalyzes R170-RXN (reaction.ecocyc.R170-RXN), RXN0-5330 (reaction.ecocyc.RXN0-5330), RXN0-7123 (reaction.ecocyc.RXN0-7123). Bound by FAD (molecule.C00016), Magnesium cation (molecule.C00305), Cu+ (molecule.ecocyc.CU_).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Alternative, nonproton pumping NADH:quinone oxidoreductase that delivers electrons to the respiratory chain by oxidation of NADH and reduction of quinones (PubMed:10664466, PubMed:2679883, PubMed:3122832, PubMed:6362717, PubMed:6784762, PubMed:7009604, PubMed:7020757). Utilizes NADH exclusively, and electron flow from NADH to ubiquinone does not generate an electrochemical gradient (PubMed:2679883, PubMed:3122832). {ECO:0000269|PubMed:10664466, ECO:0000269|PubMed:2679883, ECO:0000269|PubMed:3122832, ECO:0000269|PubMed:6362717, ECO:0000269|PubMed:6784762, ECO:0000269|PubMed:7009604, ECO:0000269|PubMed:7020757}.; FUNCTION: It may also contribute to copper homeostasis and bacterial oxidative protection (PubMed:10510271, PubMed:16759635, PubMed:21390523, PubMed:7487066). Shows cupric reductase activity, and catalyzes the reduction of Cu(2+) to Cu(+) with NADH as electron donor (PubMed:10510271). Exhibits Cu(2+) reductase activity in the presence of either FAD or quinone, but is unable to reduce Fe(3+) (PubMed:10510271). Contains thiolate-bound copper (PubMed:12176061). {ECO:0000269|PubMed:10510271, ECO:0000269|PubMed:12176061, ECO:0000269|PubMed:16759635, ECO:0000269|PubMed:21390523, ECO:0000269|PubMed:7487066}.

## Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.R170-RXN|reaction.ecocyc.R170-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5330|reaction.ecocyc.RXN0-5330]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7123|reaction.ecocyc.RXN0-7123]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (4)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CU|molecule.ecocyc.CU_]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b1109|gene.b1109]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00393`
- `KEGG:ecj:JW1095;eco:b1109;ecoc:C3026_06690;`
- `GeneID:86863609;93776299;946792;`
- `GO:GO:0005886; GO:0008137; GO:0008823; GO:0009060; GO:0009061; GO:0019646; GO:0030964; GO:0050660; GO:0055070; GO:0120555`
- `EC:1.16.1.-; 1.6.5.9`

## Notes

Type II NADH:quinone oxidoreductase (EC 1.6.5.9) (Cupric reductase) (EC 1.16.1.-) (NADH dehydrogenase-2) (NADH dh II) (NDH-2) (NADH-quinone reductase) (NQR) (NADH:ubiquinone oxidoreductase) (Respiratory NADH dehydrogenase)
