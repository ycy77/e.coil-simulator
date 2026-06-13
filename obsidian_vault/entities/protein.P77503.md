---
entity_id: "protein.P77503"
entity_type: "protein"
name: "ycjS"
source_database: "UniProt"
source_id: "P77503"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ycjS b1315 JW1308"
---

# ycjS

`protein.P77503`

## Static

- Type: `protein`
- Source: `UniProt:P77503`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the NADH-dependent reduction of the oxo group at C3 of 3-dehydro-D-glucosides leading to D-glucosides. Probably functions in a metabolic pathway that transforms D-gulosides to D-glucosides. Can use 3-dehydro-D-glucose, methyl alpha-3-dehydro-D-glucoside and methyl beta-3-dehydro-D-glucoside as substrates in vitro. However, the actual specific physiological substrates for this metabolic pathway are unknown. To a lesser extent, is also able to catalyze the reverse reactions, i.e. the NAD(+)-dependent oxidation of the hydroxyl group at C3 of D-glucosides leading to 3-dehydro-D-glucosides. Cannot act on UDP-glucose, UDP-N-acetyl-D-glucosamine, D-glucosamine, N-acetyl-D-glucosamine, or UDP-D-galactose. {ECO:0000269|PubMed:30742415}. Purified YcjS has NAD+-dependent D-glucoside 3-dehydrogenase activity . YcjS was predicted to be an NAD+-dependent dehydrogenase . Based on sequence similarity, YcjS was also predicted to be a D-galactose 1-dehydrogenase . However, this is not consistent with the known biochemistry of E. coli, which metabolizes galactose via the PWY-6317 "Leloir pathway".

## Biological Role

Catalyzes RXN-20682 (reaction.ecocyc.RXN-20682).

## Annotation

FUNCTION: Catalyzes the NADH-dependent reduction of the oxo group at C3 of 3-dehydro-D-glucosides leading to D-glucosides. Probably functions in a metabolic pathway that transforms D-gulosides to D-glucosides. Can use 3-dehydro-D-glucose, methyl alpha-3-dehydro-D-glucoside and methyl beta-3-dehydro-D-glucoside as substrates in vitro. However, the actual specific physiological substrates for this metabolic pathway are unknown. To a lesser extent, is also able to catalyze the reverse reactions, i.e. the NAD(+)-dependent oxidation of the hydroxyl group at C3 of D-glucosides leading to 3-dehydro-D-glucosides. Cannot act on UDP-glucose, UDP-N-acetyl-D-glucosamine, D-glucosamine, N-acetyl-D-glucosamine, or UDP-D-galactose. {ECO:0000269|PubMed:30742415}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-20682|reaction.ecocyc.RXN-20682]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1315|gene.b1315]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77503`
- `KEGG:ecj:JW1308;eco:b1315;ecoc:C3026_07705;`
- `GeneID:948589;`
- `GO:GO:0000166; GO:0016616`
- `EC:1.1.1.-`

## Notes

D-glucoside 3-dehydrogenase (EC 1.1.1.-)
