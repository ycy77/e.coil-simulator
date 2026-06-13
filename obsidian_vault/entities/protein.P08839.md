---
entity_id: "protein.P08839"
entity_type: "protein"
name: "ptsI"
source_database: "UniProt"
source_id: "P08839"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:33376208}. Note=Localizes mainly near one pole of the cell (PubMed:33376208). Localization at the pole requires phosphorylation at Tyr-122 and is controlled by the pole-localizer protein TmaR (PubMed:33376208). {ECO:0000269|PubMed:33376208}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ptsI b2416 JW2409"
---

# ptsI

`protein.P08839`

## Static

- Type: `protein`
- Source: `UniProt:P08839`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:33376208}. Note=Localizes mainly near one pole of the cell (PubMed:33376208). Localization at the pole requires phosphorylation at Tyr-122 and is controlled by the pole-localizer protein TmaR (PubMed:33376208). {ECO:0000269|PubMed:33376208}.

## Enriched Summary

FUNCTION: General (non sugar-specific) component of the phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS). This major carbohydrate active-transport system catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. Enzyme I transfers the phosphoryl group from phosphoenolpyruvate (PEP) to the phosphoryl carrier protein (HPr) (PubMed:12705838, PubMed:17053069, PubMed:7876255). Can also use (Z)-3-fluoro-PEP (ZFPEP), (Z)-3-methyl-PEP (ZMePEP), (Z)-3-chloro-PEP (ZClPEP) and (E)-3-chloro-PEP (EClPEP) as alternative phosphoryl donors (PubMed:12705838). {ECO:0000269|PubMed:12705838, ECO:0000269|PubMed:17053069, ECO:0000269|PubMed:7876255}.

## Biological Role

Component of PTS enzyme I (complex.ecocyc.CPLX0-7938), PTS Enzyme I-Nτ-phospho-L-histidine (complex.ecocyc.PTSI-PHOSPHORYLATED).

## Enriched Pathways

- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

FUNCTION: General (non sugar-specific) component of the phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS). This major carbohydrate active-transport system catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. Enzyme I transfers the phosphoryl group from phosphoenolpyruvate (PEP) to the phosphoryl carrier protein (HPr) (PubMed:12705838, PubMed:17053069, PubMed:7876255). Can also use (Z)-3-fluoro-PEP (ZFPEP), (Z)-3-methyl-PEP (ZMePEP), (Z)-3-chloro-PEP (ZClPEP) and (E)-3-chloro-PEP (EClPEP) as alternative phosphoryl donors (PubMed:12705838). {ECO:0000269|PubMed:12705838, ECO:0000269|PubMed:17053069, ECO:0000269|PubMed:7876255}.

## Pathways

- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7938|complex.ecocyc.CPLX0-7938]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.PTSI-PHOSPHORYLATED|complex.ecocyc.PTSI-PHOSPHORYLATED]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2416|gene.b2416]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P08839`
- `KEGG:ecj:JW2409;eco:b2416;ecoc:C3026_13430;`
- `GeneID:946879;`
- `GO:GO:0005829; GO:0008965; GO:0009401; GO:0015764; GO:0016301; GO:0042802; GO:0046872`
- `EC:2.7.3.9`

## Notes

Phosphoenolpyruvate-protein phosphotransferase (EC 2.7.3.9) (Phosphotransferase system, enzyme I)
