---
entity_id: "protein.P0AA39"
entity_type: "protein"
name: "rluC"
source_database: "UniProt"
source_id: "P0AA39"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rluC yceC b1086 JW1072"
---

# rluC

`protein.P0AA39`

## Static

- Type: `protein`
- Source: `UniProt:P0AA39`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Responsible for synthesis of pseudouridine from uracil at positions 955, 2504 and 2580 in 23S ribosomal RNA. {ECO:0000269|PubMed:9660827}. RluC catalyzes pseudouridylation of nucleotides U955, U2504, and U2580 in 23S rRNA; all three sites are located near the peptidyl transferase center of the ribosome . RluC also shows activity toward 16S rRNA in vitro . RluC associates with a pre-50S ribosomal particle . A proteolytic fragment consisting of amino acids 89-319 is catalytically active . The crystal structure of the C-terminal catalytic domain has been determined at 2 Å resolution . An rluC mutant lacks pseudouridylation of nucleotides U955, U2504, and U2580 in 23S rRNA, but does not exhibit an obvious growth defect . It was later shown that an rluC mutant shows some cold sensitivity . Insertion mutations in rluC suppress the cold-sensitive growth phenotype of a bipA deletion mutant . Inactivation of rluC leads to increased susceptibility to antibiotics that target the peptidyl transferase center, such as clindamycin, linezolid, and tiamulin . A ΔrlmE ΔrluC double mutant exhibited a 20°C conditional lethal phenotype but was permissive at 37°C; a lower tripeptide synthesis rate compared to the single mutations was also observed...

## Biological Role

Catalyzes RXN-11838 (reaction.ecocyc.RXN-11838).

## Annotation

FUNCTION: Responsible for synthesis of pseudouridine from uracil at positions 955, 2504 and 2580 in 23S ribosomal RNA. {ECO:0000269|PubMed:9660827}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-11838|reaction.ecocyc.RXN-11838]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1086|gene.b1086]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AA39`
- `KEGG:ecj:JW1072;eco:b1086;ecoc:C3026_06575;`
- `GeneID:75171210;75203672;945637;`
- `GO:GO:0000455; GO:0003723; GO:0005829; GO:0009982; GO:0120159; GO:0160141`
- `EC:5.4.99.24`

## Notes

Ribosomal large subunit pseudouridine synthase C (EC 5.4.99.24) (23S rRNA pseudouridine(955/2504/2580) synthase) (rRNA pseudouridylate synthase C) (rRNA-uridine isomerase C)
