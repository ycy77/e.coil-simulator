---
entity_id: "protein.P0AFF0"
entity_type: "protein"
name: "nuoN"
source_database: "UniProt"
source_id: "P0AFF0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nuoN b2276 JW2271"
---

# nuoN

`protein.P0AFF0`

## Static

- Type: `protein`
- Source: `UniProt:P0AFF0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: NDH-1 shuttles electrons from NADH, via FMN and iron-sulfur (Fe-S) centers, to quinones in the respiratory chain. The immediate electron acceptor for the enzyme in this species is believed to be ubiquinone. Couples the redox reaction to proton translocation (for every two electrons transferred, four hydrogen ions are translocated across the cytoplasmic membrane), and thus conserves the redox energy in a proton gradient. NuoN is part of the inner membrane component of NADH dehydrogenase I . The protein has 14 transmembrane helices . The transmembrane topology of NuoN has been investigated, supporting data from the crystal structure and indicating that both the N and C terminus are located in the periplasm . Transmembrane helices were assigned to locations in the crystal structure using Fourier transform analysis . A crystal structure of the membrane component at higher resolution has allowed better identification of the unusual arrangement of the transmembrane helices . This subunit may function in proton translocation . Site-directed mutagenesis has identified residues important for dNADH oxidase activity, proton translocation, and interaction with quinones . NuoM and NuoN share a pattern of conserved residues; predictions of membrane topology indicate that conserved Lys residues are located in a transmembrane helix and suggest a proton translocation mechanism...

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

- `encodes` <-- [[gene.b2276|gene.b2276]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFF0`
- `KEGG:ecj:JW2271;eco:b2276;ecoc:C3026_12705;`
- `GeneID:75172404;75205678;945136;`
- `GO:GO:0005886; GO:0008137; GO:0009060; GO:0015990; GO:0016020; GO:0022904; GO:0030964; GO:0042773; GO:0045271; GO:0048038; GO:0050136`
- `EC:7.1.1.-`

## Notes

NADH-quinone oxidoreductase subunit N (EC 7.1.1.-) (NADH dehydrogenase I subunit N) (NDH-1 subunit N) (NUO14)
