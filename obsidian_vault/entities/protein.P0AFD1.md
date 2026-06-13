---
entity_id: "protein.P0AFD1"
entity_type: "protein"
name: "nuoE"
source_database: "UniProt"
source_id: "P0AFD1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nuoE b2285 JW2280"
---

# nuoE

`protein.P0AFD1`

## Static

- Type: `protein`
- Source: `UniProt:P0AFD1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: NDH-1 shuttles electrons from NADH, via FMN and iron-sulfur (Fe-S) centers, to quinones in the respiratory chain. The immediate electron acceptor for the enzyme in this species is believed to be ubiquinone. Couples the redox reaction to proton translocation (for every two electrons transferred, four hydrogen ions are translocated across the cytoplasmic membrane), and thus conserves the redox energy in a proton gradient. NuoE is part of the soluble fragment of NADH dehydrogenase I (NDH-1), which represents the electron input part of the enzyme . Based on sequence similarity, this subunit is predicted to contain the N1a 2Fe-2S cluster . The location of the conserved N1a cluster suggests that it does not participate in electron transfer chain through NDH-1. Site-directed mutagenesis of the cysteine residues expected to coordinate the N1a cluster resulted in the loss of N1a and significantly reduced the amount of the N1b cluster coordinated by the NuoG subunit. Only the C97A mutant retained most of the N1a cluster. The mutants showed reduced NHD-1 activity, but severely affected the stability of the NDH-1 complex . A V96P/N142M double mutant switches the N1a cluster from its high-potential to a low-potential state . NDH-1 containing the NuoE G135D mutant is stable, but loses most NADH oxidase activity; the loss is attributed to the inability to release NAD+, i.e...

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

- `encodes` <-- [[gene.b2285|gene.b2285]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFD1`
- `KEGG:ecj:JW2280;eco:b2285;ecoc:C3026_12750;`
- `GeneID:86860448;93774889;946746;`
- `GO:GO:0005886; GO:0016020; GO:0016491; GO:0022904; GO:0030964; GO:0045271; GO:0046872; GO:0048038; GO:0051537; GO:1902600`
- `EC:7.1.1.-`

## Notes

NADH-quinone oxidoreductase subunit E (EC 7.1.1.-) (NADH dehydrogenase I subunit E) (NDH-1 subunit E) (NUO5)
