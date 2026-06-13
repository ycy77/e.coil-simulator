---
entity_id: "protein.Q46868"
entity_type: "protein"
name: "ubiK"
source_database: "UniProt"
source_id: "Q46868"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_02216, ECO:0000269|PubMed:30686758}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ubiK yqiC b3042 JW5505"
---

# ubiK

`protein.Q46868`

## Static

- Type: `protein`
- Source: `UniProt:Q46868`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_02216, ECO:0000269|PubMed:30686758}.

## Enriched Summary

FUNCTION: Required for efficient ubiquinone (coenzyme Q) biosynthesis under aerobic conditions (PubMed:28559279, PubMed:30686758). UbiK is probably an accessory factor of Ubi enzymes and facilitates ubiquinone biosynthesis by acting as an assembly factor, a targeting factor, or both (PubMed:28559279). Dispensable for ubiquinone biosynthesis under anaerobiosis (PubMed:28559279). {ECO:0000269|PubMed:28559279, ECO:0000269|PubMed:30686758}. UbiK is an accessory factor in ubiquinone biosynthesis that is part of the Ubi complex metabolon . UbiK interacts directly with the C terminus of UbiJ; the isolated proteins appear to form a 2:1 UbiK:UbiJ heterotrimer that is able to bind palmitoleate , ubiquinone-8, 2-octaprenylphenol, and C6-demethoxy-ubiquinone-8 . Purified UbiK homotrimerizes . UbiK predominantly localizes to the membrane fraction, but can also be found in the cytosol. The seven ubiquinone biosynthesis proteins UbiE, UbiF, UbiG, UbiH, UbiI, UbiJ, and UbiK form a 1 MDa complex in the cytosol . A ubiK mutant contains 18% of the wild type level of ubiquinone and accumulates octaprenylphenol . A ΔubiIΔubiK double mutant produces no detectable ubiquinone and in contrast to the single mutants, has a significant growth defect when grown aerobically on rich medium and does not grow on the non-fermentable carbon sources oleate, acetate, and succinate...

## Biological Role

Component of Ubi complex (complex.ecocyc.CPLX0-8301).

## Annotation

FUNCTION: Required for efficient ubiquinone (coenzyme Q) biosynthesis under aerobic conditions (PubMed:28559279, PubMed:30686758). UbiK is probably an accessory factor of Ubi enzymes and facilitates ubiquinone biosynthesis by acting as an assembly factor, a targeting factor, or both (PubMed:28559279). Dispensable for ubiquinone biosynthesis under anaerobiosis (PubMed:28559279). {ECO:0000269|PubMed:28559279, ECO:0000269|PubMed:30686758}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8301|complex.ecocyc.CPLX0-8301]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3042|gene.b3042]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q46868`
- `KEGG:ecj:JW5505;eco:b3042;ecoc:C3026_16615;`
- `GeneID:947524;`
- `GO:GO:0005829; GO:0006744; GO:0016020; GO:0042802; GO:0110142`

## Notes

Ubiquinone biosynthesis accessory factor UbiK
