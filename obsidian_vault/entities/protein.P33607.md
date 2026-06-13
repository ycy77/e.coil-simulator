---
entity_id: "protein.P33607"
entity_type: "protein"
name: "nuoL"
source_database: "UniProt"
source_id: "P33607"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nuoL b2278 JW2273"
---

# nuoL

`protein.P33607`

## Static

- Type: `protein`
- Source: `UniProt:P33607`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: NDH-1 shuttles electrons from NADH, via FMN and iron-sulfur (Fe-S) centers, to quinones in the respiratory chain. The immediate electron acceptor for the enzyme in this species is believed to be ubiquinone. Couples the redox reaction to proton translocation (for every two electrons transferred, four hydrogen ions are translocated across the cytoplasmic membrane), and thus conserves the redox energy in a proton gradient. NuoL is part of the inner membrane component of NADH dehydrogenase I . The protein has 14 transmembrane helices and a 110 Å long amphipathic α-helix that spans almost the entire length of the membrane domain . Transmembrane helices were assigned to locations in the crystal structure using Fourier transform analysis . A crystal structure of the membrane component at higher resolution has allowed better identification of the unusual arrangement of the transmembrane helices . NuoL was proposed to be located at the distal end of the membrane arm of NDH-1 and to function in proton translocation . The striking placement within the NDH-1 complex of NuoL's long amphipathic α-helix suggested that proton translocation may be facilitated by a piston-like movement of this helix . A modified indirect coupling mechanism was later proposed by...

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

- `encodes` <-- [[gene.b2278|gene.b2278]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33607`
- `KEGG:ecj:JW2273;eco:b2278;ecoc:C3026_12715;`
- `GeneID:945540;`
- `GO:GO:0005886; GO:0008137; GO:0015990; GO:0016020; GO:0022904; GO:0030964; GO:0042773; GO:0045271; GO:0048038`
- `EC:7.1.1.-`

## Notes

NADH-quinone oxidoreductase subunit L (EC 7.1.1.-) (NADH dehydrogenase I subunit L) (NDH-1 subunit L) (NUO12)
