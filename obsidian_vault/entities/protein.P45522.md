---
entity_id: "protein.P45522"
entity_type: "protein"
name: "kefB"
source_database: "UniProt"
source_id: "P45522"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01412, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01412, ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "kefB trkB b3350 JW3313"
---

# kefB

`protein.P45522`

## Static

- Type: `protein`
- Source: `UniProt:P45522`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01412, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01412, ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Pore-forming subunit of a potassium efflux system that confers protection against electrophiles. Catalyzes K(+)/H(+) antiport. {ECO:0000255|HAMAP-Rule:MF_01412, ECO:0000269|PubMed:3301813, ECO:0000269|PubMed:9023177}. KefB and KefC are two independent glutathione-regulated potassium efflux systems, which play a role in protecting the cell from electrophile toxicity. Mutations in kefB and kefC affect potassium efflux at neutral pH, can be complemented by the cloned genes and probably function via potassium/proton antiport . Potassium efflux by KefB or KefC is activated by adducts formed by reaction of glutathione with electrophilic compounds such as N-ethylmaleimide, methylglyoxal and chlorodinitrobenzene . Potassium efflux mediated by KefB and KefC leads to acidification of the cytoplasm, which protects the cell from electrophile toxicity . KefB and KefC differ in their activation by methylglyoxal, with KefC only weakly activated . KefB is a member of the CPA2 family of monovalent cation:proton antiporters. In addition to KefB and KefC, additional unidentified potassium efflux systems exist.

## Biological Role

Catalyzes potassium:proton antiport (reaction.ecocyc.TRANS-RXN-42).

## Annotation

FUNCTION: Pore-forming subunit of a potassium efflux system that confers protection against electrophiles. Catalyzes K(+)/H(+) antiport. {ECO:0000255|HAMAP-Rule:MF_01412, ECO:0000269|PubMed:3301813, ECO:0000269|PubMed:9023177}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-42|reaction.ecocyc.TRANS-RXN-42]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3350|gene.b3350]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P45522`
- `KEGG:ecj:JW3313;eco:b3350;ecoc:C3026_18195;`
- `GeneID:947858;`
- `GO:GO:0005886; GO:0006813; GO:0015503; GO:0051453; GO:1902600; GO:1903103`

## Notes

Glutathione-regulated potassium-efflux system protein KefB (K(+)/H(+) antiporter) (NEM-activable K(+)/H(+) antiporter)
