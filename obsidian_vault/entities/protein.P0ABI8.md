---
entity_id: "protein.P0ABI8"
entity_type: "protein"
name: "cyoB"
source_database: "UniProt"
source_id: "P0ABI8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:6365921}; Multi-pass membrane protein {ECO:0000269|PubMed:6365921}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cyoB b0431 JW0421"
---

# cyoB

`protein.P0ABI8`

## Static

- Type: `protein`
- Source: `UniProt:P0ABI8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:6365921}; Multi-pass membrane protein {ECO:0000269|PubMed:6365921}.

## Enriched Summary

FUNCTION: Cytochrome bo(3) ubiquinol oxidase is the terminal enzyme in the aerobic respiratory chain of E.coli that predominates when cells are grown at high aeration. Catalyzes the four-electron reduction of O2 to water, using a ubiquinol as a membrane soluble electron donor for molecular oxygen reduction; ubiquinol-8 is the natural substrate for E.coli. Has proton pump activity across the membrane in addition to electron transfer, pumping 2 protons/electron and generating a proton motive force. All the redox centers of this enzyme complex are located within the largest subunit, subunit I. Protons are probably pumped via D- and K- channels found in this subunit (PubMed:11017202). {ECO:0000269|PubMed:11017202, ECO:0000269|PubMed:19542282, ECO:0000269|PubMed:22843529, ECO:0000269|PubMed:6308657}. cyoB encodes subunit I of the cytochrome bo complex. The three prosthetic groups (heme O, heme B and CuB) are located in subunit 1 and are liganded by conserved histidine residues: His106 and His421 for heme B; His419 for heme O; His284, His333 and His334 for CuB ( and reviewed in ). The 3.5Å crystal structure confirmed these assignments . Subunit 1 contains 15 transmembrane helices ; helices 1-12 constitute a transmembrane barrel...

## Biological Role

Catalyzes ubiquinol:oxygen oxidoreductase (H+-transporting) (reaction.R11335). Component of cytochrome bo3 ubiquinol:oxygen oxidoreductase (complex.ecocyc.CYT-O-UBIOX-CPLX).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Cytochrome bo(3) ubiquinol oxidase is the terminal enzyme in the aerobic respiratory chain of E.coli that predominates when cells are grown at high aeration. Catalyzes the four-electron reduction of O2 to water, using a ubiquinol as a membrane soluble electron donor for molecular oxygen reduction; ubiquinol-8 is the natural substrate for E.coli. Has proton pump activity across the membrane in addition to electron transfer, pumping 2 protons/electron and generating a proton motive force. All the redox centers of this enzyme complex are located within the largest subunit, subunit I. Protons are probably pumped via D- and K- channels found in this subunit (PubMed:11017202). {ECO:0000269|PubMed:11017202, ECO:0000269|PubMed:19542282, ECO:0000269|PubMed:22843529, ECO:0000269|PubMed:6308657}.

## Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R11335|reaction.R11335]] `KEGG` `database` - via EC:7.1.1.3
- `is_component_of` --> [[complex.ecocyc.CYT-O-UBIOX-CPLX|complex.ecocyc.CYT-O-UBIOX-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0431|gene.b0431]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABI8`
- `KEGG:ecj:JW0421;eco:b0431;ecoc:C3026_02105;`
- `GeneID:93777023;945615;`
- `GO:GO:0004129; GO:0005507; GO:0005886; GO:0009055; GO:0009060; GO:0009319; GO:0009486; GO:0015078; GO:0015453; GO:0015990; GO:0016682; GO:0019646; GO:0020037; GO:0022904; GO:0048039`
- `EC:7.1.1.3`

## Notes

Cytochrome bo(3) ubiquinol oxidase subunit 1 (cyt bo(3) subunit 1) (EC 7.1.1.3) (Cytochrome b562-o complex subunit I) (Cytochrome o ubiquinol oxidase subunit 1) (Cytochrome o subunit 1) (Oxidase bo(3) subunit 1) (Ubiquinol oxidase chain A) (Ubiquinol oxidase polypeptide I) (Ubiquinol oxidase subunit 1)
