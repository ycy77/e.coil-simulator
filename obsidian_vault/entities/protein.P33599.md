---
entity_id: "protein.P33599"
entity_type: "protein"
name: "nuoC"
source_database: "UniProt"
source_id: "P33599"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:16079137}. Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01359, ECO:0000269|PubMed:16079137}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01359, ECO:0000269|PubMed:16079137}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nuoC nuoCD nuoD b2286 JW5375"
---

# nuoC

`protein.P33599`

## Static

- Type: `protein`
- Source: `UniProt:P33599`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:16079137}. Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01359, ECO:0000269|PubMed:16079137}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01359, ECO:0000269|PubMed:16079137}.

## Enriched Summary

FUNCTION: NDH-1 shuttles electrons from NADH, via FMN and iron-sulfur (Fe-S) centers, to quinones in the respiratory chain. The immediate electron acceptor for the enzyme in this species is believed to be ubiquinone. Couples the redox reaction to proton translocation (for every two electrons transferred, four hydrogen ions are translocated across the cytoplasmic membrane), and thus conserves the redox energy in a proton gradient. NuoCD is part of the connecting fragment within the peripheral arm of NADH:ubiquinone oxidoreductase I (NDH-1). Unlike in other bacteria, which contain two separate genes encoding the NuoC and NuoD subunits, the nuoC gene of E. coli K-12 encodes a fused version of these subunits . NuoCD is the only subunit of the peripheral arm that does not contain a cofactor. This subunit was predicted to function as the proton channel . NuoCD interacts with FliG and FliM, components of the flagellar switch-motor complex . Mutagenesis of two conserved histidine residues, H224 and H228, only has a modest effect on ubiquinone reductase activity of NDH-1. An R274A mutant leads to a significant loss of signal from the N2 4Fe-4S cluster as well as from a second fast-relaxing 4Fe-4S cluster...

## Biological Role

Catalyzes NADH:ubiquinone oxidoreductase (reaction.R11945). Component of NADH:quinone oxidoreductase I, peripheral arm (complex.ecocyc.CPLX0-3361), NADH:quinone oxidoreductase I (complex.ecocyc.NADH-DHI-CPLX).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: NDH-1 shuttles electrons from NADH, via FMN and iron-sulfur (Fe-S) centers, to quinones in the respiratory chain. The immediate electron acceptor for the enzyme in this species is believed to be ubiquinone. Couples the redox reaction to proton translocation (for every two electrons transferred, four hydrogen ions are translocated across the cytoplasmic membrane), and thus conserves the redox energy in a proton gradient.

## Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R11945|reaction.R11945]] `KEGG` `database` - via EC:7.1.1.2
- `is_component_of` --> [[complex.ecocyc.CPLX0-3361|complex.ecocyc.CPLX0-3361]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.NADH-DHI-CPLX|complex.ecocyc.NADH-DHI-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2286|gene.b2286]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33599`
- `KEGG:ecj:JW5375;eco:b2286;ecoc:C3026_12755;`
- `GeneID:946759;`
- `GO:GO:0005737; GO:0005886; GO:0008137; GO:0016020; GO:0022904; GO:0030964; GO:0045271; GO:0048038; GO:0050136; GO:0051287`
- `EC:7.1.1.-`

## Notes

NADH-quinone oxidoreductase subunit C/D (EC 7.1.1.-) (NADH dehydrogenase I subunit C/D) (NDH-1 subunit C/D) (NUO3/NUO4)
