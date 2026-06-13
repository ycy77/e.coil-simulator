---
entity_id: "protein.P0AE52"
entity_type: "protein"
name: "bcp"
source_database: "UniProt"
source_id: "P0AE52"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "bcp b2480 JW2465"
---

# bcp

`protein.P0AE52`

## Static

- Type: `protein`
- Source: `UniProt:P0AE52`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Thiol-specific peroxidase that catalyzes the reduction of hydrogen peroxide and organic hydroperoxides to water and alcohols, respectively. Plays a role in cell protection against oxidative stress by detoxifying peroxides and as sensor of hydrogen peroxide-mediated signaling events. {ECO:0000269|PubMed:21910476}. Bcp is a RED-THIOREDOXIN-MONOMER-dependent thiol peroxidase that belongs to the family of atypical 2-Cys peroxidases . The enzyme can utilize a variety of peroxides and reducing substrates, including Trx1, Trx2, Grx1, and Grx3. The redox potential of Bcp is very high, at -145.9 mV . The reaction mechanism has been investigated. Utilizing an atypical two-cysteine peroxiredoxin pathway, a sulfenic acid is transiently formed on Cys45, followed by formation of an intramolecular disulfide bond between Cys45 and Cys50. This oxidized form of Bcp is a substrate for reduction by thioredoxin. In a C50S mutant, the sulfenic acid intermediate is resolved by formation of an intermolecular disulfide bond . Both the oxidized and the reduced form of the Bcp protein is monomeric in solution . A Cys45 mutant loses all catalytic activity. A bcp insertion mutant grows slower than wild type and is hypersensitive to peroxides. Expression of bcp is induced by oxidative stress . Bcp: "bacterioferritin comigratory protein" Reviews:

## Biological Role

Catalyzes 1.11.1.15-RXN (reaction.ecocyc.1.11.1.15-RXN).

## Annotation

FUNCTION: Thiol-specific peroxidase that catalyzes the reduction of hydrogen peroxide and organic hydroperoxides to water and alcohols, respectively. Plays a role in cell protection against oxidative stress by detoxifying peroxides and as sensor of hydrogen peroxide-mediated signaling events. {ECO:0000269|PubMed:21910476}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.1.11.1.15-RXN|reaction.ecocyc.1.11.1.15-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2480|gene.b2480]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AE52`
- `KEGG:ecj:JW2465;eco:b2480;ecoc:C3026_13765;`
- `GeneID:89517289;93774658;946949;`
- `GO:GO:0005737; GO:0005829; GO:0006979; GO:0008379; GO:0032843; GO:0034599; GO:0045454`
- `EC:1.11.1.24`

## Notes

Peroxiredoxin Bcp (EC 1.11.1.24) (Bacterioferritin comigratory protein) (Thioredoxin peroxidase) (Thioredoxin-dependent peroxiredoxin Bcp)
