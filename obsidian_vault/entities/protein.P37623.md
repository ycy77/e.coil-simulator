---
entity_id: "protein.P37623"
entity_type: "protein"
name: "acpT"
source_database: "UniProt"
source_id: "P37623"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "acpT yhhU b3475 JW3440"
---

# acpT

`protein.P37623`

## Static

- Type: `protein`
- Source: `UniProt:P37623`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: May be involved in an alternative pathway for phosphopantetheinyl transfer and holo-ACP synthesis in E.coli. The native apo-protein substrate is unknown. Is able to functionally replace AcpS in vivo but only when expressed at high levels. {ECO:0000269|PubMed:10625633, ECO:0000269|PubMed:8939709}. The carrier protein substrates of AcpT have been identified in E. coli O157:H7 strain EDL933 as Z4853 and Z4854, two proteins in O-island 138 which appears to contain genes for fatty-acid biosynthesis . O-island 138 has been deleted from a K-12 ancestor, but acpT has been retained possibly because AcpT allows slow growth in the absence of AcpS activity . Overexpression of acpT suppresses an acpS mutation . Overexpression of acpT also suppresses the lethality of yejM null mutants, as well as the temperature sensitivity of yejMG570A mutants . This suppression does not require phosphopantetheinyl transferase activity because a mutant lacking this activity was still able to suppress the temperature sensitivity of the yejMG570A mutant .

## Biological Role

Catalyzes HOLO-ACP-SYNTH-RXN (reaction.ecocyc.HOLO-ACP-SYNTH-RXN).

## Enriched Pathways

- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: May be involved in an alternative pathway for phosphopantetheinyl transfer and holo-ACP synthesis in E.coli. The native apo-protein substrate is unknown. Is able to functionally replace AcpS in vivo but only when expressed at high levels. {ECO:0000269|PubMed:10625633, ECO:0000269|PubMed:8939709}.

## Pathways

- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.HOLO-ACP-SYNTH-RXN|reaction.ecocyc.HOLO-ACP-SYNTH-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3475|gene.b3475]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37623`
- `KEGG:ecj:JW3440;eco:b3475;ecoc:C3026_18820;`
- `GeneID:947979;`
- `GO:GO:0000287; GO:0005829; GO:0006633; GO:0008897; GO:0019878`
- `EC:2.7.8.7`

## Notes

4'-phosphopantetheinyl transferase AcpT (EC 2.7.8.7)
