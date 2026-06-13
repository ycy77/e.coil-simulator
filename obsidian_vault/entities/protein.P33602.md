---
entity_id: "protein.P33602"
entity_type: "protein"
name: "nuoG"
source_database: "UniProt"
source_id: "P33602"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:16079137}. Cell inner membrane {ECO:0000269|PubMed:16079137}; Peripheral membrane protein {ECO:0000269|PubMed:16079137}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nuoG b2283 JW2278"
---

# nuoG

`protein.P33602`

## Static

- Type: `protein`
- Source: `UniProt:P33602`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:16079137}. Cell inner membrane {ECO:0000269|PubMed:16079137}; Peripheral membrane protein {ECO:0000269|PubMed:16079137}.

## Enriched Summary

FUNCTION: NDH-1 shuttles electrons from NADH, via FMN and iron-sulfur (Fe-S) centers, to quinones in the respiratory chain. The immediate electron acceptor for the enzyme in this species is believed to be ubiquinone. Couples the redox reaction to proton translocation (for every two electrons transferred, four hydrogen ions are translocated across the cytoplasmic membrane), and thus conserves the redox energy in a proton gradient. NuoG is part of the soluble fragment of NADH dehydrogenase I, which represents the electron input part of the enzyme . NuoG is essential for NDH-1 function . This subunit contains the 2Fe-2S cluster N1b and three 4Fe-4S clusters. N7 was formerly misidentified as "N1c", whose EPR signal is in fact derived from the 2Fe-2S cluster N1a on the NuoE subunit . N7 is non-conserved and not thought to be involved in electron transfer; however, it is essential for the stability of NDH-1 . The cysteine residues responsible for ligation of the 4Fe-4S clusters were identified by site-directed mutagenesis . However, the location and identity of EPR spectra for the N4 and N5 Fe-S clusters were subject of some controversy . Recent reevaluation of the data and mutational analysis of the N5 His(Cys)3 ligands confirmed the location of both N4 and N5 in the NuoG subunit...

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

- `encodes` <-- [[gene.b2283|gene.b2283]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33602`
- `KEGG:ecj:JW2278;eco:b2283;ecoc:C3026_12740;`
- `GeneID:946762;`
- `GO:GO:0005737; GO:0005886; GO:0008137; GO:0009060; GO:0016020; GO:0016651; GO:0022904; GO:0030964; GO:0042773; GO:0043546; GO:0045271; GO:0046872; GO:0048038; GO:0051537; GO:0051539`
- `EC:7.1.1.-`

## Notes

NADH-quinone oxidoreductase subunit G (EC 7.1.1.-) (NADH dehydrogenase I subunit G) (NDH-1 subunit G) (NUO7)
