---
entity_id: "protein.P0A8V6"
entity_type: "protein"
name: "fadR"
source_database: "UniProt"
source_id: "P0A8V6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00696}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fadR oleR thdB b1187 JW1176"
---

# fadR

`protein.P0A8V6`

## Static

- Type: `protein`
- Source: `UniProt:P0A8V6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00696}.

## Enriched Summary

FUNCTION: Multifunctional regulator of fatty acid metabolism (PubMed:11859088, PubMed:1569108, PubMed:19854834, PubMed:21276098, PubMed:8446033, PubMed:9388199). Represses transcription of at least eight genes required for fatty acid transport and beta-oxidation including fadA, fadB, fadD, fadL and fadE (PubMed:9388199). Activates transcription of at least three genes required for unsaturated fatty acid biosynthesis: fabA, fabB and iclR, the gene encoding the transcriptional regulator of the aceBAK operon encoding the glyoxylate shunt enzymes (PubMed:9388199). {ECO:0000269|PubMed:11859088, ECO:0000269|PubMed:1569108, ECO:0000269|PubMed:19854834, ECO:0000269|PubMed:21276098, ECO:0000269|PubMed:7836365, ECO:0000269|PubMed:8446033, ECO:0000269|PubMed:9388199}. FadR, Fatty acid degradation Regulon , is a multifunctional dual regulator that exerts negative control over the fatty acid degradative regulon and acetate metabolism , whereas it is responsible for maximal expression of unsaturated fatty acid biosynthesis . FadR coordinately regulates fatty acid biosynthesis and fatty acid degradation at the level of transcription . In this way, FadR functions as a switch between fatty acid β-oxidation and fatty acid biosynthesis...

## Biological Role

Component of FadR-an acyl-CoA (complex.ecocyc.MONOMER-51).

## Annotation

FUNCTION: Multifunctional regulator of fatty acid metabolism (PubMed:11859088, PubMed:1569108, PubMed:19854834, PubMed:21276098, PubMed:8446033, PubMed:9388199). Represses transcription of at least eight genes required for fatty acid transport and beta-oxidation including fadA, fadB, fadD, fadL and fadE (PubMed:9388199). Activates transcription of at least three genes required for unsaturated fatty acid biosynthesis: fabA, fabB and iclR, the gene encoding the transcriptional regulator of the aceBAK operon encoding the glyoxylate shunt enzymes (PubMed:9388199). {ECO:0000269|PubMed:11859088, ECO:0000269|PubMed:1569108, ECO:0000269|PubMed:19854834, ECO:0000269|PubMed:21276098, ECO:0000269|PubMed:7836365, ECO:0000269|PubMed:8446033, ECO:0000269|PubMed:9388199}.

## Outgoing Edges (19)

- `activates` --> [[gene.b0185|gene.b0185]] `RegulonDB` `S` - regulator=FadR; target=accA; function=+
- `activates` --> [[gene.b0954|gene.b0954]] `RegulonDB` `S` - regulator=FadR; target=fabA; function=+
- `activates` --> [[gene.b1091|gene.b1091]] `RegulonDB` `C` - regulator=FadR; target=fabH; function=+
- `activates` --> [[gene.b1092|gene.b1092]] `RegulonDB` `C` - regulator=FadR; target=fabD; function=+
- `activates` --> [[gene.b1093|gene.b1093]] `RegulonDB` `C` - regulator=FadR; target=fabG; function=+
- `activates` --> [[gene.b1288|gene.b1288]] `RegulonDB` `S` - regulator=FadR; target=fabI; function=+
- `activates` --> [[gene.b2316|gene.b2316]] `RegulonDB` `S` - regulator=FadR; target=accD; function=+
- `activates` --> [[gene.b2323|gene.b2323]] `RegulonDB` `S` - regulator=FadR; target=fabB; function=+
- `activates` --> [[gene.b3255|gene.b3255]] `RegulonDB` `S` - regulator=FadR; target=accB; function=+
- `activates` --> [[gene.b3256|gene.b3256]] `RegulonDB` `S` - regulator=FadR; target=accC; function=+
- `activates` --> [[gene.b4018|gene.b4018]] `RegulonDB` `C` - regulator=FadR; target=iclR; function=+
- `is_component_of` --> [[complex.ecocyc.MONOMER-51|complex.ecocyc.MONOMER-51]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b0221|gene.b0221]] `RegulonDB` `S` - regulator=FadR; target=fadE; function=-
- `represses` --> [[gene.b1805|gene.b1805]] `RegulonDB` `S` - regulator=FadR; target=fadD; function=-
- `represses` --> [[gene.b2341|gene.b2341]] `RegulonDB` `S` - regulator=FadR; target=fadJ; function=-
- `represses` --> [[gene.b2342|gene.b2342]] `RegulonDB` `S` - regulator=FadR; target=fadI; function=-
- `represses` --> [[gene.b2344|gene.b2344]] `RegulonDB` `C` - regulator=FadR; target=fadL; function=-
- `represses` --> [[gene.b3081|gene.b3081]] `RegulonDB` `S` - regulator=FadR; target=fadH; function=-
- `represses` --> [[gene.b3495|gene.b3495]] `RegulonDB` `C` - regulator=FadR; target=uspA; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b1187|gene.b1187]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A8V6`
- `KEGG:ecj:JW1176;eco:b1187;ecoc:C3026_06990;`
- `GeneID:89516039;93776245;948652;`
- `GO:GO:0000062; GO:0000987; GO:0003700; GO:0005829; GO:0006355; GO:0006631; GO:0019217; GO:0042803; GO:0045723; GO:0045892; GO:0045893`

## Notes

Fatty acid metabolism regulator protein
