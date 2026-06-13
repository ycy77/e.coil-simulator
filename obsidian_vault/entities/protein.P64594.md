---
entity_id: "protein.P64594"
entity_type: "protein"
name: "yhaV"
source_database: "UniProt"
source_id: "P64594"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yhaV b3130 JW3099"
---

# yhaV

`protein.P64594`

## Static

- Type: `protein`
- Source: `UniProt:P64594`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Toxic component of a type II toxin-antitoxin (TA) system. Has RNase activity in vitro. Overexpression leads to growth arrest after 30 minutes; these effects are overcome by concomitant expression of antitoxin SohA (PrlF). Massive overexpression is toxic. Unlike most other characterized TA systems degrades rRNA, and co-folding of the both TA proteins is necessary in vitro for inhibition of the RNase activity. It is not known if it has any sequence-specificity. Acts as a transcription factor. The YhaV/PrlF complex binds the prlF-yhaV operon, probably negatively regulating its expression. {ECO:0000269|PubMed:17706670}. YhaV is a BECR-fold toxin in the RelE/ParE superfamily of type II toxin-antitoxin systems and the ribonuclease toxin component of the YhaV-PrlF toxin-antitoxin system . The ribonuclease activity of YhaV is dependent on the presence of the ribosome . YhaV associates with the 70S ribosome and the 50S ribosomal subunit in a ribosomal profiling assay . Residues 131-145 at the C terminus of YhaV are involved in its mRNA interferase activity . An analysis of the targets and site specificity of YhaV showed some cleavage site specificity, favoring a G immediately downstream of the cleavage site, a preference for cleavage in the 5' end of mRNAs, and high codon position preference. Like other E...

## Biological Role

Catalyzes RXN0-6528 (reaction.ecocyc.RXN0-6528). Component of YhaV-PrlF toxin-antitoxin complex (complex.ecocyc.CPLX0-7624).

## Annotation

FUNCTION: Toxic component of a type II toxin-antitoxin (TA) system. Has RNase activity in vitro. Overexpression leads to growth arrest after 30 minutes; these effects are overcome by concomitant expression of antitoxin SohA (PrlF). Massive overexpression is toxic. Unlike most other characterized TA systems degrades rRNA, and co-folding of the both TA proteins is necessary in vitro for inhibition of the RNase activity. It is not known if it has any sequence-specificity. Acts as a transcription factor. The YhaV/PrlF complex binds the prlF-yhaV operon, probably negatively regulating its expression. {ECO:0000269|PubMed:17706670}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN0-6528|reaction.ecocyc.RXN0-6528]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-7624|complex.ecocyc.CPLX0-7624]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b3130|gene.b3130]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P64594`
- `KEGG:ecj:JW3099;eco:b3130;ecoc:C3026_17060;`
- `GeneID:947638;`
- `GO:GO:0004521; GO:0004540; GO:0006355; GO:0006402; GO:0016787; GO:0030308; GO:0040008; GO:0042803; GO:0043023; GO:0044010; GO:0110001`
- `EC:3.1.-.-`

## Notes

Ribonuclease toxin YhaV (EC 3.1.-.-) (Ribonuclease YhaV)
