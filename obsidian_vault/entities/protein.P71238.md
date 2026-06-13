---
entity_id: "protein.P71238"
entity_type: "protein"
name: "wcaD"
source_database: "UniProt"
source_id: "P71238"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "wcaD b2056 JW2041"
---

# wcaD

`protein.P71238`

## Static

- Type: `protein`
- Source: `UniProt:P71238`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}.

## Enriched Summary

Putative colanic acid polymerase wcaD is located within a cluster of genes that are responsible for production of the extracellular polysaccharide, CPD-21504 "colanic acid" (CA); WcaD is predicted to be an integral inner membrane protein and it may have a role in polymerising the CA hexasaccharide unit . A ΔwcaD mutant of an rcsA overexpressing, CA producing strain of E. coli K-12 MG1655 grows as misshapen rods and spheres and accumulates the pyruvylated hexasaccharide CPD-21522 repeat unit of CA; further deletion of EG11424 waaL, encoding O-antigen ligase, in this strain results in extensive cell lysis . The Keio collection wcaD mutant is sensitive to lithium (<90% growth at 200mM Li) .

## Biological Role

Catalyzes RXN-22213 (reaction.ecocyc.RXN-22213).

## Annotation

Putative colanic acid polymerase

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-22213|reaction.ecocyc.RXN-22213]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2056|gene.b2056]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P71238`
- `KEGG:ecj:JW2041;eco:b2056;ecoc:C3026_11570;`
- `GeneID:75203919;946550;`
- `GO:GO:0005886; GO:0009103; GO:0045228; GO:0046377`

## Notes

Putative colanic acid polymerase
