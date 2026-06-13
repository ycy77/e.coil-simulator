---
entity_id: "protein.P69786"
entity_type: "protein"
name: "ptsG"
source_database: "UniProt"
source_id: "P69786"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|PROSITE-ProRule:PRU00426, ECO:0000269|PubMed:15919996, ECO:0000305|PubMed:3129430}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00426, ECO:0000305|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ptsG glcA umg b1101 JW1087"
---

# ptsG

`protein.P69786`

## Static

- Type: `protein`
- Source: `UniProt:P69786`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|PROSITE-ProRule:PRU00426, ECO:0000269|PubMed:15919996, ECO:0000305|PubMed:3129430}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00426, ECO:0000305|PubMed:15919996}.

## Enriched Summary

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II complex composed of PtsG and Crr is involved in glucose transport (PubMed:10562420, PubMed:3129430). Also functions as a chemoreceptor monitoring the environment for changes in sugar concentration and an effector modulating the activity of the transcriptional repressor Mlc (PubMed:18319344). In the presence of glucose in the medium, the dephosphorylated form of PtsG can interact with Mlc, leading to sequestration of Mlc in the inner membrane and inhibition of its repressor activity (PubMed:11032803, PubMed:11157755, PubMed:12529317, PubMed:18319344). {ECO:0000269|PubMed:10562420, ECO:0000269|PubMed:11032803, ECO:0000269|PubMed:11157755, ECO:0000269|PubMed:12529317, ECO:0000269|PubMed:18319344, ECO:0000269|PubMed:3129430}.; FUNCTION: (Microbial infection) Probably transports the toxic C-terminal region of CdiA from E.coli strains NC101 and 3006 across the inner membrane to the cytoplasm, where CdiA degrades specific tRNAs. Toxin transport is strain-specific, mutations in this gene do not confer resistance to several other tested CdiA toxins (PubMed:26305955)...

## Biological Role

Component of glucose-specific PTS enzyme II (complex.ecocyc.CPLX-157), Mlc-PtsG (complex.ecocyc.CPLX0-8255).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II complex composed of PtsG and Crr is involved in glucose transport (PubMed:10562420, PubMed:3129430). Also functions as a chemoreceptor monitoring the environment for changes in sugar concentration and an effector modulating the activity of the transcriptional repressor Mlc (PubMed:18319344). In the presence of glucose in the medium, the dephosphorylated form of PtsG can interact with Mlc, leading to sequestration of Mlc in the inner membrane and inhibition of its repressor activity (PubMed:11032803, PubMed:11157755, PubMed:12529317, PubMed:18319344). {ECO:0000269|PubMed:10562420, ECO:0000269|PubMed:11032803, ECO:0000269|PubMed:11157755, ECO:0000269|PubMed:12529317, ECO:0000269|PubMed:18319344, ECO:0000269|PubMed:3129430}.; FUNCTION: (Microbial infection) Probably transports the toxic C-terminal region of CdiA from E.coli strains NC101 and 3006 across the inner membrane to the cytoplasm, where CdiA degrades specific tRNAs. Toxin transport is strain-specific, mutations in this gene do not confer resistance to several other tested CdiA toxins (PubMed:26305955). Probably also serves as the inner membrane receptor for CdiA-STECO31 from E.coli strain STEC_O31 (Probable). {ECO:0000269|PubMed:26305955, ECO:0000305|PubMed:28351921}.

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX-157|complex.ecocyc.CPLX-157]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-8255|complex.ecocyc.CPLX0-8255]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1101|gene.b1101]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69786`
- `KEGG:ecj:JW1087;eco:b1101;ecoc:C3026_06650;`
- `GeneID:93776307;945651;`
- `GO:GO:0005886; GO:0006355; GO:0008982; GO:0009401; GO:0016020; GO:0016301; GO:0055056; GO:0090564; GO:0098708; GO:1902495; GO:1904659`
- `EC:2.7.1.199`

## Notes

PTS system glucose-specific EIICB component (EIICB-Glc) (EII-Glc) [Includes: Glucose permease IIC component (PTS system glucose-specific EIIC component); Glucose-specific phosphotransferase enzyme IIB component (EC 2.7.1.199) (PTS system glucose-specific EIIB component)]
