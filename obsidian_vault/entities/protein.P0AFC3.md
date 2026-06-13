---
entity_id: "protein.P0AFC3"
entity_type: "protein"
name: "nuoA"
source_database: "UniProt"
source_id: "P0AFC3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01394, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01394, ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nuoA b2288 JW2283"
---

# nuoA

`protein.P0AFC3`

## Static

- Type: `protein`
- Source: `UniProt:P0AFC3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01394, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01394, ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: NDH-1 shuttles electrons from NADH, via FMN and iron-sulfur (Fe-S) centers, to quinones in the respiratory chain. The immediate electron acceptor for the enzyme in this species is believed to be ubiquinone. Couples the redox reaction to proton translocation (for every two electrons transferred, four hydrogen ions are translocated across the cytoplasmic membrane), and thus conserves the redox energy in a proton gradient. NuoA is part of the inner membrane component of NADH dehydrogenase I . The protein has three predicted transmembrane domains , and the C terminus is located in the cytoplasm . Site-specific mutagenesis of conserved charged amino acid residues has elucidated possible functional roles for Asp79 and Glu81 . A crystal structure of the membrane component at higher resolution has allowed better identification of the interactions between the subunits . In the presence of NADH, crosslinking between NuoA and NuoJ in the intact Complex I is abolished, indicating that the conformational change involving the hydrophilic subunits in the presence of NADH extends to the membrane domain . Null mutants of all individual nuo genes have a growth defect under aerobic conditions in rich medium . NuoA: "NADH:ubiquinone oxidoreductase"

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

- `encodes` <-- [[gene.b2288|gene.b2288]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFC3`
- `KEGG:ecj:JW2283;eco:b2288;ecoc:C3026_12765;`
- `GeneID:89517123;93774886;946764;`
- `GO:GO:0005886; GO:0008137; GO:0016020; GO:0022904; GO:0030964; GO:0045271; GO:0048038; GO:0050136`
- `EC:7.1.1.-`

## Notes

NADH-quinone oxidoreductase subunit A (EC 7.1.1.-) (NADH dehydrogenase I subunit A) (NDH-1 subunit A) (NUO1)
