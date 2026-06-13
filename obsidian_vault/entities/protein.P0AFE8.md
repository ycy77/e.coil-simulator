---
entity_id: "protein.P0AFE8"
entity_type: "protein"
name: "nuoM"
source_database: "UniProt"
source_id: "P0AFE8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nuoM b2277 JW2272"
---

# nuoM

`protein.P0AFE8`

## Static

- Type: `protein`
- Source: `UniProt:P0AFE8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: NDH-1 shuttles electrons from NADH, via FMN and iron-sulfur (Fe-S) centers, to quinones in the respiratory chain. The immediate electron acceptor for the enzyme in this species is believed to be ubiquinone. Couples the redox reaction to proton translocation (for every two electrons transferred, four hydrogen ions are translocated across the cytoplasmic membrane), and thus conserves the redox energy in a proton gradient. NuoM is part of the inner membrane component of NADH dehydrogenase I . The protein has 14 transmembrane helices . Transmembrane helices were assigned to locations in the crystal structure using Fourier transform analysis . A crystal structure of the membrane component at higher resolution has allowed better identification of the unusual arrangement of the transmembrane helices . This subunit may function in proton translocation and may contain the ubiquinone binding site . Site-directed mutagenesis of various conserved amino acid residues suggest that E144 and K234 are essential for energy transduction and may thus participate in proton translocation . The E144 residue was systematically shifted to other positions within helix V and adjacent helices by site-directed mutagenesis. When the glutamic acid residue was shifted by one turn of the helix upstream or downstream, a moderate level of energy-transducing activity of NDH-1 was restored...

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

- `encodes` <-- [[gene.b2277|gene.b2277]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFE8`
- `KEGG:ecj:JW2272;eco:b2277;ecoc:C3026_12710;`
- `GeneID:75172405;75205677;947731;`
- `GO:GO:0005886; GO:0008137; GO:0009060; GO:0015990; GO:0016020; GO:0022904; GO:0030964; GO:0042773; GO:0045271; GO:0048039`
- `EC:7.1.1.-`

## Notes

NADH-quinone oxidoreductase subunit M (EC 7.1.1.-) (NADH dehydrogenase I subunit M) (NDH-1 subunit M) (NUO13)
