---
entity_id: "protein.P0AFD6"
entity_type: "protein"
name: "nuoI"
source_database: "UniProt"
source_id: "P0AFD6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Peripheral membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nuoI b2281 JW2276"
---

# nuoI

`protein.P0AFD6`

## Static

- Type: `protein`
- Source: `UniProt:P0AFD6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Peripheral membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: NDH-1 shuttles electrons from NADH, via FMN and iron-sulfur (Fe-S) centers, to quinones in the respiratory chain. The immediate electron acceptor for the enzyme in this species is believed to be ubiquinone. Couples the redox reaction to proton translocation (for every two electrons transferred, four hydrogen ions are translocated across the cytoplasmic membrane), and thus conserves the redox energy in a proton gradient. NuoI is part of the connecting fragment of NADH dehydrogenase I and is required for efficient assembly of NDH-1 . The Fe-S clusters of NuoI conduct electrons from NuoG to the Fe-S cluster of NuoB . Based on sequence similarity, this subunit was predicted to contain the two 4Fe-4S clusters N6a and N6b . EPR signals for both N6a and N6b have now been detected . Although N6a and N6b are located close to each other, they display no spin-spin interaction . The location and identity of EPR spectra for the N4 and N5 Fe-S clusters were subject of some controversy. The 4Fe-4S cluster N4, located on the NuoG subunit, was thought to be identical to either N6a or N6b . Recent reevaluation of the data and mutational analysis of the N5 His(Cys)3 ligands confirmed the location of both N4 and N5 in the NuoG subunit...

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

- `encodes` <-- [[gene.b2281|gene.b2281]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFD6`
- `KEGG:ecj:JW2276;eco:b2281;ecoc:C3026_12730;`
- `GeneID:86860444;89517116;946757;`
- `GO:GO:0005506; GO:0005886; GO:0009060; GO:0016020; GO:0022904; GO:0030964; GO:0045271; GO:0048038; GO:0050136; GO:0051539`
- `EC:7.1.1.-`

## Notes

NADH-quinone oxidoreductase subunit I (EC 7.1.1.-) (NADH dehydrogenase I subunit I) (NDH-1 subunit I) (NUO9)
