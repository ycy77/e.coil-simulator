---
entity_id: "protein.P76514"
entity_type: "protein"
name: "yfdR"
source_database: "UniProt"
source_id: "P76514"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yfdR b2361 JW2358"
---

# yfdR

`protein.P76514`

## Static

- Type: `protein`
- Source: `UniProt:P76514`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Uncharacterized protein YfdR YfdR is a deoxyribonucleoside 5'-monophosphate phosphatase with a conserved HD domain. The enzyme has a broader substrate range than YfbR . YfdR was found to interact with DnaA . The genomic region comprising yfdQRST was found to act as a multicopy suppressor of the hda-185 ΔsfiA mutation. A ΔyfdQRST deletion mutant has no obvious growth defect .

## Biological Role

Catalyzes RXN0-3741 (reaction.ecocyc.RXN0-3741). Bound by Cobalt ion (molecule.C00175).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

Uncharacterized protein YfdR

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-3741|reaction.ecocyc.RXN0-3741]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2361|gene.b2361]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76514`
- `KEGG:ecj:JW2358;eco:b2361;ecoc:C3026_13130;`
- `GeneID:946834;`
- `GO:GO:0002953; GO:0050897`

## Notes

Uncharacterized protein YfdR
