---
entity_id: "protein.P42601"
entity_type: "protein"
name: "alx"
source_database: "UniProt"
source_id: "P42601"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "alx ygjT b3088 JW5515"
---

# alx

`protein.P42601`

## Static

- Type: `protein`
- Source: `UniProt:P42601`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Functions as a low-activity manganese exporter at alkaline pH (PubMed:38869303). Involved in manganese homeostasis (PubMed:29440394, PubMed:38869303). Alx-mediated manganese export serves as a primary protective mechanism that fine tunes the cytoplasmic manganese content, especially during alkaline stress (PubMed:38869303). Transport of Mn(2+) by Alx is unlikely to be accompanied by an H(+) antiport (PubMed:38869303). Alx does not participate in maintaining cellular pH (PubMed:38869303). {ECO:0000269|PubMed:29440394, ECO:0000269|PubMed:38869303}. Alx is a "low-activity" Mn2+ exporter with a role in manganese ion homeostasis at alkaline pH; Alx-mediated Mn2+ export prevents a build-up of intracellular Mn2+ under alkaline conditions . Previously Alx was predicted to be a membrane-bound redox modulator . Expression from the alx promoter is highly induced by growth at an external pH of 8.5 and above both aerobically and anaerobically; expression is repressed by low pH only under aerobic conditions . alx expression is repressed by paraquat . pH-responsive regulation of alx expression is achieved via a novel pH-responsive riboregulator element (PRE) that was previously thought to encode small RNA G0-8869 SraF...

## Biological Role

Catalyzes Mn2+ export (reaction.ecocyc.TRANS-RXN0-487).

## Annotation

FUNCTION: Functions as a low-activity manganese exporter at alkaline pH (PubMed:38869303). Involved in manganese homeostasis (PubMed:29440394, PubMed:38869303). Alx-mediated manganese export serves as a primary protective mechanism that fine tunes the cytoplasmic manganese content, especially during alkaline stress (PubMed:38869303). Transport of Mn(2+) by Alx is unlikely to be accompanied by an H(+) antiport (PubMed:38869303). Alx does not participate in maintaining cellular pH (PubMed:38869303). {ECO:0000269|PubMed:29440394, ECO:0000269|PubMed:38869303}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-487|reaction.ecocyc.TRANS-RXN0-487]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3088|gene.b3088]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P42601`
- `KEGG:ecj:JW5515;eco:b3088;ecoc:C3026_16865;`
- `GeneID:947607;`
- `GO:GO:0005886; GO:0071467`

## Notes

Manganese exporter Alx
