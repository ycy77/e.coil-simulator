---
entity_id: "protein.P24077"
entity_type: "protein"
name: "entS"
source_database: "UniProt"
source_id: "P24077"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01436, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01436}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "entS ybdA b0591 JW0583"
---

# entS

`protein.P24077`

## Static

- Type: `protein`
- Source: `UniProt:P24077`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01436, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01436}.

## Enriched Summary

FUNCTION: Component of an export pathway for enterobactin (PubMed:12068807). Overexpression reduces intracellular arabinose concentrations (PubMed:22952739). {ECO:0000269|PubMed:12068807, ECO:0000269|PubMed:22952739}. The EntS protein is a member of the major facilitator superfamily (MFS) of transporters . Based on sequence similarity, it functions as a proton-driven efflux system. Siderophore nutrition assays have shown that an entS mutant is unable to export enterobactin efficiently to alleviate iron deprivation , though some export does still occur through another mechanism. entS was identified in a screen for genes that reduce the lethal effects of stress; an entS insertion mutant is more sensitive than wild type to mitomycin C and other stresses . EntS has been implicated in arabinose efflux .

## Biological Role

Catalyzes enterobactin export (reaction.ecocyc.TRANS-RXN0-496). Transports Enterochelin (molecule.C05821), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Component of an export pathway for enterobactin (PubMed:12068807). Overexpression reduces intracellular arabinose concentrations (PubMed:22952739). {ECO:0000269|PubMed:12068807, ECO:0000269|PubMed:22952739}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-496|reaction.ecocyc.TRANS-RXN0-496]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C05821|molecule.C05821]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b0591|gene.b0591]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P24077`
- `KEGG:ecj:JW0583;eco:b0591;ecoc:C3026_02950;`
- `GeneID:946268;`
- `GO:GO:0005886; GO:0006974; GO:0015562; GO:0042930; GO:0042931; GO:0046677`

## Notes

Enterobactin exporter EntS (Protein p43)
