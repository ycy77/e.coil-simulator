---
entity_id: "protein.P50456"
entity_type: "protein"
name: "mlc"
source_database: "UniProt"
source_id: "P50456"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}. Note=Interaction with dephosphorylated PtsG leads to the sequestration of Mlc in the inner membrane fraction. {ECO:0000269|PubMed:11032803, ECO:0000269|PubMed:12529317, ECO:0000269|PubMed:18319344}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mlc dgsA b1594 JW1586"
---

# mlc

`protein.P50456`

## Static

- Type: `protein`
- Source: `UniProt:P50456`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}. Note=Interaction with dephosphorylated PtsG leads to the sequestration of Mlc in the inner membrane fraction. {ECO:0000269|PubMed:11032803, ECO:0000269|PubMed:12529317, ECO:0000269|PubMed:18319344}.

## Enriched Summary

FUNCTION: Global regulator of carbohydrate metabolism (PubMed:10464268, PubMed:11361067, PubMed:11934616, PubMed:9484892, PubMed:9484893, PubMed:9781886). Represses the expression of several genes involved in sugar transport and utilization, in particular phosphoenolpyruvate-carbohydrate phosphotransferase system (PTS) genes (PubMed:10464268, PubMed:9484892, PubMed:9484893, PubMed:9781886). Represses expression of ptsG (EIICB(Glc)), which encodes the PTS system glucose-specific EIICB component (PubMed:9781886). Also represses the expression of the manXYZ operon, encoding the mannose-specific PTS system, expression of malT, encoding the transcriptional activator of the maltose regulon, and expression of the pts operon, composed of the genes ptsH, ptsI and crr (PubMed:10464268, PubMed:9484892, PubMed:9484893). Represses its own expression (PubMed:9484893). Acts by binding to the regulatory region of the target genes (PubMed:10464268, PubMed:9484893, PubMed:9781886). {ECO:0000269|PubMed:10464268, ECO:0000269|PubMed:11361067, ECO:0000269|PubMed:11934616, ECO:0000269|PubMed:9484892, ECO:0000269|PubMed:9484893, ECO:0000269|PubMed:9781886}. DgsA, better known as Mlc, "makes large colonies," is a transcriptional dual regulator that controls the expression of a number of genes encoding enzymes of the Escherichia coli phosphotransferase (PTS) and phosphoenolpyruvate (PEP) systems...

## Biological Role

Component of Mlc-PtsG (complex.ecocyc.CPLX0-8255).

## Annotation

FUNCTION: Global regulator of carbohydrate metabolism (PubMed:10464268, PubMed:11361067, PubMed:11934616, PubMed:9484892, PubMed:9484893, PubMed:9781886). Represses the expression of several genes involved in sugar transport and utilization, in particular phosphoenolpyruvate-carbohydrate phosphotransferase system (PTS) genes (PubMed:10464268, PubMed:9484892, PubMed:9484893, PubMed:9781886). Represses expression of ptsG (EIICB(Glc)), which encodes the PTS system glucose-specific EIICB component (PubMed:9781886). Also represses the expression of the manXYZ operon, encoding the mannose-specific PTS system, expression of malT, encoding the transcriptional activator of the maltose regulon, and expression of the pts operon, composed of the genes ptsH, ptsI and crr (PubMed:10464268, PubMed:9484892, PubMed:9484893). Represses its own expression (PubMed:9484893). Acts by binding to the regulatory region of the target genes (PubMed:10464268, PubMed:9484893, PubMed:9781886). {ECO:0000269|PubMed:10464268, ECO:0000269|PubMed:11361067, ECO:0000269|PubMed:11934616, ECO:0000269|PubMed:9484892, ECO:0000269|PubMed:9484893, ECO:0000269|PubMed:9781886}.

## Outgoing Edges (8)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8255|complex.ecocyc.CPLX0-8255]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `represses` --> [[gene.b1101|gene.b1101]] `RegulonDB` `S` - regulator=Mlc; target=ptsG; function=-
- `represses` --> [[gene.b1593|gene.b1593]] `RegulonDB` `S` - regulator=Mlc; target=bidA; function=-
- `represses` --> [[gene.b1594|gene.b1594]] `RegulonDB` `S` - regulator=Mlc; target=mlc; function=-
- `represses` --> [[gene.b2415|gene.b2415]] `RegulonDB` `S` - regulator=Mlc; target=ptsH; function=-
- `represses` --> [[gene.b2416|gene.b2416]] `RegulonDB` `S` - regulator=Mlc; target=ptsI; function=-
- `represses` --> [[gene.b2417|gene.b2417]] `RegulonDB` `S` - regulator=Mlc; target=crr; function=-
- `represses` --> [[gene.b3418|gene.b3418]] `RegulonDB` `S` - regulator=Mlc; target=malT; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b1594|gene.b1594]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P50456`
- `KEGG:ecj:JW1586;eco:b1594;ecoc:C3026_09180;`
- `GeneID:945510;`
- `GO:GO:0003677; GO:0005737; GO:0006351; GO:0006355; GO:0016020; GO:0042802; GO:0046872`

## Notes

DNA-binding transcriptional repressor Mlc (Making large colonies protein) (Membrane linked control)
