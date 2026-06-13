---
entity_id: "protein.P31224"
entity_type: "protein"
name: "acrB"
source_database: "UniProt"
source_id: "P31224"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15228545, ECO:0000269|PubMed:16079137}; Multi-pass membrane protein {ECO:0000269|PubMed:15228545, ECO:0000269|PubMed:16079137}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "acrB acrE b0462 JW0451"
---

# acrB

`protein.P31224`

## Static

- Type: `protein`
- Source: `UniProt:P31224`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15228545, ECO:0000269|PubMed:16079137}; Multi-pass membrane protein {ECO:0000269|PubMed:15228545, ECO:0000269|PubMed:16079137}.

## Enriched Summary

FUNCTION: The inner membrane transporter component of the AcrAB-TolC efflux system which confers multidrug resistance (PubMed:16915237, PubMed:16946072, PubMed:17194213, PubMed:23010927, PubMed:28355133, PubMed:31201302). The AcrAB-TolC efflux system has a broad substrate specificity, acting as a substrate:proton antiporter, using proton motive force to export substrates (PubMed:16915237, PubMed:16946072, PubMed:17015667, PubMed:17194213, PubMed:19023693, PubMed:19425588, PubMed:22121023, PubMed:23010927, PubMed:25248080). Oxidized fatty acids may be one class of native substrate for AcrB, as part of the AcrAB-TolC efflux protein complex (PubMed:33785633). AcrB is also a component of the AcrABZ-TolC efflux system, where the small accessory protein AcrZ, together with membrane lipids, may influence the specificity of drug export (PubMed:23010927, PubMed:24747401, PubMed:32348749). {ECO:0000269|PubMed:16915237, ECO:0000269|PubMed:16946072, ECO:0000269|PubMed:17015667, ECO:0000269|PubMed:17194213, ECO:0000269|PubMed:19023693, ECO:0000269|PubMed:19425588, ECO:0000269|PubMed:22121023, ECO:0000269|PubMed:23010927, ECO:0000269|PubMed:24747401, ECO:0000269|PubMed:25248080, ECO:0000269|PubMed:28355133, ECO:0000269|PubMed:31201302, ECO:0000269|PubMed:32348749, ECO:0000269|PubMed:33785633}...

## Biological Role

Component of multidrug efflux pump AcrAB-TolC (complex.ecocyc.TRANS-CPLX-201).

## Enriched Pathways

- `eco01501` beta-Lactam resistance (KEGG)
- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Annotation

FUNCTION: The inner membrane transporter component of the AcrAB-TolC efflux system which confers multidrug resistance (PubMed:16915237, PubMed:16946072, PubMed:17194213, PubMed:23010927, PubMed:28355133, PubMed:31201302). The AcrAB-TolC efflux system has a broad substrate specificity, acting as a substrate:proton antiporter, using proton motive force to export substrates (PubMed:16915237, PubMed:16946072, PubMed:17015667, PubMed:17194213, PubMed:19023693, PubMed:19425588, PubMed:22121023, PubMed:23010927, PubMed:25248080). Oxidized fatty acids may be one class of native substrate for AcrB, as part of the AcrAB-TolC efflux protein complex (PubMed:33785633). AcrB is also a component of the AcrABZ-TolC efflux system, where the small accessory protein AcrZ, together with membrane lipids, may influence the specificity of drug export (PubMed:23010927, PubMed:24747401, PubMed:32348749). {ECO:0000269|PubMed:16915237, ECO:0000269|PubMed:16946072, ECO:0000269|PubMed:17015667, ECO:0000269|PubMed:17194213, ECO:0000269|PubMed:19023693, ECO:0000269|PubMed:19425588, ECO:0000269|PubMed:22121023, ECO:0000269|PubMed:23010927, ECO:0000269|PubMed:24747401, ECO:0000269|PubMed:25248080, ECO:0000269|PubMed:28355133, ECO:0000269|PubMed:31201302, ECO:0000269|PubMed:32348749, ECO:0000269|PubMed:33785633}.; FUNCTION: (Microbial infection) Involved in contact-dependent growth inhibition (CDI), acts downstream of BamA, the receptor for CDI (PubMed:18761695). Its role in CDI is independent of the AcrAB-TolC efflux pump complex (PubMed:18761695). {ECO:0000269|PubMed:18761695}.

## Pathways

- `eco01501` beta-Lactam resistance (KEGG)
- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.TRANS-CPLX-201|complex.ecocyc.TRANS-CPLX-201]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3 | EcoCyc transporter component coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b0462|gene.b0462]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31224`
- `KEGG:ecj:JW0451;eco:b0462;ecoc:C3026_02265;`
- `GeneID:75170480;75202887;945108;`
- `GO:GO:0005886; GO:0009410; GO:0009636; GO:0015125; GO:0015562; GO:0015567; GO:0015721; GO:0015895; GO:0015908; GO:0016020; GO:0042802; GO:0042908; GO:0042910; GO:0042930; GO:0042931; GO:0046677; GO:0098567; GO:0140330; GO:1990281`

## Notes

Multidrug efflux pump subunit AcrB (AcrAB-TolC multidrug efflux pump subunit AcrB) (Acridine resistance protein B)
