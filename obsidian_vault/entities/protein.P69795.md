---
entity_id: "protein.P69795"
entity_type: "protein"
name: "chbB"
source_database: "UniProt"
source_id: "P69795"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "chbB celA b1738 JW1727"
---

# chbB

`protein.P69795`

## Static

- Type: `protein`
- Source: `UniProt:P69795`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II ChbABC PTS system is involved in the transport of the chitin disaccharide N,N'-diacetylchitobiose (GlcNAc2) (PubMed:10913117). Also able to use N,N',N''-triacetyl chitotriose (GlcNAc3) (PubMed:10913117, PubMed:10913119). {ECO:0000269|PubMed:10913117, ECO:0000269|PubMed:10913119, ECO:0000305|PubMed:2092358}. ChbB contains a PTS Enzyme IIB domain. Cys10 is the site of phosphotransfer during the PTScbh reaction sequence . The 3-dimensional structure of IIBChb has been determined by NMR spectroscopy and by X-ray crystallography to a resolution of 1.8 Å . A solution structure of a ChbB-ChbA complex has been obtained and the interaction sites mapped. The protruding active site of ChbB containing the active site cysteine residue (Cys10) is buried within the cleft formed by the adjacent subunits of the ChbA trimer . chbB: N,N'-diacetylchitobiose B

## Biological Role

Component of N,N'-diacetylchitobiose-specific PTS enzyme II (complex.ecocyc.CPLX-155).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II ChbABC PTS system is involved in the transport of the chitin disaccharide N,N'-diacetylchitobiose (GlcNAc2) (PubMed:10913117). Also able to use N,N',N''-triacetyl chitotriose (GlcNAc3) (PubMed:10913117, PubMed:10913119). {ECO:0000269|PubMed:10913117, ECO:0000269|PubMed:10913119, ECO:0000305|PubMed:2092358}.

## Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX-155|complex.ecocyc.CPLX-155]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1738|gene.b1738]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69795`
- `KEGG:ecj:JW1727;eco:b1738;ecoc:C3026_09930;`
- `GeneID:86859497;93775951;945339;`
- `GO:GO:0005829; GO:0008982; GO:0009401; GO:0016301; GO:0090563; GO:0090566; GO:1902495; GO:1902815`
- `EC:2.7.1.196`

## Notes

PTS system N,N'-diacetylchitobiose-specific EIIB component (EIIB-Chb) (IVcel) (N,N'-diacetylchitobiose-specific phosphotransferase enzyme IIB component) (EC 2.7.1.196)
