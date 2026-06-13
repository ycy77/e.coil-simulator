---
entity_id: "protein.P0A814"
entity_type: "protein"
name: "ruvC"
source_database: "UniProt"
source_id: "P0A814"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00034, ECO:0000269|PubMed:21219465}. Note=In 15% of cell localizes to discrete nucleoid foci (probable DNA damage sites) upon treatment with mitomycin C (MMC) for 2 hours."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ruvC b1863 JW1852"
---

# ruvC

`protein.P0A814`

## Static

- Type: `protein`
- Source: `UniProt:P0A814`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00034, ECO:0000269|PubMed:21219465}. Note=In 15% of cell localizes to discrete nucleoid foci (probable DNA damage sites) upon treatment with mitomycin C (MMC) for 2 hours.

## Enriched Summary

FUNCTION: The RuvA-RuvB-RuvC complex processes Holliday junctions during genetic recombination and DNA repair (PubMed:6374379). Endonuclease that resolves Holliday junction (HJ) intermediates. Cleaves cruciform DNA by making single-stranded nicks across the junction at symmetrical positions within the homologous arms, leaving a 5'-phosphate and a 3'-hydroxyl group; requires a central core of homology in the junction (PubMed:10471285, PubMed:1661673, PubMed:1758493, PubMed:1829835, PubMed:36000732, PubMed:8001122, PubMed:8106500, PubMed:8195150, PubMed:9000618, PubMed:9135161, PubMed:9160752). The consensus cleavage sequence is 5'-(A/T)TT(C>G/A)-3'. Cleavage occurs on the 3'-side of the TT dinucleotide at the point of strand exchange, although there is some flexibility in the position cleaved (PubMed:10471285, PubMed:8001122, PubMed:8195150, PubMed:9135161). The cleavage reactions can be uncoupled; incision requires the presence of two consensus cleavage sequences, although they do not have to be identical (PubMed:9135161). The presence of a 5'-phosphate in a half-cut site accelerates cleavage of the second site, ensuring the second cleavage occurs within the lifetime of a single RuvC-HJ complex (PubMed:19399178). Binds to cruciform DNA in a sequence non-specific manner (PubMed:10471285, PubMed:8106500, PubMed:8195150)...

## Biological Role

Catalyzes RXN0-7496 (reaction.ecocyc.RXN0-7496). Component of resolvasome (complex.ecocyc.RUVABC-CPLX).

## Enriched Pathways

- `eco03440` Homologous recombination (KEGG)

## Annotation

FUNCTION: The RuvA-RuvB-RuvC complex processes Holliday junctions during genetic recombination and DNA repair (PubMed:6374379). Endonuclease that resolves Holliday junction (HJ) intermediates. Cleaves cruciform DNA by making single-stranded nicks across the junction at symmetrical positions within the homologous arms, leaving a 5'-phosphate and a 3'-hydroxyl group; requires a central core of homology in the junction (PubMed:10471285, PubMed:1661673, PubMed:1758493, PubMed:1829835, PubMed:36000732, PubMed:8001122, PubMed:8106500, PubMed:8195150, PubMed:9000618, PubMed:9135161, PubMed:9160752). The consensus cleavage sequence is 5'-(A/T)TT(C>G/A)-3'. Cleavage occurs on the 3'-side of the TT dinucleotide at the point of strand exchange, although there is some flexibility in the position cleaved (PubMed:10471285, PubMed:8001122, PubMed:8195150, PubMed:9135161). The cleavage reactions can be uncoupled; incision requires the presence of two consensus cleavage sequences, although they do not have to be identical (PubMed:9135161). The presence of a 5'-phosphate in a half-cut site accelerates cleavage of the second site, ensuring the second cleavage occurs within the lifetime of a single RuvC-HJ complex (PubMed:19399178). Binds to cruciform DNA in a sequence non-specific manner (PubMed:10471285, PubMed:8106500, PubMed:8195150). {ECO:0000255|HAMAP-Rule:MF_00034, ECO:0000269|PubMed:10471285, ECO:0000269|PubMed:1661673, ECO:0000269|PubMed:1758493, ECO:0000269|PubMed:1829835, ECO:0000269|PubMed:19399178, ECO:0000269|PubMed:36000732, ECO:0000269|PubMed:6374379, ECO:0000269|PubMed:8001122, ECO:0000269|PubMed:8106500, ECO:0000269|PubMed:8195150, ECO:0000269|PubMed:9000618, ECO:0000269|PubMed:9135161, ECO:0000269|PubMed:9160752}.; FUNCTION: An in vitro resolvase system that forms and processes HJ has been reconstituted with DNA substrates, RuvA, RuvB and RuvC. RuvA-RuvB increases the rate of strand exchange (branch migration), dissociates the RecA filament and allows RuvC to cleave in both orientations at the cruciform junction (PubMed:10421637, PubMed:9160752). HJ-RuvA-RuvB-RuvC complexes resolve Holliday junctions and also undergo branch migration, providing evidence for a coupled branch migration/HJ resolution reaction (PubMed:10421637). {ECO:0000269|PubMed:10421637, ECO:0000269|PubMed:9160752}.

## Pathways

- `eco03440` Homologous recombination (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN0-7496|reaction.ecocyc.RXN0-7496]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.RUVABC-CPLX|complex.ecocyc.RUVABC-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1863|gene.b1863]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A814`
- `KEGG:ecj:JW1852;eco:b1863;ecoc:C3026_10610;`
- `GeneID:86860005;89516631;946378;`
- `GO:GO:0000287; GO:0000725; GO:0003677; GO:0005737; GO:0008821; GO:0009314; GO:0048476; GO:0071932`
- `EC:3.1.21.10`

## Notes

Crossover junction endodeoxyribonuclease RuvC (EC 3.1.21.10) (Holliday junction endonuclease RuvC) (Holliday junction nuclease RuvC) (Holliday junction resolvase RuvC)
