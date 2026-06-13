---
entity_id: "protein.P0AAI9"
entity_type: "protein"
name: "fabD"
source_database: "UniProt"
source_id: "P0AAI9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fabD tfpA b1092 JW1078"
---

# fabD

`protein.P0AAI9`

## Static

- Type: `protein`
- Source: `UniProt:P0AAI9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Malonyl CoA-acyl carrier protein transacylase (MCT) (EC 2.3.1.39) Malonyl-CoA-acyl carrier protein transacylase (FabD) catalyzes the first committed step in the initiation of fatty acid biosynthesis, the transfer of the malonyl group from malonyl-CoA to acyl carrier protein (ACP) to form malonyl-ACP. Initial biochemical studies were performed on the enzyme purified from E. coli B . These studies showed that a malonyl-enzyme intermediate is formed during the reaction . The reaction utilizes a ping-pong bi bi mechanism . Crystal structures of FabD alone and in various binary complexes have been solved . In a crystal structure obtained after soaking in the substrate malonyl-CoA, its thioester bond has been cleaved, and the malonyl moiety is covalently bound to the active-site Ser92 residue via an oxo-ester bond. A detailed reaction mechanism has been described . Arg117 is an active site residue that interacts with the carboxylate of the malonyl-FabD reaction intermediate . An R117A variant of FabD has reduced substrate specificity and is able to synthesize a variety of ACP-linked products including acetyl-ACP, succinyl-ACP, isobutyryl-ACP, 2-butenoyl-ACP, and β-hydroxybutyryl-ACP . A temperature-sensitive mutant has been characterized . The fabD89 allele was found to produce an inactive enzyme that is truncated at codon 257 due to an amber mutation...

## Biological Role

Catalyzes MALONYL-COA-ACP-TRANSACYL-RXN (reaction.ecocyc.MALONYL-COA-ACP-TRANSACYL-RXN).

## Enriched Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00074` Mycolic acid biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)

## Annotation

Malonyl CoA-acyl carrier protein transacylase (MCT) (EC 2.3.1.39)

## Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00074` Mycolic acid biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.MALONYL-COA-ACP-TRANSACYL-RXN|reaction.ecocyc.MALONYL-COA-ACP-TRANSACYL-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1092|gene.b1092]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAI9`
- `KEGG:ecj:JW1078;eco:b1092;ecoc:C3026_06605;`
- `GeneID:75171216;75203678;945766;`
- `GO:GO:0004314; GO:0005829; GO:0006633`
- `EC:2.3.1.39`

## Notes

Malonyl CoA-acyl carrier protein transacylase (MCT) (EC 2.3.1.39)
