---
entity_id: "protein.P64483"
entity_type: "protein"
name: "proXp-y"
source_database: "UniProt"
source_id: "P64483"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "proXp-y yeaK b1787 JW1776"
---

# proXp-y

`protein.P64483`

## Static

- Type: `protein`
- Source: `UniProt:P64483`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: An aminoacyl-tRNA editing enzyme that deacylates Ser-tRNA and/or Thr-tRNA mischarged by lysyl-tRNA synthetase (LysRS), threonyl-tRNA synthetase (ThrRS), seryl-tRNA synthetase (SerRS), alanyl-tRNA synthetase (AlaRS), valyl-tRNA synthetase (ValRS) and isoleucyl-tRNA synthetase (IleRS) in vitro. Also deacylates mischarged Hse-tRNA(Lys) and Hse-tRNA(Ser), and cognate Ser-tRNA(Ser) and Thr-tRNA(Thr) in vitro. The presence of cognate ThrRS abolishes the Thr-tRNA(Thr) deacylase activity, hence this activity is not applicable physiologically. Not able to remove the amino acid moiety from cognate Val-tRNA(Val), Ile-tRNA(Ile), Lys-tRNA(Lys), Ala-tRNA(Ala) or Pro-tRNA(Pro), or from incorrectly charged Ala-tRNA(Pro), Cys-tRNA(Pro) or Leu-tRNA(Pro) in vitro. May be required in vivo to prevent mistranslation and to maintain growth when the error prone stress-inducible lysyl-tRNA synthetase (LysU) is expressed under environmental pressure. {ECO:0000269|PubMed:25918376}. The YeaK protein ("ProXp-ST1") has aminoacyl-tRNA editing activity. It is able to deacylate tRNAs mischarged with serine or threonine, such as Thr-tRNALys, Thr-tRNAVal, and Thr-tRNAIle as well as, to a lesser extent, Ser-tRNALys, Ser-tRNAAla, homoseryl-tRNALys, and Ser-tRNAThr. It does not deacylate cognate Lys-tRNALys, Ala-tRNAAla, Val-tRNAVal, or Ile-tRNAIle...

## Biological Role

Catalyzes RXN0-7429 (reaction.ecocyc.RXN0-7429), RXN0-7430 (reaction.ecocyc.RXN0-7430), RXN0-7431 (reaction.ecocyc.RXN0-7431), RXN0-7432 (reaction.ecocyc.RXN0-7432), RXN0-7433 (reaction.ecocyc.RXN0-7433), RXN0-7434 (reaction.ecocyc.RXN0-7434), RXN0-7435 (reaction.ecocyc.RXN0-7435).

## Annotation

FUNCTION: An aminoacyl-tRNA editing enzyme that deacylates Ser-tRNA and/or Thr-tRNA mischarged by lysyl-tRNA synthetase (LysRS), threonyl-tRNA synthetase (ThrRS), seryl-tRNA synthetase (SerRS), alanyl-tRNA synthetase (AlaRS), valyl-tRNA synthetase (ValRS) and isoleucyl-tRNA synthetase (IleRS) in vitro. Also deacylates mischarged Hse-tRNA(Lys) and Hse-tRNA(Ser), and cognate Ser-tRNA(Ser) and Thr-tRNA(Thr) in vitro. The presence of cognate ThrRS abolishes the Thr-tRNA(Thr) deacylase activity, hence this activity is not applicable physiologically. Not able to remove the amino acid moiety from cognate Val-tRNA(Val), Ile-tRNA(Ile), Lys-tRNA(Lys), Ala-tRNA(Ala) or Pro-tRNA(Pro), or from incorrectly charged Ala-tRNA(Pro), Cys-tRNA(Pro) or Leu-tRNA(Pro) in vitro. May be required in vivo to prevent mistranslation and to maintain growth when the error prone stress-inducible lysyl-tRNA synthetase (LysU) is expressed under environmental pressure. {ECO:0000269|PubMed:25918376}.

## Outgoing Edges (7)

- `catalyzes` --> [[reaction.ecocyc.RXN0-7429|reaction.ecocyc.RXN0-7429]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7430|reaction.ecocyc.RXN0-7430]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7431|reaction.ecocyc.RXN0-7431]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7432|reaction.ecocyc.RXN0-7432]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7433|reaction.ecocyc.RXN0-7433]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7434|reaction.ecocyc.RXN0-7434]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7435|reaction.ecocyc.RXN0-7435]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1787|gene.b1787]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P64483`
- `KEGG:ecj:JW1776;eco:b1787;ecoc:C3026_10190;`
- `GeneID:946303;`
- `GO:GO:0000049; GO:0002161; GO:0002196; GO:0005737; GO:0045903; GO:0106074`
- `EC:3.1.1.-`

## Notes

Multifunctional Ser/Thr-tRNA deacylase ProXp-y (EC 3.1.1.-) (Free-standing editing domain ProXp-y) (Homologous trans-editing factor ProXp-y) (ProXp-ST1) (Prolyl-tRNA synthetase insertion domain homolog ProXp-y) (ProRS INS domain homolog ProXp-y)
