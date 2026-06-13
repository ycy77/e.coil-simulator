---
entity_id: "protein.P69791"
entity_type: "protein"
name: "chbA"
source_database: "UniProt"
source_id: "P69791"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "chbA celC b1736 JW1725"
---

# chbA

`protein.P69791`

## Static

- Type: `protein`
- Source: `UniProt:P69791`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II ChbABC PTS system is involved in the transport of the chitin disaccharide N,N'-diacetylchitobiose (GlcNAc2) (PubMed:10913117, PubMed:10913118). Also able to use N,N',N''-triacetyl chitotriose (GlcNAc3) (PubMed:10913117). {ECO:0000269|PubMed:10913117, ECO:0000269|PubMed:10913118, ECO:0000305|PubMed:2092358}. ChbA contains a PTS Enzyme IIA domain. IIAchb has been shown to form stable homodimers , though the solution structure of a mutant IIAChb determined by NMR spectroscopy suggests that a homotrimer is the primary oligomeric state of IIAchb. The active site histidine (His89) is located within a crevice formed at the interface of two adjacent subunits of the EIIAChb trimer . A solution structure of a ChbA-ChbB complex has been obtained and the interaction sites mapped. The protruding active site of ChbB containing the active site cysteine residue (Cys10) is buried within the cleft formed by the adjacent subunits of the ChbA trimer . The solution structure of a ChbA-HPr complex shows the active site histidine (His15) of HPr buried within this same cleft...

## Biological Role

Component of N,N'-diacetylchitobiose-specific PTS enzyme II (complex.ecocyc.CPLX-155).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II ChbABC PTS system is involved in the transport of the chitin disaccharide N,N'-diacetylchitobiose (GlcNAc2) (PubMed:10913117, PubMed:10913118). Also able to use N,N',N''-triacetyl chitotriose (GlcNAc3) (PubMed:10913117). {ECO:0000269|PubMed:10913117, ECO:0000269|PubMed:10913118, ECO:0000305|PubMed:2092358}.

## Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX-155|complex.ecocyc.CPLX-155]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1736|gene.b1736]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69791`
- `KEGG:ecj:JW1725;eco:b1736;ecoc:C3026_09920;`
- `GeneID:86859499;93775949;946244;`
- `GO:GO:0005829; GO:0009401; GO:0032991; GO:0090566; GO:1902495; GO:1902815`

## Notes

PTS system N,N'-diacetylchitobiose-specific EIIA component (EIIA-Chb) (EIII-Chb) (IIIcel) (N,N'-diacetylchitobiose-specific phosphotransferase enzyme IIA component)
