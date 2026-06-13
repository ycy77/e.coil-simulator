---
entity_id: "protein.P76104"
entity_type: "protein"
name: "rlhA"
source_database: "UniProt"
source_id: "P76104"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rlhA ydcP b1435 JW1431"
---

# rlhA

`protein.P76104`

## Static

- Type: `protein`
- Source: `UniProt:P76104`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Responsible for the formation of the 5-hydroxycytidine modification at the C2501 position (ho5C2501) of 23S rRNA. May be a Fe-S protein that catalyzes ho5C2501 formation using prephenate as a hydroxyl group donor. {ECO:0000269|PubMed:29069499}. RlhA is the enzyme responsible for generating the 5-hydroxycytidine modification at the C2501 position (ho5C2501) of 23S rRNA. In addition to RlhA, prephenate biosynthesis and iron-sulfur cluster biogenesis proteins are required for generating the ho5C2501 modification . RlhA co-fractionates with the 30S subunit of the ribosome in a sucrose gradient, similar to other 23S rRNA-modifying enzymes . A ΔrlhA mutant strain completely lacks the ho5C2501 modification of 23S rRNA. Mutations in the conserved cysteine residues 169, 176, 580 and 611 abolish the activity of RlhA . RlhA: "large subunit ribosomal RNA hydroxylation A"

## Biological Role

Catalyzes RXN-21990 (reaction.ecocyc.RXN-21990).

## Annotation

FUNCTION: Responsible for the formation of the 5-hydroxycytidine modification at the C2501 position (ho5C2501) of 23S rRNA. May be a Fe-S protein that catalyzes ho5C2501 formation using prephenate as a hydroxyl group donor. {ECO:0000269|PubMed:29069499}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-21990|reaction.ecocyc.RXN-21990]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1435|gene.b1435]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76104`
- `KEGG:ecj:JW1431;eco:b1435;ecoc:C3026_08355;`
- `GeneID:945993;`
- `GO:GO:0000154`

## Notes

23S rRNA 5-hydroxycytidine C2501 synthase (Large subunit ribosomal RNA hydroxylation A)
