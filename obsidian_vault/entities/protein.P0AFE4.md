---
entity_id: "protein.P0AFE4"
entity_type: "protein"
name: "nuoK"
source_database: "UniProt"
source_id: "P0AFE4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nuoK b2279 JW2274"
---

# nuoK

`protein.P0AFE4`

## Static

- Type: `protein`
- Source: `UniProt:P0AFE4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: NDH-1 shuttles electrons from NADH, via FMN and iron-sulfur (Fe-S) centers, to quinones in the respiratory chain. The immediate electron acceptor for the enzyme in this species is believed to be ubiquinone. Couples the redox reaction to proton translocation (for every two electrons transferred, four hydrogen ions are translocated across the cytoplasmic membrane), and thus conserves the redox energy in a proton gradient.; FUNCTION: There are 2 NADH dehydrogenases in E.coli, however only this complex is able to use dNADH (reduced nicotinamide hypoxanthine dinucleotide, deamino-NADH) and dNADH-DB (dimethoxy-5-methyl-6-decyl-1,4-benzoquinone) as substrates. NuoK is part of the inner membrane component of NADH dehydrogenase I . The protein has three predicted transmembrane domains; the C terminus is located in the cytoplasm . A crystal structure of the membrane component at higher resolution has allowed better identification of the interactions between the subunits . NuoK participates in proton translocation . The SecYEG protein secretion machinery and its YidC component are required for insertion of NuoK in the cytoplasmic membrane. The YidC requirement is due to the presence of two conserved glutamate residues (Glu36, Glu72) in transmembrane segments of NuoK . Both of these membrane-embedded acidic residues are required for high rates of ubiquinone reduction...

## Biological Role

Catalyzes NADH:ubiquinone oxidoreductase (reaction.R11945). Component of NADH:quinone oxidoreductase I (complex.ecocyc.NADH-DHI-CPLX).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: NDH-1 shuttles electrons from NADH, via FMN and iron-sulfur (Fe-S) centers, to quinones in the respiratory chain. The immediate electron acceptor for the enzyme in this species is believed to be ubiquinone. Couples the redox reaction to proton translocation (for every two electrons transferred, four hydrogen ions are translocated across the cytoplasmic membrane), and thus conserves the redox energy in a proton gradient.; FUNCTION: There are 2 NADH dehydrogenases in E.coli, however only this complex is able to use dNADH (reduced nicotinamide hypoxanthine dinucleotide, deamino-NADH) and dNADH-DB (dimethoxy-5-methyl-6-decyl-1,4-benzoquinone) as substrates.

## Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R11945|reaction.R11945]] `KEGG` `database` - via EC:7.1.1.2
- `is_component_of` --> [[complex.ecocyc.NADH-DHI-CPLX|complex.ecocyc.NADH-DHI-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2279|gene.b2279]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFE4`
- `KEGG:ecj:JW2274;eco:b2279;ecoc:C3026_12720;`
- `GeneID:86860442;93033872;947580;`
- `GO:GO:0005886; GO:0008137; GO:0016020; GO:0022904; GO:0030964; GO:0042773; GO:0045271; GO:0048038; GO:0050136`
- `EC:7.1.1.-`

## Notes

NADH-quinone oxidoreductase subunit K (EC 7.1.1.-) (NADH dehydrogenase I subunit K) (NDH-1 subunit K) (NUO11)
