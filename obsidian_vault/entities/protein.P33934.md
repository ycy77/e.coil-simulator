---
entity_id: "protein.P33934"
entity_type: "protein"
name: "napH"
source_database: "UniProt"
source_id: "P33934"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:14674886, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:14674886}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "napH yejZ b2204 JW2192"
---

# napH

`protein.P33934`

## Static

- Type: `protein`
- Source: `UniProt:P33934`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:14674886, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:14674886}.

## Enriched Summary

FUNCTION: Required for electron transfer from ubiquinol, via NapC, to the periplasmic nitrate reductase NapAB complex. {ECO:0000269|PubMed:11967083, ECO:0000269|PubMed:14674886}. The EG12062 gene encodes a ferredoxin-type non-heme iron-sulfur protein. . NapH is an integral membrane protein with four membrane-spanning domains; the C-terminal domain with its two predicted [4Fe-4S] clusters is located in the cytoplasm . Using two-hybrid assays, it has been shown that NapH interacts strongly with EG12060 NapC . A mutant lacking EG12064 and EG12062 was totally defective for growth in glycerol/nitrate medium. When grown in glucose/nitrate medium, it was found that the mutant had almost completely lost the ability to reduce nitrate. With ubiquinol as the electron donor no significant nitrate reduction could be observed . In a subsequent study, deletion of either EG12064 or EG12062 almost abolished Nap-dependent nitrate reduction by a strain uncapable of producing menaquinone. Thus it was concluded that NapG and NapH are required for electron transfer from ubiquinol, but not menaquinol, via EG12060 NapC, to the NAP-CPLX NapAB complex .

## Biological Role

Component of ubiquinol—[NapC cytochrome c] reductase (complex.ecocyc.CPLX0-3241).

## Annotation

FUNCTION: Required for electron transfer from ubiquinol, via NapC, to the periplasmic nitrate reductase NapAB complex. {ECO:0000269|PubMed:11967083, ECO:0000269|PubMed:14674886}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3241|complex.ecocyc.CPLX0-3241]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2204|gene.b2204]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33934`
- `KEGG:ecj:JW2192;eco:b2204;ecoc:C3026_12315;`
- `GeneID:945984;`
- `GO:GO:0005886; GO:0016020; GO:0046872; GO:0051539`

## Notes

Ferredoxin-type protein NapH (Ubiquinol--[NapC cytochrome c] reductase NapH subunit)
