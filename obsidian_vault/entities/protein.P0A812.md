---
entity_id: "protein.P0A812"
entity_type: "protein"
name: "ruvB"
source_database: "UniProt"
source_id: "P0A812"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00016, ECO:0000269|PubMed:21219465}. Note=In 15% of cell localizes to discrete nucleoid foci (probable DNA damage sites) upon treatment with mitomycin C (MMC) for 2 hours."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ruvB b1860 JW1849"
---

# ruvB

`protein.P0A812`

## Static

- Type: `protein`
- Source: `UniProt:P0A812`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00016, ECO:0000269|PubMed:21219465}. Note=In 15% of cell localizes to discrete nucleoid foci (probable DNA damage sites) upon treatment with mitomycin C (MMC) for 2 hours.

## Enriched Summary

FUNCTION: The RuvABC complex is involved in recombinational repair of UV or chemically damaged DNA (PubMed:6374379). The complex also plays an important role in the rescue of blocked DNA replication forks via replication fork reversal (RFR); RFR and homologous recombination required for UV light survival can be separated (PubMed:16424908, PubMed:18942176, PubMed:9814711). This subunit has a weak ATPase activity that is inhibited by its ADP product; binds ADP better than ATP (PubMed:2529252). Promotes Holliday junction (HJ) branch migration in conjunction with RuvA. Binds to HJ cruciform DNA; in the presence of RuvA, ATP and Mg(2+) the junction is dissociated. Hydrolyzable (d)NTPs can replace ATP but other analogs cannot (PubMed:1608954, PubMed:1617728, PubMed:6374379, PubMed:8393934). The RuvB hexamer acts as a pump, pulling DNA into and through the RuvAB complex (PubMed:9078376). Can bypass UV-induced lesions (PubMed:1617728) and physically cross-linked DNA strands (PubMed:10662672), suggesting RuvB does not unwind large sections of DNA. RuvA gives specificity by binding to cruciform junctions, while the RuvB ATPase provides the motor force for branch migration; excess RuvB can promote branch migration in the absence of RuvA (PubMed:10662672, PubMed:1617728)...

## Biological Role

Component of resolvasome (complex.ecocyc.RUVABC-CPLX).

## Enriched Pathways

- `eco03440` Homologous recombination (KEGG)

## Annotation

FUNCTION: The RuvABC complex is involved in recombinational repair of UV or chemically damaged DNA (PubMed:6374379). The complex also plays an important role in the rescue of blocked DNA replication forks via replication fork reversal (RFR); RFR and homologous recombination required for UV light survival can be separated (PubMed:16424908, PubMed:18942176, PubMed:9814711). This subunit has a weak ATPase activity that is inhibited by its ADP product; binds ADP better than ATP (PubMed:2529252). Promotes Holliday junction (HJ) branch migration in conjunction with RuvA. Binds to HJ cruciform DNA; in the presence of RuvA, ATP and Mg(2+) the junction is dissociated. Hydrolyzable (d)NTPs can replace ATP but other analogs cannot (PubMed:1608954, PubMed:1617728, PubMed:6374379, PubMed:8393934). The RuvB hexamer acts as a pump, pulling DNA into and through the RuvAB complex (PubMed:9078376). Can bypass UV-induced lesions (PubMed:1617728) and physically cross-linked DNA strands (PubMed:10662672), suggesting RuvB does not unwind large sections of DNA. RuvA gives specificity by binding to cruciform junctions, while the RuvB ATPase provides the motor force for branch migration; excess RuvB can promote branch migration in the absence of RuvA (PubMed:10662672, PubMed:1617728). In vitro the RuvA-RuvB complex has 5'-3' helicase activity that is ATP-dependent and works best on short dsDNA hybrids; 52 and 66-nucleotide (nt) pairs are easily displaced, hybrids greater than 140-nts are not (PubMed:8433990). RuvA stimulates the weak ATPase activity of RuvB in the presence of DNA; HJ DNA stimulates ATPase about 10-fold (PubMed:1435721, PubMed:1833759, PubMed:8393934). {ECO:0000255|HAMAP-Rule:MF_00016, ECO:0000269|PubMed:10662672, ECO:0000269|PubMed:1435721, ECO:0000269|PubMed:1608954, ECO:0000269|PubMed:1617728, ECO:0000269|PubMed:16424908, ECO:0000269|PubMed:1833759, ECO:0000269|PubMed:18942176, ECO:0000269|PubMed:2529252, ECO:0000269|PubMed:6374379, ECO:0000269|PubMed:8393934, ECO:0000269|PubMed:8433990, ECO:0000269|PubMed:9078376, ECO:0000269|PubMed:9814711}.; FUNCTION: An in vitro resolvase system that forms and processes HJ has been reconstituted with DNA substrates, RuvA, RuvB and RuvC. RuvA-RuvB increases the rate of strand exchange (branch migration), dissociates the RecA filament and allows RuvC to cleave in both orientations at the cruciform junction (PubMed:10421637, PubMed:9160752). HJ-RuvA-RuvB-RuvC complexes resolve Holliday junctions and also undergo branch migration, providing evidence for a coupled branch migration/HJ resolution reaction (PubMed:10421637). {ECO:0000269|PubMed:10421637, ECO:0000269|PubMed:9160752}.

## Pathways

- `eco03440` Homologous recombination (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.RUVABC-CPLX|complex.ecocyc.RUVABC-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=12 | EcoCyc protcplxs.col coefficient=12

## Incoming Edges (1)

- `encodes` <-- [[gene.b1860|gene.b1860]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A812`
- `KEGG:ecj:JW1849;eco:b1860;ecoc:C3026_10595;`
- `GeneID:75171931;75202735;946371;`
- `GO:GO:0000400; GO:0000725; GO:0003678; GO:0005524; GO:0005829; GO:0009378; GO:0009379; GO:0009411; GO:0009432; GO:0016887; GO:0048476`
- `EC:3.6.4.-`

## Notes

Holliday junction branch migration complex subunit RuvB (EC 3.6.4.-)
