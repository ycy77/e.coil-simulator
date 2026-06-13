---
entity_id: "protein.P0ABS1"
entity_type: "protein"
name: "dksA"
source_database: "UniProt"
source_id: "P0ABS1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00926, ECO:0000269|PubMed:16858726}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dksA b0145 JW0141"
---

# dksA

`protein.P0ABS1`

## Static

- Type: `protein`
- Source: `UniProt:P0ABS1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00926, ECO:0000269|PubMed:16858726}.

## Enriched Summary

FUNCTION: Transcription factor that acts by binding directly to the RNA polymerase (RNAP). Required for negative regulation of rRNA expression and positive regulation of several amino acid biosynthesis promoters. Also required for regulation of fis expression. Binding to RNAP disrupts interaction of RNAP with DNA, inhibits formation of initiation complexes, and amplifies effects of ppGpp and the initiating NTP on rRNA transcription. Inhibits transcript elongation, exonucleolytic RNA cleavage and pyrophosphorolysis, and increases intrinsic termination. Also involved, with RecN, in repair of DNA double-strand breaks. Required, probably upstream of the two-component system BarA-UvrY, for expression of CsrA-antagonistic small RNAs CsrB and CsrC (PubMed:21488981). {ECO:0000255|HAMAP-Rule:MF_00926, ECO:0000269|PubMed:15294156, ECO:0000269|PubMed:15294157, ECO:0000269|PubMed:15948952, ECO:0000269|PubMed:16885445, ECO:0000269|PubMed:21488981, ECO:0000269|PubMed:22210857}. The DksA protein binds directly to RNA polymerase, affecting transcript elongation and potentiating allosterically the effect of the alarmone ppGpp on transcription initiation...

## Biological Role

Component of DksA-ppGpp (complex.ecocyc.CPLX0-8070).

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

FUNCTION: Transcription factor that acts by binding directly to the RNA polymerase (RNAP). Required for negative regulation of rRNA expression and positive regulation of several amino acid biosynthesis promoters. Also required for regulation of fis expression. Binding to RNAP disrupts interaction of RNAP with DNA, inhibits formation of initiation complexes, and amplifies effects of ppGpp and the initiating NTP on rRNA transcription. Inhibits transcript elongation, exonucleolytic RNA cleavage and pyrophosphorolysis, and increases intrinsic termination. Also involved, with RecN, in repair of DNA double-strand breaks. Required, probably upstream of the two-component system BarA-UvrY, for expression of CsrA-antagonistic small RNAs CsrB and CsrC (PubMed:21488981). {ECO:0000255|HAMAP-Rule:MF_00926, ECO:0000269|PubMed:15294156, ECO:0000269|PubMed:15294157, ECO:0000269|PubMed:15948952, ECO:0000269|PubMed:16885445, ECO:0000269|PubMed:21488981, ECO:0000269|PubMed:22210857}.

## Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (4)

- `activates` --> [[gene.b4408|gene.b4408]] `RegulonDB` `S` - regulator=DksA; target=csrB; function=+
- `activates` --> [[gene.b4417|gene.b4417]] `RegulonDB` `S` - regulator=DksA; target=rybB; function=+
- `activates` --> [[gene.b4457|gene.b4457]] `RegulonDB` `S` - regulator=DksA; target=csrC; function=+
- `is_component_of` --> [[complex.ecocyc.CPLX0-8070|complex.ecocyc.CPLX0-8070]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `encodes` <-- [[gene.b0145|gene.b0145]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABS1`
- `KEGG:ecj:JW0141;eco:b0145;ecoc:C3026_00630;`
- `GeneID:86862653;93777282;944850;`
- `GO:GO:0005737; GO:0005829; GO:0006302; GO:0006355; GO:0008270; GO:0097216`

## Notes

RNA polymerase-binding transcription factor DksA (DnaK suppressor protein)
