---
entity_id: "protein.P33232"
entity_type: "protein"
name: "lldD"
source_database: "UniProt"
source_id: "P33232"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01559, ECO:0000269|PubMed:18473}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01559, ECO:0000269|PubMed:18473}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lldD lctD b3605 JW3580"
---

# lldD

`protein.P33232`

## Static

- Type: `protein`
- Source: `UniProt:P33232`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01559, ECO:0000269|PubMed:18473}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01559, ECO:0000269|PubMed:18473}.

## Enriched Summary

FUNCTION: Catalyzes the conversion of L-lactate to pyruvate. Seems to be a primary dehydrogenase in the respiratory chain. To a lesser extent, can also oxidize DL-alpha-hydroxybutyrate, but not D-lactate. {ECO:0000269|PubMed:18473, ECO:0000269|PubMed:8407843}. L-lactate dehydrogenase is an FMN-dependent membrane-associated dehydrogenase . It functions in aerobic respiration and also has a role in anaerobic nitrate respiration . L-lactate dehydrogenase is associated with the inner membrane . LldD is one of three lactate dehydrogenase enzymes which interconvert pyruvate and lactate in E. coli. The other two enzymes are specific for D-lactate: the soluble DLACTDEHYDROGNAD-MONOMER "LdhA", an NAD-linked fermentative enzyme, and DLACTDEHYDROGFAD-MONOMER "Dld", a membrane-associated respiratory enzyme. L-lactate dehydrogenase is induced by aerobic growth on L-lactate and L-fucose and in the presence of lactate under nitrate, fumarate and TMAO respiration conditions . Repression of lldD expression under anaerobic conditions is mediated by ArcA . An lldD insertion mutant has lost the ability to grow on L-lactate as the sole source of carbon and energy, but can still utilize D-lactate .

## Biological Role

Catalyzes (S)-lactate:ferricytochrome-c 2-oxidoreductase (reaction.R00196), lactate oxidation (reaction.ecocyc.L-LACTDEHYDROGFMN-RXN), RXN0-7227 (reaction.ecocyc.RXN0-7227). Bound by FMN (molecule.C00061).

## Enriched Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the conversion of L-lactate to pyruvate. Seems to be a primary dehydrogenase in the respiratory chain. To a lesser extent, can also oxidize DL-alpha-hydroxybutyrate, but not D-lactate. {ECO:0000269|PubMed:18473, ECO:0000269|PubMed:8407843}.

## Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00196|reaction.R00196]] `KEGG` `database` - via EC:1.1.2.3
- `catalyzes` --> [[reaction.ecocyc.L-LACTDEHYDROGFMN-RXN|reaction.ecocyc.L-LACTDEHYDROGFMN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7227|reaction.ecocyc.RXN0-7227]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00061|molecule.C00061]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3605|gene.b3605]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33232`
- `KEGG:ecj:JW3580;eco:b3605;ecoc:C3026_19550;`
- `GeneID:948121;`
- `GO:GO:0004459; GO:0005886; GO:0006089; GO:0009060; GO:0010181; GO:0042355`
- `EC:1.1.-.-`

## Notes

L-lactate dehydrogenase (EC 1.1.-.-)
