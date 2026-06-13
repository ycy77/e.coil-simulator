---
entity_id: "protein.P0ACU0"
entity_type: "protein"
name: "cecR"
source_database: "UniProt"
source_id: "P0ACU0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cecR ybiH b0796 JW0780"
---

# cecR

`protein.P0ACU0`

## Static

- Type: `protein`
- Source: `UniProt:P0ACU0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Regulates transcription of the cecR-ybhGFSR operon and the rhlE gene, which altogether are involved in the control of sensitivity to cefoperazone and chloramphenicol. Represses the cecR-ybhGFSR operon and activates the rhlE operon. Acts by binding to a palindromic sequence within the intergenic spacer located between these two divergently transcribed operons. {ECO:0000269|PubMed:27112147}. CecR (also known as YbiH) is a TetR-family (subfamily D) transcription factor originally described as a "Cefoperazone and chloramphenicol Regulator" [Yamanaka16] and confirmed as a TF through an integrated workflow comprised of computational prediction, knowledge-based classification, and experimental validation of candidate TFs at the genome scale . CecR controls genes involved in sensitivity to cefoperazone and chloramphenicol . CecR functions as an all-helical TetR-like homodimer, and each protomer contains an N-terminal DNA-binding domain with a helix-turn-helix (HTH) motif and a C-terminal ligand-recognition domain . The CecR crystal structure (1.91 Å) shows a C-terminal effector-binding cavity with an uncommon tunnel-like architecture (~35 Å long; with volume of ~399 Å3) that can accommodate polyethylene glycol fragments from the crystallization solution, consistent with a potential ligand-binding site...

## Annotation

FUNCTION: Regulates transcription of the cecR-ybhGFSR operon and the rhlE gene, which altogether are involved in the control of sensitivity to cefoperazone and chloramphenicol. Represses the cecR-ybhGFSR operon and activates the rhlE operon. Acts by binding to a palindromic sequence within the intergenic spacer located between these two divergently transcribed operons. {ECO:0000269|PubMed:27112147}.

## Outgoing Edges (6)

- `activates` --> [[gene.b0797|gene.b0797]] `RegulonDB` `C` - regulator=CecR; target=rhlE; function=+
- `represses` --> [[gene.b0792|gene.b0792]] `RegulonDB` `C` - regulator=CecR; target=ybhR; function=-
- `represses` --> [[gene.b0793|gene.b0793]] `RegulonDB` `C` - regulator=CecR; target=ybhS; function=-
- `represses` --> [[gene.b0794|gene.b0794]] `RegulonDB` `C` - regulator=CecR; target=ybhF; function=-
- `represses` --> [[gene.b0795|gene.b0795]] `RegulonDB` `C` - regulator=CecR; target=ybhG; function=-
- `represses` --> [[gene.b0796|gene.b0796]] `RegulonDB` `C` - regulator=CecR; target=cecR; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b0796|gene.b0796]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACU0`
- `KEGG:ecj:JW0780;eco:b0796;ecoc:C3026_05030;`
- `GeneID:75170861;75204911;945421;`
- `GO:GO:0000976; GO:0003700; GO:0005737; GO:0006351; GO:0006355; GO:0042802; GO:2000143; GO:2000144`

## Notes

HTH-type transcriptional dual regulator CecR (Regulator of cefoperazone and chloramphenicol sensitivity)
