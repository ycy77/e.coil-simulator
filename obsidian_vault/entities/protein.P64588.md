---
entity_id: "protein.P64588"
entity_type: "protein"
name: "yqjI"
source_database: "UniProt"
source_id: "P64588"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yqjI b3071 JW3042"
---

# yqjI

`protein.P64588`

## Static

- Type: `protein`
- Source: `UniProt:P64588`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Represses the expression of YqjH which is involved in iron homeostasis under excess nickel conditions. Also represses its own expression. {ECO:0000269|PubMed:21097627}. NfeR, "Ni-responsive Fe uptake regulator" (previously known as YqjI), is a local transcription regulator that represses expression of the divergent operon, yqjH-yqjI, related to its autorepression and the synthesis of an NADPH-dependent ferric reductase . This regulator forms a complex with DNA in the absence of nickel, binding to a 20-bp-long sequence with an imperfect palindromic sequence. YqjI is inactivated under conditions of elevated nickel levels, and the presence of this divalent metal prevents its binding to the target gene. Thus, this regulator maintains the iron homeostasis during high levels of nickel . However, in vitro studies have shown that YqjI can be affected by other divalent metals. The YqjI regulator is structurally related to the PadR family, which is characterized by a winged helix-turn-helix (WHTH) motif. The amino-terminal region of this protein is similar to the C-terminal SlyD protein and to the N-terminal RcnA protein . Comparison with the crystal structure of the AphA protein from Vibrio cholerae suggests that the amino terminal of YqjI contains the WHTH motif and that in the C-terminal domain is located the ligand-binding domain for oligomerization...

## Biological Role

Component of NfeR-Ni(2+) (complex.ecocyc.CPLX0-8069).

## Annotation

FUNCTION: Represses the expression of YqjH which is involved in iron homeostasis under excess nickel conditions. Also represses its own expression. {ECO:0000269|PubMed:21097627}.

## Outgoing Edges (3)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8069|complex.ecocyc.CPLX0-8069]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b3070|gene.b3070]] `RegulonDB` `C` - regulator=NfeR; target=nfeF; function=-
- `represses` --> [[gene.b3071|gene.b3071]] `RegulonDB` `C` - regulator=NfeR; target=nfeR; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b3071|gene.b3071]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P64588`
- `KEGG:ecj:JW3042;eco:b3071;ecoc:C3026_16775;`
- `GeneID:947584;`
- `GO:GO:0003677; GO:0003700; GO:0005829; GO:0006355; GO:0006974; GO:0045892; GO:0045893`

## Notes

Transcriptional regulator YqjI
