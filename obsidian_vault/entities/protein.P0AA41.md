---
entity_id: "protein.P0AA41"
entity_type: "protein"
name: "truC"
source_database: "UniProt"
source_id: "P0AA41"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "truC yqcB b2791 JW2762"
---

# truC

`protein.P0AA41`

## Static

- Type: `protein`
- Source: `UniProt:P0AA41`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Responsible for synthesis of pseudouridine from uracil-65 in transfer RNAs. {ECO:0000269|PubMed:11720289}. TruC is the pseudouridine synthase that catalyzes formation of pseudouridine at position 65 in tRNAIle1 and tRNAAsp. TruC belongs to the RluA family of RNA pseudouridine synthases . A truC null mutant exhibits no obvious growth defect. The conserved active site residue Asp54 is essential for activity . Reviews:

## Biological Role

Catalyzes RXN-11840 (reaction.ecocyc.RXN-11840).

## Annotation

FUNCTION: Responsible for synthesis of pseudouridine from uracil-65 in transfer RNAs. {ECO:0000269|PubMed:11720289}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-11840|reaction.ecocyc.RXN-11840]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2791|gene.b2791]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AA41`
- `KEGG:ecj:JW2762;eco:b2791;ecoc:C3026_15345;`
- `GeneID:86860878;93779207;947242;`
- `GO:GO:0000455; GO:0003723; GO:0005829; GO:0006399; GO:0008033; GO:0009451; GO:0009982; GO:0031119; GO:0106029; GO:0160149`
- `EC:5.4.99.26`

## Notes

tRNA pseudouridine synthase C (EC 5.4.99.26) (tRNA pseudouridine(65) synthase) (tRNA pseudouridylate synthase C) (tRNA-uridine isomerase C)
