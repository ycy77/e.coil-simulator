---
entity_id: "protein.P76043"
entity_type: "protein"
name: "ycjQ"
source_database: "UniProt"
source_id: "P76043"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ycjQ b1313 JW1306"
---

# ycjQ

`protein.P76043`

## Static

- Type: `protein`
- Source: `UniProt:P76043`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the NAD(+)-dependent oxidation of the hydroxyl group at C3 of D-gulosides leading to 3-dehydro-D-gulosides. Probably functions in a metabolic pathway that transforms D-gulosides to D-glucosides. Is also able to catalyze the reverse reactions, i.e. the NADH-dependent reduction of the oxo group at C3 of 3-dehydro-D-gulosides leading to D-gulosides. In vitro, can oxidize D-gulose and methyl beta-D-guloside, and reduce methyl alpha-3-dehydro-D-guloside and methyl beta-3-dehydro-D-guloside. However, the actual specific physiological substrates for this metabolic pathway are unknown. {ECO:0000269|PubMed:30742415}. Purified YcjQ has NAD+-dependent D-guloside dehydrogenase activity .

## Biological Role

Catalyzes RXN-20680 (reaction.ecocyc.RXN-20680).

## Annotation

FUNCTION: Catalyzes the NAD(+)-dependent oxidation of the hydroxyl group at C3 of D-gulosides leading to 3-dehydro-D-gulosides. Probably functions in a metabolic pathway that transforms D-gulosides to D-glucosides. Is also able to catalyze the reverse reactions, i.e. the NADH-dependent reduction of the oxo group at C3 of 3-dehydro-D-gulosides leading to D-gulosides. In vitro, can oxidize D-gulose and methyl beta-D-guloside, and reduce methyl alpha-3-dehydro-D-guloside and methyl beta-3-dehydro-D-guloside. However, the actual specific physiological substrates for this metabolic pathway are unknown. {ECO:0000269|PubMed:30742415}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-20680|reaction.ecocyc.RXN-20680]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1313|gene.b1313]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76043`
- `KEGG:ecj:JW1306;eco:b1313;ecoc:C3026_07695;`
- `GeneID:945971;`
- `GO:GO:0008270; GO:0016491; GO:0016616`
- `EC:1.1.1.-`

## Notes

D-guloside 3-dehydrogenase (EC 1.1.1.-)
