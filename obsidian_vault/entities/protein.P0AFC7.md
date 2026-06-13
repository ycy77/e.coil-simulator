---
entity_id: "protein.P0AFC7"
entity_type: "protein"
name: "nuoB"
source_database: "UniProt"
source_id: "P0AFC7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Peripheral membrane protein; Cytoplasmic side."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nuoB b2287 JW5875"
---

# nuoB

`protein.P0AFC7`

## Static

- Type: `protein`
- Source: `UniProt:P0AFC7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Peripheral membrane protein; Cytoplasmic side.

## Enriched Summary

FUNCTION: NDH-1 shuttles electrons from NADH, via FMN and iron-sulfur (Fe-S) centers, to quinones in the respiratory chain. The immediate electron acceptor for the enzyme in this species is ubiquinone. Couples the redox reaction to proton translocation (for every two electrons transferred, four hydrogen ions are translocated across the cytoplasmic membrane), and thus conserves the redox energy in a proton gradient. NuoB is part of the connecting fragment of NADH dehydrogenase I . This subunit contains the N2 4Fe-4S cluster , which may play a role in proton translocation activity of NDH I . The Glu67 residue is most likely protonated by oxidation of the N2 cluster, and is involved in proton translocation . A mechanism by which the redox reaction at the N2 cluster induces conformational changes leading to proton translocation has been proposed . Point mutations in NuoB have been analyzed; the Tyr114 and Tyr139 residues appear to be protonated upon reduction of the 4Fe-4S cluster, and a double mutant retains only 20% activity . Mutagenesis of the conserved acidic residues E67, D77, and D94 abolishes electron transfer activity of NDH I . Enzymes containing these mutant subunits have been characterized by FT-IR difference spectroscopy to evaluate conformational changes...

## Biological Role

Catalyzes NADH:ubiquinone oxidoreductase (reaction.R11945). Component of NADH:quinone oxidoreductase I, peripheral arm (complex.ecocyc.CPLX0-3361), NADH:quinone oxidoreductase I (complex.ecocyc.NADH-DHI-CPLX).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: NDH-1 shuttles electrons from NADH, via FMN and iron-sulfur (Fe-S) centers, to quinones in the respiratory chain. The immediate electron acceptor for the enzyme in this species is ubiquinone. Couples the redox reaction to proton translocation (for every two electrons transferred, four hydrogen ions are translocated across the cytoplasmic membrane), and thus conserves the redox energy in a proton gradient.

## Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R11945|reaction.R11945]] `KEGG` `database` - via EC:7.1.1.2
- `is_component_of` --> [[complex.ecocyc.CPLX0-3361|complex.ecocyc.CPLX0-3361]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.NADH-DHI-CPLX|complex.ecocyc.NADH-DHI-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2287|gene.b2287]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFC7`
- `KEGG:ecj:JW5875;eco:b2287;ecoc:C3026_12760;`
- `GeneID:86860450;93774887;946738;`
- `GO:GO:0005506; GO:0005886; GO:0008137; GO:0009060; GO:0015990; GO:0016020; GO:0022904; GO:0030964; GO:0045271; GO:0048038; GO:0050136; GO:0051539`
- `EC:7.1.1.-`

## Notes

NADH-quinone oxidoreductase subunit B (EC 7.1.1.-) (NADH dehydrogenase I subunit B) (NDH-1 subunit B) (NUO2)
