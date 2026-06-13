---
entity_id: "protein.P21693"
entity_type: "protein"
name: "dbpA"
source_database: "UniProt"
source_id: "P21693"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dbpA b1343 JW1337"
---

# dbpA

`protein.P21693`

## Static

- Type: `protein`
- Source: `UniProt:P21693`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: DEAD-box RNA helicase involved in the assembly of the 50S ribosomal subunit. Has an RNA-dependent ATPase activity, which is specific for 23S rRNA, and a 3' to 5' RNA helicase activity that uses the energy of ATP hydrolysis to destabilize and unwind short rRNA duplexes. Requires a single-stranded RNA loading site on the 3' side of the substrate helix. {ECO:0000255|HAMAP-Rule:MF_00965, ECO:0000269|PubMed:11350034, ECO:0000269|PubMed:11574482, ECO:0000269|PubMed:15910005, ECO:0000269|PubMed:18237742, ECO:0000269|PubMed:19734347, ECO:0000269|PubMed:20160110, ECO:0000269|PubMed:8253085, ECO:0000269|PubMed:9016593, ECO:0000269|PubMed:9836593}. DbpA is a 3'->5' RNA helicase that plays a role in the late stage of biogenesis of the 50S subunit of the ribosome . DbpA interacts with 23S rRNA and exhibits RNA-dependent ATPase activity that shows specificity for 23S rRNA molecules that are not incorporated within the ribosome . Footprinting of DbpA protein on a fragment of 23S rRNA indicates binding at multiple sites , but the primary binding site appears to be hairpin 92 of the 23S rRNA, which is part of the peptidyltransferase center of the ribosome . A dominant negative R331A active site mutant accumulates an incompletely assembled 45S particle which can stimulate the ATPase activity of wild-type DbpA...

## Biological Role

Catalyzes RXN-24177 (reaction.ecocyc.RXN-24177).

## Annotation

FUNCTION: DEAD-box RNA helicase involved in the assembly of the 50S ribosomal subunit. Has an RNA-dependent ATPase activity, which is specific for 23S rRNA, and a 3' to 5' RNA helicase activity that uses the energy of ATP hydrolysis to destabilize and unwind short rRNA duplexes. Requires a single-stranded RNA loading site on the 3' side of the substrate helix. {ECO:0000255|HAMAP-Rule:MF_00965, ECO:0000269|PubMed:11350034, ECO:0000269|PubMed:11574482, ECO:0000269|PubMed:15910005, ECO:0000269|PubMed:18237742, ECO:0000269|PubMed:19734347, ECO:0000269|PubMed:20160110, ECO:0000269|PubMed:8253085, ECO:0000269|PubMed:9016593, ECO:0000269|PubMed:9836593}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-24177|reaction.ecocyc.RXN-24177]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1343|gene.b1343]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P21693`
- `KEGG:ecj:JW1337;eco:b1343;ecoc:C3026_07870;`
- `GeneID:947153;`
- `GO:GO:0000027; GO:0003724; GO:0005524; GO:0005829; GO:0016887; GO:0019843; GO:0033677; GO:0034458; GO:0043531`
- `EC:3.6.4.13`

## Notes

ATP-dependent RNA helicase DbpA (EC 3.6.4.13)
