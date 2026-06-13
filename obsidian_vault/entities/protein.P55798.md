---
entity_id: "protein.P55798"
entity_type: "protein"
name: "pphA"
source_database: "UniProt"
source_id: "P55798"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pphA prpA yebX b1838 JW1827"
---

# pphA

`protein.P55798`

## Static

- Type: `protein`
- Source: `UniProt:P55798`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Plays a key role in signaling protein misfolding via the CpxR/CPXA transducing system. It also modulates the phosphorylated status of many phosphoproteins in E.coli, some of which acting as major chaperones. Has been shown, in vitro, to act on Ser, Thr and Tyr-phosphorylated substrates. PphA and PphB are phosphoprotein phosphatases that act in transduction of the misfolded protein stress signal in a pathway that includes the PWY0-1485 and which activates transcription of htrA. PphA is involved in induction of the heat shock response. PphA exhibits phosphatase activity toward phosphorylated serine/threonine and phosphorylated tyrosine in protein substrates and PHOSPHO-CPXR phosphorylated CpxR. Additional phosphoproteins accumulate in a pphA mutant, suggesting that they are in vivo targets of PphA . PphA and PphB have similarity to the phosphoprotein phosphatase of bacteriophage lambda (λ-PP) and to Salmonella enterica serovar Typhimurium PrpA and PrpB proteins . A pphA null mutant has a slow growth phenotype. Overexpression of pphA induces the heat shock response . Transcription of the RYEA-RNA RyeA RNA, which is encoded upstream of pphA, interferes with read-through transcription of pphA from the sdsR promoter . PrpA: "protein phosphatase A" Review:

## Biological Role

Catalyzes phosphoprotein phosphohydrolase (reaction.R00164), 3.1.3.16-RXN (reaction.ecocyc.3.1.3.16-RXN), PROTEIN-TYROSINE-PHOSPHATASE-RXN (reaction.ecocyc.PROTEIN-TYROSINE-PHOSPHATASE-RXN).

## Annotation

FUNCTION: Plays a key role in signaling protein misfolding via the CpxR/CPXA transducing system. It also modulates the phosphorylated status of many phosphoproteins in E.coli, some of which acting as major chaperones. Has been shown, in vitro, to act on Ser, Thr and Tyr-phosphorylated substrates.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00164|reaction.R00164]] `KEGG` `database` - via EC:3.1.3.16
- `catalyzes` --> [[reaction.ecocyc.3.1.3.16-RXN|reaction.ecocyc.3.1.3.16-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.PROTEIN-TYROSINE-PHOSPHATASE-RXN|reaction.ecocyc.PROTEIN-TYROSINE-PHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1838|gene.b1838]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P55798`
- `KEGG:ecj:JW1827;eco:b1838;ecoc:C3026_10470;`
- `GeneID:946356;`
- `GO:GO:0004722; GO:0005737; GO:0008138; GO:0008803; GO:0009266; GO:0016791; GO:0046872; GO:0110154`
- `EC:3.1.3.16`

## Notes

Serine/threonine-protein phosphatase 1 (EC 3.1.3.16)
