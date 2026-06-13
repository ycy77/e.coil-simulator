---
entity_id: "protein.P0AGK8"
entity_type: "protein"
name: "iscR"
source_database: "UniProt"
source_id: "P0AGK8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "iscR yfhP b2531 JW2515"
---

# iscR

`protein.P0AGK8`

## Static

- Type: `protein`
- Source: `UniProt:P0AGK8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Regulates the transcription of several operons and genes involved in the biogenesis of Fe-S clusters and Fe-S-containing proteins. Transcriptional repressor of the iscRSUA operon, which is involved in the assembly of Fe-S clusters into Fe-S proteins. In its apoform, under conditions of oxidative stress or iron deprivation, it activates the suf operon, which is a second operon involved in the assembly of Fe-S clusters. Represses its own transcription as well as that of toxin rnlA. {ECO:0000269|PubMed:11742080, ECO:0000269|PubMed:16824106, ECO:0000269|PubMed:20421606}. The transcription factor IscR, for "Iron-sulfur cluster Regulator," is negatively autoregulated, and it contains an iron-sulfur cluster that could act as a sensor of iron-sulfur cluster assembly . This protein regulates the expression of the operons that encode components of a secondary pathway of iron-sulfur cluster assembly, iron-sulfur proteins, anaerobic respiration enzymes, and biofilm formation . In addition, IscR contributes to the cellular response to stress caused by the superoxide-producing redox-cycling agent phenazine methosulfate (PMS) . The role of IscR in iron-sulfur (Fe-S) cluster biogenesis was simulated and analyzed in a mathematical model in...

## Biological Role

Component of DNA-binding transcriptional repressor IscR-a [2Fe-2S] iron-sulfur cluster (complex.ecocyc.CPLX0-8083).

## Annotation

FUNCTION: Regulates the transcription of several operons and genes involved in the biogenesis of Fe-S clusters and Fe-S-containing proteins. Transcriptional repressor of the iscRSUA operon, which is involved in the assembly of Fe-S clusters into Fe-S proteins. In its apoform, under conditions of oxidative stress or iron deprivation, it activates the suf operon, which is a second operon involved in the assembly of Fe-S clusters. Represses its own transcription as well as that of toxin rnlA. {ECO:0000269|PubMed:11742080, ECO:0000269|PubMed:16824106, ECO:0000269|PubMed:20421606}.

## Outgoing Edges (30)

- `activates` --> [[gene.b1679|gene.b1679]] `RegulonDB` `S` - regulator=IscR; target=sufE; function=+
- `activates` --> [[gene.b1680|gene.b1680]] `RegulonDB` `C` - regulator=IscR; target=sufS; function=+
- `activates` --> [[gene.b1681|gene.b1681]] `RegulonDB` `S` - regulator=IscR; target=sufD; function=+
- `activates` --> [[gene.b1682|gene.b1682]] `RegulonDB` `S` - regulator=IscR; target=sufC; function=+
- `activates` --> [[gene.b1683|gene.b1683]] `RegulonDB` `C` - regulator=IscR; target=sufB; function=+
- `activates` --> [[gene.b1684|gene.b1684]] `RegulonDB` `S` - regulator=IscR; target=sufA; function=+
- `activates` --> [[gene.b1706|gene.b1706]] `RegulonDB` `S` - regulator=IscR; target=selO; function=+
- `is_component_of` --> [[complex.ecocyc.CPLX0-8083|complex.ecocyc.CPLX0-8083]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b0156|gene.b0156]] `RegulonDB` `S` - regulator=IscR; target=erpA; function=-
- `represses` --> [[gene.b0972|gene.b0972]] `RegulonDB` `S` - regulator=IscR; target=hyaA; function=-
- `represses` --> [[gene.b0973|gene.b0973]] `RegulonDB` `S` - regulator=IscR; target=hyaB; function=-
- `represses` --> [[gene.b0974|gene.b0974]] `RegulonDB` `S` - regulator=IscR; target=hyaC; function=-
- `represses` --> [[gene.b0975|gene.b0975]] `RegulonDB` `S` - regulator=IscR; target=hyaD; function=-
- `represses` --> [[gene.b0976|gene.b0976]] `RegulonDB` `S` - regulator=IscR; target=hyaE; function=-
- `represses` --> [[gene.b0977|gene.b0977]] `RegulonDB` `S` - regulator=IscR; target=hyaF; function=-
- `represses` --> [[gene.b0994|gene.b0994]] `RegulonDB` `C` - regulator=IscR; target=torT; function=-
- `represses` --> [[gene.b2202|gene.b2202]] `RegulonDB` `S` - regulator=IscR; target=napC; function=-
- `represses` --> [[gene.b2203|gene.b2203]] `RegulonDB` `S` - regulator=IscR; target=napB; function=-
- `represses` --> [[gene.b2204|gene.b2204]] `RegulonDB` `S` - regulator=IscR; target=napH; function=-
- `represses` --> [[gene.b2205|gene.b2205]] `RegulonDB` `S` - regulator=IscR; target=napG; function=-
- `represses` --> [[gene.b2206|gene.b2206]] `RegulonDB` `S` - regulator=IscR; target=napA; function=-
- `represses` --> [[gene.b2207|gene.b2207]] `RegulonDB` `S` - regulator=IscR; target=napD; function=-
- `represses` --> [[gene.b2208|gene.b2208]] `RegulonDB` `S` - regulator=IscR; target=napF; function=-
- `represses` --> [[gene.b2528|gene.b2528]] `RegulonDB` `C` - regulator=IscR; target=iscA; function=-
- `represses` --> [[gene.b2529|gene.b2529]] `RegulonDB` `C` - regulator=IscR; target=iscU; function=-
- `represses` --> [[gene.b2530|gene.b2530]] `RegulonDB` `C` - regulator=IscR; target=iscS; function=-
- `represses` --> [[gene.b2531|gene.b2531]] `RegulonDB` `C` - regulator=IscR; target=iscR; function=-
- `represses` --> [[gene.b2630|gene.b2630]] `RegulonDB` `S` - regulator=IscR; target=rnlA; function=-
- `represses` --> [[gene.b2631|gene.b2631]] `RegulonDB` `S` - regulator=IscR; target=rnlB; function=-
- `represses` --> [[gene.b3414|gene.b3414]] `RegulonDB` `S` - regulator=IscR; target=nfuA; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b2531|gene.b2531]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AGK8`
- `KEGG:ecj:JW2515;eco:b2531;ecoc:C3026_14025;`
- `GeneID:86947421;945279;`
- `GO:GO:0003690; GO:0003700; GO:0005506; GO:0005829; GO:0006355; GO:0042802; GO:0051537`

## Notes

HTH-type transcriptional regulator IscR
