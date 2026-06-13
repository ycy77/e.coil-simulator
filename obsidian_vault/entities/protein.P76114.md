---
entity_id: "protein.P76114"
entity_type: "protein"
name: "mcbR"
source_database: "UniProt"
source_id: "P76114"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mcbR yncC b1450 JW1445"
---

# mcbR

`protein.P76114`

## Static

- Type: `protein`
- Source: `UniProt:P76114`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Important for biofilm formation. Represses expression of McbA by binding to its promoter region, which prevents colanic acid overproduction and mucoidy. {ECO:0000269|PubMed:18309357}. McbR is a member of the FadR C-terminal domain (FCD) family of the GntR superfamily of transcriptional regulators . It is probable that McbR binds to DNA as a dimer . Residues of McbR that could interact with DNA-binding sites are Lys38 with the α2-helix and Thr49 with the α3-helix. In addition, Arg34 and Arg52 are also important for the DNA-binding site . McbR (YncC) regulates biofilm formation and mucoidity by repressing expression of mcbA (ybiM) . McbA belongs to the YhcN family of periplasmic proteins and is induced by the quorum-sensing signal autoinducer 2 (AI-2) . McbR is negatively autoregulated and, in addition, repressed by YgiV . Expression of mcbR is induced by overexpression of the lsr operon regulators LsrR and LsrK, the quorum-sensing regulator MqsR, and the AI-2 exporter TqsA . McbR carries a helix-turn-helix DNA-binding motif (aa 37-56) and represses transcription of mcbA by binding to the promoter region of mcbA . The crystal structure of McbR has been determined to 2.1 Å . Overexpression of mcbR from an ASKA plasmid leads to a more than 3-fold increase in the MIC of hydrogen peroxide . An mcbR knockout mutant is able to growth faster than the wild type...

## Annotation

FUNCTION: Important for biofilm formation. Represses expression of McbA by binding to its promoter region, which prevents colanic acid overproduction and mucoidy. {ECO:0000269|PubMed:18309357}.

## Outgoing Edges (6)

- `activates` --> [[gene.b0953|gene.b0953]] `RegulonDB` `S` - regulator=McbR; target=rmf; function=+
- `activates` --> [[gene.b1257|gene.b1257]] `RegulonDB` `S` - regulator=McbR; target=yciE; function=+
- `activates` --> [[gene.b1258|gene.b1258]] `RegulonDB` `S` - regulator=McbR; target=yciF; function=+
- `activates` --> [[gene.b1259|gene.b1259]] `RegulonDB` `S` - regulator=McbR; target=yciG; function=+
- `activates` --> [[gene.b3995|gene.b3995]] `RegulonDB` `S` - regulator=McbR; target=rsd; function=+
- `represses` --> [[gene.b0806|gene.b0806]] `RegulonDB` `S` - regulator=McbR; target=mcbA; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b1450|gene.b1450]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76114`
- `KEGG:ecj:JW1445;eco:b1450;ecoc:C3026_08435;`
- `GeneID:946014;`
- `GO:GO:0000987; GO:0003700; GO:0006355; GO:0045892`

## Notes

HTH-type transcriptional regulator McbR
