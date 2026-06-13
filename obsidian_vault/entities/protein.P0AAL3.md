---
entity_id: "protein.P0AAL3"
entity_type: "protein"
name: "napG"
source_database: "UniProt"
source_id: "P0AAL3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:14674886}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "napG yojA yojB b2205 JW2193"
---

# napG

`protein.P0AAL3`

## Static

- Type: `protein`
- Source: `UniProt:P0AAL3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:14674886}.

## Enriched Summary

FUNCTION: Required for electron transfer from ubiquinol, via NapC, to the periplasmic nitrate reductase NapAB complex. {ECO:0000269|PubMed:11967083, ECO:0000269|PubMed:14674886}. The EG12064 gene, which is located in the operon of the periplasmic nitrite reductase, encodes a ferredoxin-type non-heme iron-sulfur protein . A mutant lacking EG12064 and EG12062 was totally defective for growth in glycerol/nitrate medium. When grown in glucose/nitrate medium, it was found that the mutant had almost completely lost the ability to reduce nitrate. With ubiquinol as the electron donor no significant nitrate reduction could be observed . In a subsequent study, deletion of either EG12064 or EG12062 almost abolished Nap-dependent nitrate reduction by a strain incapable of producing menaquinone. Since experiments with a bacterial two-hybrid system showed that NapH interacts with NapC, it was concluded that NapG and NapH are required for electron transfer from ubiquinol, but not menaquinol, via EG12060 NapC, to the NAP-CPLX NapAB complex . NapG contains a twin-arginine sequence that is essential for its function, suggesting that it may be secreted into the periplasm by the twin arginine translocation pathway .

## Biological Role

Component of ubiquinol—[NapC cytochrome c] reductase (complex.ecocyc.CPLX0-3241).

## Annotation

FUNCTION: Required for electron transfer from ubiquinol, via NapC, to the periplasmic nitrate reductase NapAB complex. {ECO:0000269|PubMed:11967083, ECO:0000269|PubMed:14674886}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3241|complex.ecocyc.CPLX0-3241]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2205|gene.b2205]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAL3`
- `KEGG:ecj:JW2193;eco:b2205;ecoc:C3026_12320;`
- `GeneID:86860377;93774973;945544;`
- `GO:GO:0005886; GO:0042597; GO:0046872; GO:0051539`

## Notes

Ferredoxin-type protein NapG (Ubiquinol--[NapC cytochrome c] reductase NapG subunit)
