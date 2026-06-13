---
entity_id: "protein.P17334"
entity_type: "protein"
name: "chbC"
source_database: "UniProt"
source_id: "P17334"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|PROSITE-ProRule:PRU00428}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00428}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "chbC celB b1737 JW1726"
---

# chbC

`protein.P17334`

## Static

- Type: `protein`
- Source: `UniProt:P17334`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|PROSITE-ProRule:PRU00428}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00428}.

## Enriched Summary

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II ChbABC PTS system is involved in the transport of the chitin disaccharide N,N'-diacetylchitobiose (GlcNAc2) (PubMed:10913117). Also able to use N,N',N''-triacetyl chitotriose (GlcNAc3) (PubMed:10913117). {ECO:0000269|PubMed:10913117, ECO:0000305|PubMed:2092358}. ChbC contains a PTS Enzyme IIC domain. ChbC is the integral membrane component of the chitobiose PTS and is predicted to contain the sugar binding site . chbC: N,N'-diacetylchitobiose C

## Biological Role

Component of N,N'-diacetylchitobiose-specific PTS enzyme II (complex.ecocyc.CPLX-155).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II ChbABC PTS system is involved in the transport of the chitin disaccharide N,N'-diacetylchitobiose (GlcNAc2) (PubMed:10913117). Also able to use N,N',N''-triacetyl chitotriose (GlcNAc3) (PubMed:10913117). {ECO:0000269|PubMed:10913117, ECO:0000305|PubMed:2092358}.

## Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX-155|complex.ecocyc.CPLX-155]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1737|gene.b1737]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P17334`
- `KEGG:ecj:JW1726;eco:b1737;ecoc:C3026_09925;`
- `GeneID:75171804;945982;`
- `GO:GO:0005886; GO:0008982; GO:0009401; GO:1902495; GO:1902815`

## Notes

PTS system N,N'-diacetylchitobiose-specific EIIC component (EIIC-Chb) (IIcel) (N,N'-diacetylchitobiose-specific phosphotransferase enzyme IIC component)
