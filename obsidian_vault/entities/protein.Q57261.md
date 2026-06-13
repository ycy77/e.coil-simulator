---
entity_id: "protein.Q57261"
entity_type: "protein"
name: "truD"
source_database: "UniProt"
source_id: "Q57261"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "truD ygbO b2745 JW2715"
---

# truD

`protein.Q57261`

## Static

- Type: `protein`
- Source: `UniProt:Q57261`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Responsible for synthesis of pseudouridine from uracil-13 in transfer RNAs. {ECO:0000269|PubMed:12756329}. TruD is responsible for biosynthesis of the pseudouridine13 modification of tRNA(Glu) . TruD is a member of a widely conserved fifth family of pseudouridine synthases that is unrelated to any previously characterized pseudouridine synthases . Crystal structures of TruD have been solved . The enzyme has an overall V-shaped structure; one arm is structurally similar to the catalytic domain of other pseudouridine synthases, while the other arm has a novel fold and has been named the TRUD domain . The conserved Glu31 residue may act as the general base for proton abstraction . A truD mutant lacks the pseudouridine13 modification at tRNA(Glu), but shows no growth defect . The conserved Asp80 is required for catalysis . Reviews:

## Biological Role

Catalyzes RXN-11841 (reaction.ecocyc.RXN-11841).

## Annotation

FUNCTION: Responsible for synthesis of pseudouridine from uracil-13 in transfer RNAs. {ECO:0000269|PubMed:12756329}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-11841|reaction.ecocyc.RXN-11841]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2745|gene.b2745]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q57261`
- `KEGG:ecj:JW2715;eco:b2745;ecoc:C3026_15095;`
- `GeneID:75205606;947214;`
- `GO:GO:0001522; GO:0003723; GO:0005829; GO:0009982; GO:0031119; GO:0106029; GO:0160150`
- `EC:5.4.99.27`

## Notes

tRNA pseudouridine synthase D (EC 5.4.99.27) (tRNA pseudouridine(13) synthase) (tRNA pseudouridylate synthase D) (tRNA-uridine isomerase D)
