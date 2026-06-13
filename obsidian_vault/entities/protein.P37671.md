---
entity_id: "protein.P37671"
entity_type: "protein"
name: "plaR"
source_database: "UniProt"
source_id: "P37671"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "plaR yiaJ b3574 JW3546"
---

# plaR

`protein.P37671`

## Static

- Type: `protein`
- Source: `UniProt:P37671`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Transcription factor involved in the utilization of L-ascorbate (PubMed:30137486, PubMed:31892694). Negatively controls the transcription of the yiaKLMNOPQRS (yiaK-S or yiaK-yiaL-yiaM-yiaN-yiaO-lyxK-sgbH-sgbU-sgbE) operon, which is involved in the L-ascorbate degradation pathway (PubMed:10913096, PubMed:30137486). It may repress the ascorbate utilization pathway, therefore regulating the level of D-xylulose-5-phosphate that feeds into the pentose phosphate pathway (PubMed:30137486). It is involved in the utilization of plant-derived materials as nutrients for survival, including ascorbate from fruits and galacturonate from plant pectin (PubMed:31892694). In addition, the targets include genes involved in the utilization of other plant-derived materials as nutrients such as fructose, sorbitol, glycerol and fructoselysine (PubMed:31892694). Acts by binding to specific DNA sequences (PlaR-box) in the promoter regions of target operons, repressing their transcription (PubMed:10913096, PubMed:31892694). {ECO:0000269|PubMed:10913096, ECO:0000269|PubMed:30137486, ECO:0000269|PubMed:31892694}. YiaJ is a transcriptional repressor that negatively controls the expression of genes involved in the catabolism of the rare pentose L-lyxose...

## Annotation

FUNCTION: Transcription factor involved in the utilization of L-ascorbate (PubMed:30137486, PubMed:31892694). Negatively controls the transcription of the yiaKLMNOPQRS (yiaK-S or yiaK-yiaL-yiaM-yiaN-yiaO-lyxK-sgbH-sgbU-sgbE) operon, which is involved in the L-ascorbate degradation pathway (PubMed:10913096, PubMed:30137486). It may repress the ascorbate utilization pathway, therefore regulating the level of D-xylulose-5-phosphate that feeds into the pentose phosphate pathway (PubMed:30137486). It is involved in the utilization of plant-derived materials as nutrients for survival, including ascorbate from fruits and galacturonate from plant pectin (PubMed:31892694). In addition, the targets include genes involved in the utilization of other plant-derived materials as nutrients such as fructose, sorbitol, glycerol and fructoselysine (PubMed:31892694). Acts by binding to specific DNA sequences (PlaR-box) in the promoter regions of target operons, repressing their transcription (PubMed:10913096, PubMed:31892694). {ECO:0000269|PubMed:10913096, ECO:0000269|PubMed:30137486, ECO:0000269|PubMed:31892694}.

## Outgoing Edges (14)

- `represses` --> [[gene.b1850|gene.b1850]] `RegulonDB|EcoCyc` `C` - regulator=PlaR; target=eda; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b2240|gene.b2240]] `RegulonDB|EcoCyc` `S` - regulator=PlaR; target=glpT; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b2241|gene.b2241]] `RegulonDB|EcoCyc` `C` - regulator=PlaR; target=glpA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b3090|gene.b3090]] `RegulonDB|EcoCyc` `C` - regulator=PlaR; target=ygjV; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b3574|gene.b3574]] `RegulonDB` `C` - regulator=PlaR; target=plaR; function=-
- `represses` --> [[gene.b3575|gene.b3575]] `RegulonDB` `C` - regulator=PlaR; target=yiaK; function=-
- `represses` --> [[gene.b3576|gene.b3576]] `RegulonDB` `C` - regulator=PlaR; target=yiaL; function=-
- `represses` --> [[gene.b3577|gene.b3577]] `RegulonDB` `C` - regulator=PlaR; target=yiaM; function=-
- `represses` --> [[gene.b3578|gene.b3578]] `RegulonDB` `C` - regulator=PlaR; target=yiaN; function=-
- `represses` --> [[gene.b3579|gene.b3579]] `RegulonDB` `C` - regulator=PlaR; target=yiaO; function=-
- `represses` --> [[gene.b3580|gene.b3580]] `RegulonDB` `C` - regulator=PlaR; target=lyxK; function=-
- `represses` --> [[gene.b3581|gene.b3581]] `RegulonDB` `C` - regulator=PlaR; target=sgbH; function=-
- `represses` --> [[gene.b3582|gene.b3582]] `RegulonDB` `C` - regulator=PlaR; target=sgbU; function=-
- `represses` --> [[gene.b3583|gene.b3583]] `RegulonDB` `C` - regulator=PlaR; target=sgbE; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b3574|gene.b3574]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37671`
- `KEGG:ecj:JW3546;eco:b3574;ecoc:C3026_19380;`
- `GeneID:948084;`
- `GO:GO:0003677; GO:0003700; GO:0045892`

## Notes

HTH-type transcriptional repressor PlaR (Regulator of plant utilization) (YiaKLMNOPQRS operon repressor) (YiaK-S operon repressor)
