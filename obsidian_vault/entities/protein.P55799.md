---
entity_id: "protein.P55799"
entity_type: "protein"
name: "pphB"
source_database: "UniProt"
source_id: "P55799"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pphB prpB ygbH b2734 JW2704"
---

# pphB

`protein.P55799`

## Static

- Type: `protein`
- Source: `UniProt:P55799`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Has been shown, in vitro, to act on Ser, Thr and Tyr-phosphorylated substrates. PphA and PphB are phosphoprotein phosphatases that act in transduction of the misfolded protein stress signal in a pathway that includes the PWY0-1485 and which activates transcription of htrA. PphB exhibits phosphatase activity toward phosphorylated serine/threonine and phosphorylated tyrosine in protein substrates. Additional phosphoproteins accumulate in a pphB mutant, suggesting that they are in vivo targets of PphB . PphA and PphB have similarity to the phosphoprotein phosphatase of bacteriophage lambda (λ-PP) and to Salmonella enterica serovar Typhimurium PrpA and PrpB proteins . A pphB null mutant has a slow growth phenotype . PrpB: "protein phosphatase B" Reviews:

## Biological Role

Catalyzes phosphoprotein phosphohydrolase (reaction.R00164), 3.1.3.16-RXN (reaction.ecocyc.3.1.3.16-RXN), PROTEIN-TYROSINE-PHOSPHATASE-RXN (reaction.ecocyc.PROTEIN-TYROSINE-PHOSPHATASE-RXN).

## Annotation

FUNCTION: Has been shown, in vitro, to act on Ser, Thr and Tyr-phosphorylated substrates.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00164|reaction.R00164]] `KEGG` `database` - via EC:3.1.3.16
- `catalyzes` --> [[reaction.ecocyc.3.1.3.16-RXN|reaction.ecocyc.3.1.3.16-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.PROTEIN-TYROSINE-PHOSPHATASE-RXN|reaction.ecocyc.PROTEIN-TYROSINE-PHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2734|gene.b2734]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P55799`
- `KEGG:ecj:JW2704;eco:b2734;ecoc:C3026_15040;`
- `GeneID:947196;`
- `GO:GO:0004722; GO:0005737; GO:0008138; GO:0008803; GO:0016791; GO:0046872; GO:0110154`
- `EC:3.1.3.16`

## Notes

Serine/threonine-protein phosphatase 2 (EC 3.1.3.16)
