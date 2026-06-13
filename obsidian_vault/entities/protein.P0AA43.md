---
entity_id: "protein.P0AA43"
entity_type: "protein"
name: "rsuA"
source_database: "UniProt"
source_id: "P0AA43"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rsuA yejD b2183 JW2171"
---

# rsuA

`protein.P0AA43`

## Static

- Type: `protein`
- Source: `UniProt:P0AA43`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Responsible for synthesis of pseudouridine from uracil-516 in 16S ribosomal RNA. {ECO:0000269|PubMed:10376875, ECO:0000269|PubMed:7612632}. RsuA is the pseudouridine synthase that is responsible for pseudouridylation of 16S rRNA at position 516 . In vitro, the enzyme does not modify free 16S rRNA. The preferred substrate is a 5'-terminal fragment of 16S rRNA complexed with 30S ribosomal proteins, suggesting that pseudouridylation occurs at an intermediate stage of 30S assembly in vivo . RsuA has the highest affinity to the 5'-terminal 16S fragment complexed with ribosomal protein S17 alone . Crystal structures of RsuA in complex with uracil or UMP have been solved. RsuA consists of an N-terminal domain with structural similarity to ribosomal protein S4, an extended linker region, and a C-terminal catalytic domain. Despite limited sequence similarity, the structure of RsuA is similar to that of TruA, a tRNA pseudouridine synthase . The N-terminal S4-like domain may be important for substrate recognition . An rsuA mutation causes a defect in pseudouridylation at position 516 in the 16S rRNA, and a D102N or D102T mutation at a conserved aspartate residue was shown to cause a defect in catalytic activity . An rsuA mutant does not exhibit any obvious growth defect...

## Biological Role

Catalyzes RXN-11833 (reaction.ecocyc.RXN-11833).

## Annotation

FUNCTION: Responsible for synthesis of pseudouridine from uracil-516 in 16S ribosomal RNA. {ECO:0000269|PubMed:10376875, ECO:0000269|PubMed:7612632}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-11833|reaction.ecocyc.RXN-11833]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2183|gene.b2183]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AA43`
- `KEGG:ecj:JW2171;eco:b2183;ecoc:C3026_12210;`
- `GeneID:75172312;75206437;945378;`
- `GO:GO:0000455; GO:0003723; GO:0005829; GO:0009982; GO:0120159; GO:0160136`
- `EC:5.4.99.19`

## Notes

Ribosomal small subunit pseudouridine synthase A (EC 5.4.99.19) (16S pseudouridylate 516 synthase) (16S rRNA pseudouridine(516) synthase) (rRNA pseudouridylate synthase A) (rRNA-uridine isomerase A)
