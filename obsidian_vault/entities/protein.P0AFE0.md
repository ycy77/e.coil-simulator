---
entity_id: "protein.P0AFE0"
entity_type: "protein"
name: "nuoJ"
source_database: "UniProt"
source_id: "P0AFE0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nuoJ b2280 JW2275"
---

# nuoJ

`protein.P0AFE0`

## Static

- Type: `protein`
- Source: `UniProt:P0AFE0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: NDH-1 shuttles electrons from NADH, via FMN and iron-sulfur (Fe-S) centers, to quinones in the respiratory chain. The immediate electron acceptor for the enzyme in this species is believed to be ubiquinone. Couples the redox reaction to proton translocation (for every two electrons transferred, four hydrogen ions are translocated across the cytoplasmic membrane), and thus conserves the redox energy in a proton gradient. NuoJ is part of the inner membrane component of NADH dehydrogenase I . The protein has five predicted transmembrane domains; the C terminus is located in the cytoplasm . A crystal structure of the membrane component at higher resolution has allowed better identification of the interactions between the subunits . Point mutations at conserved residues have been analyzed; mutation of Val65, which is located in the most conserved transmembrane segment, causes significant reduction of coupled electron transfer activity . Among other site-directed mutants, a V65G mutation had the most deleterious effect on growth on malate and on enzymatic activity . In the presence of NADH, crosslinking between NuoA and NuoJ in the intact Complex I is abolished, indicating that the conformational change involving the hydrophilic subunits in the presence of NADH extends to the membrane domain...

## Biological Role

Catalyzes NADH:ubiquinone oxidoreductase (reaction.R11945). Component of NADH:quinone oxidoreductase I (complex.ecocyc.NADH-DHI-CPLX).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: NDH-1 shuttles electrons from NADH, via FMN and iron-sulfur (Fe-S) centers, to quinones in the respiratory chain. The immediate electron acceptor for the enzyme in this species is believed to be ubiquinone. Couples the redox reaction to proton translocation (for every two electrons transferred, four hydrogen ions are translocated across the cytoplasmic membrane), and thus conserves the redox energy in a proton gradient.

## Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R11945|reaction.R11945]] `KEGG` `database` - via EC:7.1.1.2
- `is_component_of` --> [[complex.ecocyc.NADH-DHI-CPLX|complex.ecocyc.NADH-DHI-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2280|gene.b2280]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFE0`
- `KEGG:ecj:JW2275;eco:b2280;ecoc:C3026_12725;`
- `GeneID:86947217;93774894;946756;`
- `GO:GO:0005886; GO:0008137; GO:0016020; GO:0022904; GO:0030964; GO:0045271; GO:0048038`
- `EC:7.1.1.-`

## Notes

NADH-quinone oxidoreductase subunit J (EC 7.1.1.-) (NADH dehydrogenase I subunit J) (NDH-1 subunit J) (NUO10)
